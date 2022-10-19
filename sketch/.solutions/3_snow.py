import random
from sketch.sketch import Window


def main():
    win = Window(500, 500)

    # background
    win.rectangle([50, 50, 250], [0, 0], 500, 500)

    # snowballs
    for i in range(100):
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        r = random.randint(3, 6)
        win.circle([255, 255, 255], [x, y], r)

    win.display()


if __name__ == "__main__":
    main()
