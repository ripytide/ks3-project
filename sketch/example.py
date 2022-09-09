from sketch import Window
import random


def main():
    win = Window(500, 500)

    win.rectangle([255, 0, 0], [50, 100], 200, 55)
    win.circle([0, 255, 0], [300, 350], 45)
    win.line([0, 0, 0], [75, 175], [125, 300], 5)
    win.triangle([0, 0, 255], [300, 100], [300, 200], [350, 150])

    win.display()


if __name__ == "__main__":
    main()
