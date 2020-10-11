import pygame
import logging
import os
import sys

pygame.init()

from naos.utils import Color, Database, Font
from naos.graphics.entities import *

class NaOS:
    def __init__(self, debug=False):
        self.paths = {
            "files": os.path.join(os.getenv('APPDATA'), "NaOS"),
            "users_files": os.path.join(os.getenv('APPDATA'), "NaOS", "users"),
            "programs_files": os.path.join(os.getenv('APPDATA'), "NaOS", "programs"),
        }
        self.db = Database(os.path.join(os.path.dirname(__file__), "files", "data.db"))
        self.db.createdb()
        for v in self.paths.values():
            if not os.path.exists(v):
                os.makedirs(v)

        pygame.display.set_caption("NaOS")
        self.screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN | pygame.SCALED)

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
            self.bg = pygame.transform.scale(self.bg, (1920, 1080))

        self.naosbar = NaOSBar()
        self.startmenu = StartMenu()
        test = Window("More Advanced Test", 480, 300, 500, 500)
        test.add_widget(Label(0, 0, "Ceci est un bon test je trouve."))
        self.windows = [Window("Test", 200, 200), test]
        for i in self.windows:
            i.naos = self
        self.startmenu.naos = self
        self.naosbar.naos = self

    def stop(self):
        self.is_running = False
    
    def run(self):
        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():
                self.process_event(event)
            
            self.screen.fill(self.bg_color.get_rgba())
            if self.bg is not None:
                self.screen.blit(self.bg, (0, 0))

            for i in self.windows:
                i.show(self.screen)
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
        else:
            for i in range(len(self.windows)):
                entity = self.windows[i]
                if entity.event(evt):
                    if entity in self.windows:
                        self.windows = self.windows[:i] + self.windows[i+1:] + [self.windows[i]]
                    return
            self.naosbar.event(evt)



def launch():
    if len(sys.argv) == 2 and sys.argv[1] == "--debug":
        NaOS(True).run()
    else:
        NaOS().run()
    
if __name__ == "__main__":
    launch()