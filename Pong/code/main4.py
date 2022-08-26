import pygame
from paddle import Paddle

black = (0, 0, 0)
white = (255, 255, 255)
framerate = 30

pygame.init()
screen = pygame.display.set_mode([500, 500]);

paddleA = Paddle((10, 200), pygame.K_w, pygame.K_s)
paddleB = Paddle((480, 200), pygame.K_UP, pygame.K_DOWN)

#create sprit group
sprite_group = pygame.sprite.Group()
sprite_group.add(paddleA)
sprite_group.add(paddleB)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    #update game
    sprite_group.update();

    #draw game
    screen.fill(black);

    #draw sprites
    sprite_group.draw(screen)

    pygame.display.flip();

    #enable framerate
    clock.tick(framerate)
