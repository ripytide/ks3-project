from sketch import Window
import random


def main():
    square_width = 50
    width = square_width * 9
    height = square_width * 9
    win = Window(width, height)

    win.rectangle([0, 0, 0], [0, 0], width, height)

    for row in range(0, 9):
        for col in range(0, 9):
            x = col * square_width + 1
            y = row * square_width + 1
            win.rectangle([255, 255, 255], [x, y], square_width - 2, square_width - 2)
    win.display()


if __name__ == "__main__":
    main()
