import pygame, time, os

class Player:

    def __init__(self, x_pos, y_pos, width, height):
        self.position = [x_pos, y_pos]
        self.size = [width, height]
        self.flipped = False
        self.state = "IDLE"
        self.spritePack = "IDLE"
        self.sprites = []
        self.velocity = 200

        for filename in os.listdir(f"./images/playerAnims/{self.spritePack}"):
            self.sprites.append(pygame.transform.scale(pygame.image.load(f"./images/playerAnims/{self.spritePack}/{filename}"), (self.size[0], self.size[1])))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        

    def update(self, dt, fps):
        
        if self.spritePack != self.state:
            self.spritePack = self.state
            self.sprites = []
            for filename in os.listdir(f"./images/playerAnims/{self.spritePack}"):
                self.sprites.append(pygame.transform.scale(pygame.image.load(f"./images/playerAnims/{self.spritePack}/{filename}"), (self.size[0], self.size[1])))
            self.current_sprite = 0

        self.current_sprite += 6 * dt

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

        if self.flipped:
            self.image = pygame.transform.flip(self.image, True, False)


    def movement(self, keys, deltatime, fps):
        print(deltatime, deltatime * self.velocity)
        if keys[pygame.K_a] and self.rect.x - self.velocity * deltatime > 0:
            self.state = "RUNNING"
            self.position[0] -= (self.velocity * deltatime)
            self.rect.x = self.position[0]
            self.flipped = True
        elif keys[pygame.K_d] and self.rect.x - self.velocity * deltatime < 853:
            self.state = "RUNNING"
            self.position[0] += self.velocity * deltatime
            self.rect.x = self.position[0]
            self.flipped = False
        else:
            self.state = "IDLE"

    def render(self, screen, deltatime, fps):
        screen.blit(self.image, self.rect)
        self.movement(pygame.key.get_pressed(), deltatime, fps)

    def frame(self, WINDOW, dt, fps):
            self.render(WINDOW, dt, fps)
            self.update(dt, fps)