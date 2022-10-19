import math
from sketch.sketch import Animation


def main():
    # Constants
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    MAX_DISPLACEMENT = 150
    BEADS_COUNT = 50
    CLOSENESS = 10
    SPEED = 0.01

    # Variables
    bead_width = SCREEN_WIDTH / BEADS_COUNT

    # Animation loop
    anim = Animation(SCREEN_WIDTH, SCREEN_HEIGHT)
    for t in range(628):
        # Fill the screen with a white rectangle.
        anim.rectangle([255, 255, 255], [0, 0], 500, 500)

        # Draw a line of black beads across the width of the screen.
        for i in range(BEADS_COUNT):
            # Calculate the x coordinate of the bead's centre.
            x = (i + 0.5) * bead_width
            # Calculate the y coordinate of the bead's centre.
            y = (SCREEN_HEIGHT / 2) + math.sin((t + CLOSENESS * i) * SPEED) * MAX_DISPLACEMENT
            # Draw the bead at the given coordinates.
            anim.circle([0, 0, 0], [int(x), int(y)], int(bead_width / 2))

        anim.next_frame()

    anim.display()


if __name__ == "__main__":
    main()
