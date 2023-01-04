import math
import random
from sketch.sketch import Animation


def main():
    # Constants
    SCREEN_WIDTH = 500
    OFFSETS = [random.random() * 2 * math.pi for _ in range(3)]
    DURATION = 100

    # Animation loop
    anim = Animation(SCREEN_WIDTH, SCREEN_WIDTH)
    for i in range(DURATION):
        t = (i / DURATION) * 2 * math.pi
        colour = [int(0.5 * 255 * (math.sin(t + OFFSETS[i]) + 1)) for i in range(3)]
        anim.rectangle(colour, [0, 0], SCREEN_WIDTH, SCREEN_WIDTH)

        anim.next_frame()

    anim.display(loop=True)


if __name__ == "__main__":
    main()
