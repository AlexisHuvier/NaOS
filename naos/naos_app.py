import pygame
import logging
import os
import sys

pygame.init()

from naos.utils import Color
from naos.graphics.entities import NaOSBar, Window

class NaOS:
    def __init__(self, debug=False):
        self.paths = {
            "files": os.path.join(os.getenv('APPDATA'), "NaOS"),
            "users_files": os.path.join(os.getenv('APPDATA'), "NaOS", "users"),
            "programs_files": os.path.join(os.getenv('APPDATA'), "NaOS", "programs"),
        }
        for v in self.paths.values():
            if not os.path.exists(v):
                os.makedirs(v)

        self.bg_color = Color.from_name("BLACK")
        self.debug = debug
        if self.debug:
            self.debug_font = pygame.font.SysFont("Arial", 15, 1)
    
        pygame.display.set_caption("NaOS")
        self.screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN | pygame.SCALED)

        self.clock = pygame.time.Clock()
        self.is_running = False

        self.naosbar = NaOSBar()
        self.entities = [Window("Test", 200, 200), Window("Test2", 500, 500, 300)]
        for i in self.entities:
            i.naos = self

    def stop(self):
        self.is_running = False
    
    def run(self):
        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():
                self.process_event(event)
            
            self.screen.fill(self.bg_color.get_rgba())

            for i in self.entities:
                i.show(self.screen)
            self.naosbar.show(self.screen)

            if self.debug:
                try:
                    fps_label = self.debug_font.render("FPS : " + str(round(self.clock.get_fps())), 0, Color.from_name("WHITE").get_rgba())
                except OverflowError:
                    fps_label = self.debug_font.render("FPS : Infinity", 0, Color.from_name("WHITE").get_rgba())
                self.screen.blit(fps_label, (10, 10))


            self.clock.tick()
            pygame.display.update()
        
        pygame.quit()
    
    def process_event(self, evt):
        if evt.type == pygame.QUIT or (evt.type == pygame.KEYUP and evt.key == pygame.K_ESCAPE):
            self.stop()
        else:
            for i in self.entities:
                if i.event(evt):
                    break



def launch():
    if len(sys.argv) == 2 and sys.argv[1] == "--debug":
        NaOS(True).run()
    else:
        NaOS().run()
    
if __name__ == "__main__":
    launch()