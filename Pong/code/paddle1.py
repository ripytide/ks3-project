import pygame

white = (255, 255, 255)
width = 10
height = 60

class Paddle(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(white)

        self.rect = self.image.get_rect()
        self.rect.center = position
