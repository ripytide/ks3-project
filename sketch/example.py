from sketch import Window
import random


def main():
    win = Window(500, 500)
    for y in range(500):
        for x in range(500):
            i = random.randint(0, 255)
            win.rectangle([i, i, i], [x, y], 1, 1)
    win.display()


if __name__ == "__main__":
    main()
