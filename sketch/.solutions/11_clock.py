import math
from sketch import Animation

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
BROWN = [100, 75, 50]
CENTRE = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
HOUR_LENGTH = SCREEN_HEIGHT * 0.45
MINUTE_LENGTH = SCREEN_HEIGHT * 0.4


def main():
    win = Animation(SCREEN_WIDTH, SCREEN_HEIGHT)

    for i in range(360):
        # Find the end of the hour hand.
        angle = i * math.pi / 180
        opp = HOUR_LENGTH * math.sin(angle)
        adj = HOUR_LENGTH * math.cos(angle)
        x = CENTRE[0] + opp
        y = CENTRE[1] - adj

        # Draw the clock.
        win.rectangle(BROWN, [0, 0], SCREEN_WIDTH, SCREEN_HEIGHT)
        win.circle(WHITE, CENTRE, SCREEN_WIDTH // 2)
        win.line(BLACK, CENTRE, [x, y], 1)

        # Find the end of the minute hand.
        angle = 12 * i * math.pi / 180
        opp = MINUTE_LENGTH * math.sin(angle)
        adj = MINUTE_LENGTH * math.cos(angle)
        x = CENTRE[0] + opp
        y = CENTRE[1] - adj

        # Draw the minute hand.
        win.line(BLACK, CENTRE, [x, y], 1)

        # Move onto the next frame.
        win.next_frame()

    win.display(loop=True)


if __name__ == '__main__':
    main()
