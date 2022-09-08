from sketch.sketch import Window


def main():
    win = Window(400, 400)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    # face
    win.circle(YELLOW, (200, 200), 170)
    # mouth
    win.circle(BLACK, (200, 260), 80)
    win.circle(YELLOW, (200, 280), 80)
    # left eye
    win.circle(WHITE, (130, 150), 40)
    win.circle(BLACK, (130, 150), 20)
    # right eye
    win.circle(WHITE, (260, 150), 40)
    win.circle(BLACK, (260, 150), 20)
    # eyebrows
    win.rectangle(BLACK, (80, 80), 100, 20)
    win.rectangle(BLACK, (210, 80), 100, 20)
    win.display()


if __name__ == "__main__":
    main()
