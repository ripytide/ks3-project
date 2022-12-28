import math
from sketch.sketch import Animation


def main():
    # First, create the window.
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    win = Animation(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Colours
    black = [0, 0, 0]
    brown = [100, 75, 50]
    white = [255, 255, 255]

    # Variables
    centre = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
    l_r = SCREEN_HEIGHT * 0.45
    s_r = SCREEN_HEIGHT * 0.4
    SPEED = 200

    for i in range(SPEED):
        # Update the variables for the long hand.
        l_angle = (i / SPEED) * 2 * math.pi
        l_x = centre[0] + l_r * math.sin(l_angle)
        l_y = centre[1] - l_r * math.cos(l_angle)

        # Update the variables for the short hand.
        s_angle = (12 * (i / SPEED)) * 2 * math.pi
        s_x = centre[0] + s_r * math.sin(s_angle)
        s_y = centre[1] - s_r * math.cos(s_angle)

        # Draw the shapes.
        win.rectangle(brown, [0, 0], SCREEN_WIDTH, SCREEN_HEIGHT)
        win.circle(white, centre, SCREEN_WIDTH // 2)
        win.line(black, centre, [l_x, l_y], 1)
        win.line(black, centre, [s_x, s_y], 1)
        win.next_frame()

    win.display(loop=True)


if __name__ == '__main__':
    main()
