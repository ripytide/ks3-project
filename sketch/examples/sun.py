from random import randint
from sketch.sketch import Window


def main():
    grey = (100, 100, 100)
    white = (255, 255, 255)

    win = Window(500, 500)

    win.rectangle(grey, (0, 0), 500, 500)

    for i in range(31):
        c = 100 + i * 5
        colour = (c, c, c)
        win.circle(colour, (250, 250), 50 - i)

    win.circle(white, (250, 250), 19)

    win.display()


if __name__ == "__main__":
    main()
