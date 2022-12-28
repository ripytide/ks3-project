import random
from sketch.sketch import Animation


# Duration is measured in seconds.
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
N_BALLS = 50
DURATION = 5
DARK_BLUE = [20, 10, 50]
WHITE = [255, 255, 255]


def random_snowball():
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)
    r = random.randint(3, 6)
    return [x, y, r]


def replacement_snowball():
    x = random.randint(0, SCREEN_WIDTH)
    r = random.randint(3, 6)
    y = -r
    return [x, y, r]


def main():
    # First, create the window.
    win = Animation(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Create a list of randomly generated snow balls.
    snow_balls = [random_snowball() for _ in range(N_BALLS)]

    # Create a waiting list of balls to remove.
    remove_list = []

    for _ in range(30 * DURATION):
        # Fill in the background.
        win.rectangle(DARK_BLUE, [0, 0], SCREEN_WIDTH, SCREEN_HEIGHT)
        # Handle the snow balls.
        for i in range(len(snow_balls)):
            x, y, r = snow_balls[i]
            # Draw the snow ball.
            win.circle(WHITE, [x, y], r)
            # Move it down for the next round, amount depends on its radius (bigger = faster).
            snow_balls[i][1] += r
            # Flag if this snow ball has reached the bottom of the screen.
            if y - r >= SCREEN_HEIGHT:
                remove_list.append(i)
        # Replace snow balls that reached the bottom of the screen.
        remove_list.reverse()
        for i in remove_list:
            snow_balls.pop(i)
        for _ in range(len(remove_list)):
            snow_balls.append(replacement_snowball())
        remove_list = []

        # Move onto the next frame.
        win.next_frame()

    win.display(loop=True)


if __name__ == '__main__':
    main()
