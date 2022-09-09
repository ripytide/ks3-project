from sketch import Window
import random


def main():
    win = Window(500, 500)

    for y in range(50):
        for x in range(50):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            win.rectangle((r, g, b), (10 * x, 10 * y), 10, 10)

    win.display()


if __name__ == "__main__":
    main()
