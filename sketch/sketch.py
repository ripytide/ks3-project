import os

import pygame
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.locals import QUIT, KEYDOWN, K_RETURN, K_ESCAPE


def numeric(parameter: list):
    """Returns true if the given parameter contains only numeric values"""
    for value in parameter:
        if type(value) != int and type(value) != float:
            return False
    return True


def validate(parameter: any, expected: int, name: str):
    """validates the given parameter."""
    if expected == 1:
        if type(parameter) != int:
            raise TypeError(name + " must be an integer")
    else:
        if type(parameter) != list:
            raise TypeError(f"{name} must be an array")
        elif len(parameter) != expected:
            raise TypeError(f"{name} must contain {expected} values")
        elif not numeric(parameter):
            raise TypeError(f"{name} must contain numeric values")


class Window:
    """Class for drawing shapes onto a screen"""

    def __init__(self, width: int, height: int):
        pygame.init()
        pygame.display.set_caption("Sketch")
        self.screen = pygame.display.set_mode((width, height))
        self.background = Surface((width, height))
        self.background.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))

    def circle(self, colour: (int, int, int), centre: (int, int), radius: int):
        """Draws a circle onto the screen."""
        validate(colour, 3, "colour")
        validate(centre, 2, "centre")
        validate(radius, 1, "radius")
        pygame.draw.circle(self.screen, colour, centre, radius)

    def rectangle(self, colour: (int, int, int), topleft: (int, int), width: int, height: int):
        """Draws a rectangle onto the screen."""
        validate(colour, 3, "colour")
        validate(topleft, 2, "topleft")
        validate(width, 1, "width")
        validate(height, 1, "height")
        rect = Rect(topleft, (width, height))
        pygame.draw.rect(self.screen, colour, rect)

    def triangle(self, colour: (int, int, int), point1: (int, int), point2: (int, int), point3: (int, int)):
        """Draws a triangle onto the screen."""
        validate(colour, 3, "colour")
        validate(point1, 2, "point1")
        validate(point2, 2, "point2")
        validate(point3, 2, "point3")
        pygame.draw.polygon(self.screen, colour, (point1, point2, point3))

    def line(self, colour: (int, int, int), start: (int, int), end: (int, int), width: int):
        """Draws a line onto the screen."""
        validate(colour, 3, "colour")
        validate(start, 2, "start")
        validate(end, 2, "end")
        validate(width, 1, "width")
        pygame.draw.line(self.screen, colour, start, end, width)

    def __save(self):
        """Saves a screen capture to a JPEG file."""
        pattern = "image%s.JPEG"

        i = 1
        while os.path.exists(pattern % i):
            i *= 2

        start = i // 2
        end = i
        while start + 1 < end:
            mid = (start + end) // 2
            if os.path.exists(pattern % mid):
                start = mid
            else:
                end = mid

        filename = pattern % end
        pygame.image.save(self.screen, filename)

    def display(self):
        """Displays the screen with all shapes drawn on."""

        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_RETURN:
                        self.__save()
            pygame.display.flip()

        pygame.quit()
