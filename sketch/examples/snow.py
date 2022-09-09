from random import randint
from sketch.sketch import Window


def main():
    blue = (0, 100, 230)
    white = (255, 255, 255)

    win = Window(500, 500)
    win.rectangle(blue, (0, 0), 500, 500)
    for i in range(100):
        x = randint(0, 500)
        y = randint(0, 500)
        r = randint(3, 6)
        win.circle(white, (x, y), r)
    win.display()


if __name__ == "__main__":
    main()
