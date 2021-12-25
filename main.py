from player import Player
import pygame, time
from titleScreen import TitleScreen

pygame.init()

logo = pygame.image.load("images/logo.png")
displayInfo = pygame.display.Info()
scale = displayInfo.current_h/144
clock = pygame.time.Clock()
fps = 60
renderingObjects = []

WIDTH, HEIGHT = 128 * scale, 72 * scale
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

renderingObjects.append(TitleScreen(scale, WIDTH, HEIGHT))
renderingObjects.append(Player(0, 100, 48, 93))

pygame.display.set_caption("Decent Adventure")
pygame.display.set_icon(logo)

def draw_window(dt):
    WINDOW.fill((255,255,255))

    for object in renderingObjects:
        object.frame(WINDOW, dt, fps)

    pygame.display.update()

def main():
    prev_time = time.time()
    running = True
    while running:
        clock.tick(fps)

        now = time.time()
        dt = now-prev_time
        prev_time = now
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_window(dt)

    pygame.quit()

if __name__ == "__main__":
    main()