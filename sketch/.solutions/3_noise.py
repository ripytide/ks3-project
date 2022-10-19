import random
from sketch.sketch import Window


def main():
    win = Window(500, 500)

    for x in range(500):
        for y in range(500):
            r = random.randint(0, 255)
            colour = [r, r, r]
            # Uncomment the following line for a colour image:
            # colour = [random.randint(0, 255) for _ in range(3)]
            win.rectangle(colour, [x, y], 1, 1)

    win.display()


if __name__ == "__main__":
    main()
