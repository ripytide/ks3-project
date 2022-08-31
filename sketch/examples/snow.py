from random import randint
from sketch.sketch import Window


def main():
    LIGHT_BLUE = (0, 100, 230)
    WHITE = (255, 255, 255)

    win = Window(500, 500)
    win.square(LIGHT_BLUE, (250, 250), 500)
    for i in range(100):
        x = randint(0, 500)
        y = randint(0, 500)
        r = randint(3, 6)
        win.circle(WHITE, (x, y), r)
    win.display()


if __name__ == "__main__":
    main()
