import pygame

black = (0, 0, 0)
white = (255, 255, 255)
framerate = 30

pygame.init()
screen = pygame.display.set_mode([500, 500]);

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    #draw game
    screen.fill(black);

    pygame.display.flip();

    #enable framerate
    clock.tick(framerate)
