from sketch import Animation

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
win = Animation(SCREEN_WIDTH, SCREEN_HEIGHT)

# Colours
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED_ON = [255, 0, 0]
RED_OFF = [50, 0, 0]
AMBER_ON = [255, 175, 0]
AMBER_OFF = [50, 50, 0]
GREEN_ON = [0, 255, 0]
GREEN_OFF = [0, 50, 0]

# The light cycle.
cycle = [[RED_ON, AMBER_OFF, GREEN_OFF],
         [RED_ON, AMBER_ON, GREEN_OFF],
         [RED_OFF, AMBER_OFF, GREEN_ON],
         [RED_OFF, AMBER_ON, GREEN_OFF]]


def main():
    # Iterate over each stage in the cycle.
    for i in range(4):
        # Extract the colours for this stage.
        stage = cycle[i]
        red = stage[0]
        amber = stage[1]
        green = stage[2]

        # Clear the window.
        win.rectangle(WHITE, [0, 0], SCREEN_WIDTH, SCREEN_HEIGHT)

        # Draw the black box.
        win.rectangle(BLACK, [175, 50], 150, 400)

        # Draw the lights.
        win.circle(red, [SCREEN_WIDTH // 2, 150], 50)
        win.circle(amber, [SCREEN_WIDTH // 2, 250], 50)
        win.circle(green, [SCREEN_WIDTH // 2, 350], 50)

        # Move on to the next frame.
        win.next_frame()

    # Run the animation.
    win.display(framerate=2)


if __name__ == '__main__':
    main()
