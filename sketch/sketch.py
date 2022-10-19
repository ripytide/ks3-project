import os
import pygame
from pygame.locals import QUIT, KEYDOWN, K_RETURN, K_ESCAPE, K_SPACE
from pygame.rect import Rect
from pygame.surface import Surface


def numeric(parameter: list) -> bool:
    """Returns true if the given parameter contains only numeric values"""
    for value in parameter:
        if type(value) != int and type(value) != float:
            return False
    return True


def validate(parameter: any, expected: int, name: str):
    """Validates the given parameter."""
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


def validate_params(*argv: tuple[any, int, str]):
    """Validates the given parameters."""
    for arg in argv:
        validate(arg[0], arg[1], arg[2])


class Window:
    """Class for drawing shapes onto a screen.

    1. Declare the width and height of the screen.
    2. Call methods such as circle() to draw shapes onto the screen.
    3. Call the display() method to visualise the window.
    """

    def __init__(self, width: int, height: int):
        pygame.init()
        pygame.display.set_caption("Sketch")
        self.screen = pygame.display.set_mode((width, height))
        self.background = Surface((width, height))
        self.background.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))

    def circle(self, colour: (int, int, int), centre: (int, int), radius: int):
        """
        Draws a circle onto the screen.

        Parameters:
            colour (int, int, int): RGB colour values. Each value should be between 0 and 255 inclusive.
            centre (int, int): The (x, y) pixel coordinate of the centre of the circle.
            radius (int): The radius of the circle in pixels.
        """
        validate_params((colour, 3, "colour"), (centre, 2, "centre"), (radius, 1, "radius"))
        pygame.draw.circle(self.screen, colour, centre, radius)

    def rectangle(self, colour: (int, int, int), topleft: (int, int), width: int, height: int):
        """
        Draws a rectangle onto the screen.

        Parameters:
            colour (int, int, int): RGB colour values. Each value should be between 0 and 255 inclusive.
            topleft (int, int): The (x, y) pixel coordinate of the top left corner of the rectangle.
            width (int): The width of the rectangle in pixels.
            height (int): The height of the rectangle in pixels.
        """
        validate_params((colour, 3, "colour"), (topleft, 2, "topleft"), (width, 1, "width"), (height, 1, "height"))
        rect = Rect(topleft, (width, height))
        pygame.draw.rect(self.screen, colour, rect)

    def triangle(self, colour: (int, int, int), point1: (int, int), point2: (int, int), point3: (int, int)):
        """
        Draws a triangle onto the screen.

        Parameters:
            colour (int, int, int): RGB colour values. Each value should be between 0 and 255 inclusive.
            point1 (int, int): The (x, y) pixel coordinate of the first vertex of the triangle.
            point2 (int, int): The (x, y) pixel coordinate of the second vertex of the triangle.
            point3 (int, int): The (x, y) pixel coordinate of the third vertex of the triangle.
        """
        validate_params((colour, 3, "colour"), (point1, 2, "point1"), (point2, 2, "point2"), (point3, 2, "point3"))
        pygame.draw.polygon(self.screen, colour, (point1, point2, point3))

    def line(self, colour: (int, int, int), start: (int, int), end: (int, int), width: int):
        """
        Draws a line onto the screen.

        Parameters:
            colour (int, int, int): RGB colour values. Each value should be between 0 and 255 inclusive.
            start (int, int): The (x, y) pixel coordinate of the start of the line.
            end (int, int): The (x, y) pixel coordinate of the end of the line.
            width (int): The width of the line in pixels.
        """
        validate_params((colour, 3, "colour"), (start, 2, "start"), (end, 2, "end"), (width, 1, "width"))
        pygame.draw.line(self.screen, colour, start, end, width)

    def __save(self):
        """
        Saves a screen capture to a JPEG file.

        Each image will be saved to a file called "imageX.JPEG" where X increments each time.
        The file(s) only get saved after closing the window.
        """
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
        """
        Displays the screen with all shapes drawn on.

        Press the ESCAPE key to close the window.
        Press the RETURN key to save a screenshot.
        """

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


