from sketch.sketch import Window


def main():
    win = Window(400, 400)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (50, 100, 200)
    # background
    win.rectangle(BLUE, (0, 0), 400, 400)
    # snow balls
    win.circle(WHITE, (200, 320), 80)
    win.circle(WHITE, (200, 200), 50)
    win.circle(WHITE, (200, 125), 30)
    # hat
    win.rectangle(BLACK, (160, 95), 80, 5)
    win.rectangle(BLACK, (175, 55), 50, 40)
    win.display()


if __name__ == "__main__":
    main()
