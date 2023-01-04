from sketch.sketch import Animation


# Duration is measured in seconds.
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
DURATION = 10
YELLOW = [255, 255, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]

# Variables
x = 0


def draw_face(win):
    win.circle(YELLOW, [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], 200)
    win.circle(BLACK, [SCREEN_WIDTH // 2, 350], 60)
    win.line(BLACK, [100, 130], [200, 100], 30)
    win.line(BLACK, [300, 100], [400, 130], 30)


def draw(win, offset):
    global x

    # Fill in the background.
    win.rectangle(WHITE, [0, 0], SCREEN_WIDTH, SCREEN_HEIGHT)

    # Draw the face
    draw_face(win)

    # Draw the eyes
    win.circle(BLACK, [150 + x, 200], 30)
    win.circle(BLACK, [350 + x, 200], 30)

    # Offset x
    x += offset

    # Move onto the next frame.
    win.next_frame()


def main():
    # First, create the window.
    win = Animation(SCREEN_WIDTH, SCREEN_HEIGHT)

    for _ in range(10):
        draw(win, -5)

    for _ in range(30):
        draw(win, 0)

    for _ in range(20):
        draw(win, 5)

    for _ in range(30):
        draw(win, 0)

    for _ in range(10):
        draw(win, -5)

    win.display(loop=True)


if __name__ == '__main__':
    main()
