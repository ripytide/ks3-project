import pygame

white = (255, 255, 255)
starting_position = [250, 250]
width = 10
height = 10

class Ball(pygame.sprite.Sprite):
    def __init__(self, x_velocity, y_velocity):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(white)

        self.rect = self.image.get_rect()
        self.rect.center = starting_position

        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    #update ball position based on velocity
    def update(self):
        self.rect.x = self.rect.x + self.x_velocity;
        self.rect.y = self.rect.y + self.y_velocity;
