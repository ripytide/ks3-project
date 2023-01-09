import random
from sketch import Animation

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
WHITE = [255, 255, 255]
DARK_BLUE = [20, 10, 50]


def main():
    win = Animation(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Generate 50 snow balls randomly.
    snow_balls = []
    for _ in range(50):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        r = random.randint(3, 6)
        snow_ball = [x, y, r]
        snow_balls.append(snow_ball)

    # Create 100 frames of animation.
    for _ in range(100):
        win.rectangle(DARK_BLUE, [0, 0], SCREEN_WIDTH, SCREEN_HEIGHT)
        for i in range(len(snow_balls)):
            x = snow_balls[i][0]
            y = snow_balls[i][1]
            r = snow_balls[i][2]
            win.circle(WHITE, [x, y], r)
            snow_balls[i][1] += r
            if snow_balls[i][1] + 5 > 500:
                snow_balls[i][1] = -r
        win.next_frame()

    win.display(loop=False)


if __name__ == '__main__':
    main()
