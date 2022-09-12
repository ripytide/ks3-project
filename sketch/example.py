from sketch import Window
import random


def main():
    win = Window(500, 500)
    # win.circle([215, 147, 229], [250, 250], 100)
    # win.rectangle([19, 200, 158], [100, 200], 300, 100)
    # win.triangle([200, 200, 100], [100, 200], [300, 100], [400, 300])
    win.line([255, 0, 0], [100, 100], [400, 400], 10)
    win.display()


if __name__ == "__main__":
    main()
