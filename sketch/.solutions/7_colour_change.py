import math
import random
from sketch.sketch import Animation


def main():
    # Constants
    SCREEN_WIDTH = 500
    OFFSETS = [random.randint(0, 360) for _ in range(3)]
    SPEED = 0.01

    # Animation loop
    anim = Animation(SCREEN_WIDTH, SCREEN_WIDTH)
    for t in range(int(255 / SPEED)):
        colour = [int(255 * (0.5 * math.sin(SPEED * t + OFFSETS[i]) + 0.5)) for i in range(3)]
        anim.rectangle(colour, [0, 0], SCREEN_WIDTH, SCREEN_WIDTH)

        anim.next_frame()

    anim.display()


if __name__ == "__main__":
    main()
