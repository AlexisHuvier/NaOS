import pygame
import logging
import os
from datetime import datetime
import sys

pygame.init()
pygame.fastevent.init()

from naos.utils import Color, Database, Font, FileSystem
from naos.graphics.entities import *
from naos.graphics.widgets import *
from naos.program import ProgramManager

class NaOS:
    def __init__(self, debug=False):
        self.paths = {
            "files": os.path.join(os.getenv('APPDATA'), "NaOS"),
            "system": os.path.join(os.getenv('APPDATA'), "NaOS", "system"),
            "user": os.path.join(os.getenv('APPDATA'), "NaOS", "user"),
            "programs": os.path.join(os.getenv('APPDATA'), "NaOS", "programs"),
        }
        self.fs = FileSystem(self)
        for v in self.paths.values():
            if not os.path.exists(v):
                os.makedirs(v)
        self.db = Database(os.path.join(self.paths["system"], "data.db"))
        self.db.createdb()

        self.width = 1920
        self.height = 1080 

        pygame.display.set_caption("NaOS")
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN | pygame.SCALED)

        self.clock = pygame.time.Clock()
        self.is_running = False

        self.bg_color = Color.from_name("BLACK")
        self.debug = debug
        if self.debug:
            self.debug_font = Font()
        
        background = self.db.executewithreturn("""SELECT background FROM parameters""")[0][0]
        self.bg = None
        self.set_background(background)

        self.naosbar = NaOSBar()
        self.startmenu = StartMenu(self)
        self.windows = []
        self.focused_window = None
        self.startmenu.naos = self
        self.naosbar.naos = self
        self.program_manager = ProgramManager()

    def set_background(self, background):
        if background is not None:
            self.bg = pygame.image.load(os.path.join(self.paths["files"], background.replace("/", "\\"))).convert()
            self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
            self.db.executewithoutreturn("""UPDATE parameters SET background = ?""", (background,))

    def focus_window(self, window):
        if self.focused_window is not None:
            self.focused_window.focus = False
        self.focused_window = window
        if window is not None:
            window.focus = True

    def open_window(self, window):
        self.windows.append(window)
        window.naos = self
        self.focus_window(window)

    def stop(self):
        self.is_running = False
    
    def run(self):
        self.is_running = True
        while self.is_running:
            for event in pygame.fastevent.get():
                self.process_event(event)

            for i in self.windows:
                i.update()
            self.naosbar.update()
            
            self.screen.fill(self.bg_color.get_rgba())
            if self.bg is not None:
                self.screen.blit(self.bg, (0, 0))

            for i in self.windows:
                if self.focused_window is None or i != self.focused_window:
                    i.show(self.screen)
            if self.focused_window is not None:
                self.focused_window.show(self.screen)
            self.startmenu.show(self.screen)
            self.naosbar.show(self.screen)

            if self.debug:
                try:
                    fps_label = self.debug_font.render("FPS : " + str(round(self.clock.get_fps())))
                except OverflowError:
                    fps_label = self.debug_font.render("FPS : Infinity")
                self.screen.blit(fps_label, (10, 10))


            self.clock.tick()
            pygame.display.update()
        
        pygame.quit()
    
    def process_event(self, evt):
        if evt.type == pygame.QUIT:
            self.stop()
        else:
            if self.focused_window is not None and self.focused_window.event(evt):
                return

            for i in range(len(self.windows)-1, -1, -1):
                window = self.windows[i]
                if self.focused_window != window and window.event(evt):
                    if window in self.windows:
                        self.focus_window(window)
                    return
            
            if self.naosbar.event(evt) or self.startmenu.event(evt):
                return
        
        if evt.type == pygame.KEYUP and evt.key == pygame.K_PRINTSCREEN:
            pygame.image.save(self.screen, os.path.join(self.paths["user"], "screenshot_"+datetime.now().strftime("%d-%m-%Y_%H-%M-%S")+".jpg"))



def launch():
    if len(sys.argv) == 2 and sys.argv[1] == "--debug":
        NaOS(True).run()
    else:
        NaOS().run()
    
if __name__ == "__main__":
    launch()