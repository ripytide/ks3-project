from sketch.sketch import Animation


def main():
    # First, create the window.
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    win = Animation(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Let's define some helpful variables.
    black = [0, 0, 0]
    white = [255, 255, 255]
    radius = 10
    x = 0
    y = SCREEN_HEIGHT / 2

    # Use a FOR loop to repeat 10 times.
    for i in range(50):
        # Cover up the screen completely with a white rectangle.
        win.rectangle(white, [0, 0], SCREEN_WIDTH, SCREEN_HEIGHT)
        # Find the new position for the centre of the circle (the y position never changes).
        x = x + 10
        win.circle(black, [x, y], radius)
        # Move onto the next frame of the animation.
        win.next_frame()

    win.display(loop=True, framerate=30)


if __name__ == '__main__':
    main()
