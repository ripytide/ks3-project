"""
Note that this solution isn't necessarily more efficient than the original target solution.
It is more easily adapted to be scalable and teaches the use of arrays and iteration however.
"""

from sketch.sketch import Window


def main():
    win = Window(400, 400)

    # background
    win.rectangle([100, 250, 100], [0, 0], 400, 400)

    # target
    colours = [[255, 255, 255], [0, 0, 0], [50, 50, 200], [200, 50, 50], [240, 240, 50]]
    radius = 200
    for i in range(5):
        win.circle(colours[i], [200, 200], radius)
        radius -= 40

    win.display()


if __name__ == "__main__":
    main()
