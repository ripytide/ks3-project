from sketch.sketch import Window


def main():
    win = Window(400, 400)
    BLACK = (0, 0, 0)
    win.circle(BLACK, (200, 200), 95)
    win.circle(BLACK, (100, 100), 50)
    win.circle(BLACK, (300, 100), 50)
    win.display()


if __name__ == "__main__":
    main()
