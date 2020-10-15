import pygame
import logging
import os
import sys

pygame.init()

from naos.utils import Color, Database, Font
from naos.graphics.entities import *
from naos.graphics.widgets import *

class NaOS:
    def __init__(self, debug=False):
        self.paths = {
            "files": os.path.join(os.getenv('APPDATA'), "NaOS"),
            "system": os.path.join(os.getenv('APPDATA'), "NaOS", "system"),
            "users": os.path.join(os.getenv('APPDATA'), "NaOS", "users"),
            "programs": os.path.join(os.getenv('APPDATA'), "NaOS", "programs"),
        }
        for v in self.paths.values():
            if not os.path.exists(v):
                os.makedirs(v)
        self.db = Database(os.path.join(self.paths["system"], "data.db"))
        self.db.createdb()

        self.width = 1920 # min 600x500 environ
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
        if background is not None:
            self.bg = pygame.image.load(os.path.join(self.paths["files"], background.replace("/", "\\"))).convert()
            self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

        self.naosbar = NaOSBar()
        self.startmenu = StartMenu()
        test = Window("More Advanced Test", 480, 300, 500, 500)
        test.add_widget(Label(2, 2, "Ceci est un bon test je trouve."))
        test.add_widget(Label(2, 50, "Ceci est un test\nAvec plusieurs lignes.\nNon ?"))
        test.add_widget(Button(2, 200, "Close", test.close))
        self.windows = [Window("Test with a long title", 200, 200), test]
        for i in self.windows:
            i.naos = self
        self.windows[-1].focus = True
        self.startmenu.naos = self
        self.naosbar.naos = self

    def get_focused_window(self):
        for i in self.windows:
            if i.focus:
                return i

    def stop(self):
        self.is_running = False
    
    def run(self):
        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():
                self.process_event(event)

            for i in self.windows:
                i.update()
            
            self.screen.fill(self.bg_color.get_rgba())
            if self.bg is not None:
                self.screen.blit(self.bg, (0, 0))

            for i in self.windows:
                if not i.focus:
                    i.show(self.screen)
            if self.get_focused_window() is not None:
                self.get_focused_window().show(self.screen)
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
        if evt.type == pygame.QUIT or (evt.type == pygame.KEYUP and evt.key == pygame.K_ESCAPE):
            self.stop()
        if evt.type == pygame.KEYUP and evt.key == pygame.K_p:
            pygame.image.save(self.screen, os.path.join(self.paths["users"], "screenshot.jpg"))
        else:
            if self.get_focused_window() is not None and self.get_focused_window().event(evt):
                return
            
            for i in self.windows:
                if self.get_focused_window() != i and i.event(evt):
                    if self.get_focused_window() is not None:
                        self.get_focused_window().focus = False
                    i.focus = True
                    return
            self.naosbar.event(evt)



def launch():
    if len(sys.argv) == 2 and sys.argv[1] == "--debug":
        NaOS(True).run()
    else:
        NaOS().run()
    
if __name__ == "__main__":
    launch()