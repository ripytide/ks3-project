import pygame

white = (255, 255, 255)
width = 10
height = 60

class Paddle(pygame.sprite.Sprite):
    def __init__(self, position, up_key, down_key):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(white)

        self.rect = self.image.get_rect()
        self.rect.center = position

        self.up_key = up_key
        self.down_key = down_key

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.up_key]:
            self.rect.y = self.rect.y - 4
        if keys[self.down_key]:
            self.rect.y = self.rect.y + 4
