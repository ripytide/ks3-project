from sketch.sketch import Window
import random


def main():
    win = Window(500, 500)

    for y in range(500):
        for x in range(500):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            win.rectangle((r, r, r), (x, y), 1, 1)

    win.display()


if __name__ == "__main__":
    main()
