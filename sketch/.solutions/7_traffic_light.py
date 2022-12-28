from sketch.sketch import Animation


def main():
    # First, create the window.
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    win = Animation(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Colours
    black = [0, 0, 0]
    red_on = [255, 0, 0]
    red_off = [50, 0, 0]
    amber_on = [255, 175, 0]
    amber_off = [50, 50, 0]
    green_on = [0, 255, 0]
    green_off = [0, 50, 0]
    white = [255, 255, 255]

    # Light order
    cycle = [[red_on, amber_off, green_off],
             [red_on, amber_on, green_off],
             [red_off, amber_off, green_on],
             [red_off, amber_on, green_off]]

    # Repeat for each stage in the cycle.
    for red, amber, green in cycle:
        # Wait for 1.5 seconds before moving on.
        for j in range(45):
            # Fill the background.
            win.rectangle(white, [0, 0], SCREEN_WIDTH, SCREEN_HEIGHT)
            # Draw the traffic light box.
            win.rectangle(black, [175, 50], 150, 400)
            # Draw the circle lights.
            win.circle(red, [SCREEN_WIDTH // 2, 150], 50)
            win.circle(amber, [SCREEN_WIDTH // 2, 250], 50)
            win.circle(green, [SCREEN_WIDTH // 2, 350], 50)
            # Move to the next frame.
            win.next_frame()

    win.display(loop=True)


if __name__ == '__main__':
    main()