class Animation:
    """
    Class for creating animations. Usage is very similar to the Window class:

    1. Specify the width and height of the window.
    2. Call methods such as circle() to draw shapes on the screen.
    3. Call the next_frame() method to move onto the next frame of animation.
    4. Repeat steps 2-3 for as many frames as you would like in your animation.
    5. Call display() to play the animation.
    """

    def __init__(self, width: int, height: int):
        pygame.init()
        pygame.display.set_caption("Animation")
        self.screen = pygame.display.set_mode((width, height))
        self.background = Surface((width, height))
        self.background.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))

        self.frames = list()
        self.current_frame = list()

    class Circle:
        def __init__(self, colour: (int, int, int), centre: (int, int), radius: int):
            self.colour = colour
            self.centre = centre
            self.radius = radius

    class Rectangle:
        def __init__(self, colour: (int, int, int), topleft: (int, int), width: int, height: int):
            self.colour = colour
            self.rect = Rect(topleft, (width, height))

    class Triangle:
        def __init__(self, colour: (int, int, int), point1: (int, int), point2: (int, int), point3: (int, int)):
            self.colour = colour
            self.points = (point1, point2, point3)

    class Line:
        def __init__(self, colour: (int, int, int), start: (int, int), end: (int, int), width: int):
            self.colour = colour
            self.start = start
            self.end = end
            self.width = width

    def circle(self, colour: (int, int, int), centre: (int, int), radius: int):
        """
        Draws a circle onto the screen.

        Parameters:
            colour (int, int, int): RGB colour values. Each value should be between 0 and 255 inclusive.
            centre (int, int): The (x, y) pixel coordinate of the centre of the circle.
            radius (int): The radius of the circle in pixels.
        """
        validate_params((colour, 3, "colour"), (centre, 2, "centre"), (radius, 1, "radius"))
        command = self.Circle(colour, centre, radius)
        self.current_frame.append(command)

    def rectangle(self, colour: (int, int, int), topleft: (int, int), width: int, height: int):
        """
        Draws a rectangle onto the screen.

        Parameters:
            colour (int, int, int): RGB colour values. Each value should be between 0 and 255 inclusive.
            topleft (int, int): The (x, y) pixel coordinate of the top left corner of the rectangle.
            width (int): The width of the rectangle in pixels.
            height (int): The height of the rectangle in pixels.
        """
        validate_params((colour, 3, "colour"), (topleft, 2, "topleft"), (width, 1, "width"), (height, 1, "height"))
        command = self.Rectangle(colour, topleft, width, height)
        self.current_frame.append(command)

    def triangle(self, colour: (int, int, int), point1: (int, int), point2: (int, int), point3: (int, int)):
        """
        Draws a triangle onto the screen.

        Parameters:
            colour (int, int, int): RGB colour values. Each value should be between 0 and 255 inclusive.
            point1 (int, int): The (x, y) pixel coordinate of the first vertex of the triangle.
            point2 (int, int): The (x, y) pixel coordinate of the second vertex of the triangle.
            point3 (int, int): The (x, y) pixel coordinate of the third vertex of the triangle.
        """
        validate_params((colour, 3, "colour"), (point1, 2, "point1"), (point2, 2, "point2"), (point3, 2, "point3"))
        command = self.Triangle(colour, point1, point2, point3)
        self.current_frame.append(command)

    def line(self, colour: (int, int, int), start: (int, int), end: (int, int), width: int):
        """
        Draws a line onto the screen.

        Parameters:
            colour (int, int, int): RGB colour values. Each value should be between 0 and 255 inclusive.
            start (int, int): The (x, y) pixel coordinate of the start of the line.
            end (int, int): The (x, y) pixel coordinate of the end of the line.
            width (int): The width of the line in pixels.
        """
        validate_params((colour, 3, "colour"), (start, 2, "start"), (end, 2, "end"), (width, 1, "width"))
        command = self.Line(colour, start, end, width)
        self.current_frame.append(command)

    def next_frame(self):
        """Moves onto the next frame of the animation."""
        self.frames.append(self.current_frame)
        self.current_frame = list()

    def display(self, loop=True):
        """
        Displays the window with the animation.

        Press the SPACE BAR to play/pause the animation.
        Press the ESCAPE key to close the window.

        Parameters:
            loop (bool): Loops the animation if set to True, plays once otherwise.
        """
        running = True
        paused = False

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_SPACE:
                        paused = not paused

            if not paused:
                frame = self.frames.pop(0) if len(self.frames) else self.current_frame

                if loop:
                    self.frames.append(frame)
                elif len(self.frames) == 0:
                    running = False

                for command in frame:
                    if type(command) == self.Circle:
                        pygame.draw.circle(self.screen, command.colour, command.centre, command.radius)
                    elif type(command) == self.Rectangle:
                        pygame.draw.rect(self.screen, command.colour, command.rect)
                    elif type(command) == self.Triangle:
                        pygame.draw.polygon(self.screen, command.colour, command.points)
                    else:
                        pygame.draw.line(self.screen, command.colour, command.start, command.end, command.width)

                pygame.display.flip()

        pygame.quit()
