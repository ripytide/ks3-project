from sketch import Window
import random


def main():
    win = Window(400, 400)
    win.rectangle((100, 250, 100), (0, 0), 400, 400)
    win.circle([255, 255, 255], [200, 200], 200)
    win.display()


if __name__ == "__main__":
    main()
