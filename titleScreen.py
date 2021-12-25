import pygame
import pygame.freetype

class TitleScreen:
    def __init__(self, scale, width, height):
        self.FONT = pygame.freetype.Font("ThaleahFat.ttf", 12 * scale)
        self.POSITION = [width, height]
        self.SCALE = scale
        self.rect = None

    def update(self):
        pass

    def render(self, screen):
        self.rect = self.FONT.render_to(screen, ((screen.get_rect().center[0]/3), screen.get_rect().center[1]/4), "Decent Adventure", (0,0,0))
        

    def frame(self, screen, dt, fps):
        self.render(screen)