from sketch.sketch import Window


def main():
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    INDIGO = (75, 0, 130)
    VIOLET = (148, 0, 211)
    WHITE = (255, 255, 255)
    CENTRE = (250, 500)

    win = Window(500, 500)
    win.circle(RED, CENTRE, 450)
    win.circle(ORANGE, CENTRE, 400)
    win.circle(YELLOW, CENTRE, 350)
    win.circle(GREEN, CENTRE, 300)
    win.circle(BLUE, CENTRE, 250)
    win.circle(INDIGO, CENTRE, 200)
    win.circle(VIOLET, CENTRE, 150)
    win.circle(WHITE, CENTRE, 100)
    win.display()


if __name__ == "__main__":
    main()
