import math
from sketch import Animation

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


def main():
    win = Animation(SCREEN_WIDTH, SCREEN_HEIGHT)

    n = 100
    for i in range(n):
        x = i * math.pi / (0.5 * n)

        y_r = 0.5 * (math.cos(x) + 1)
        y_r = int(y_r * 255)

        y_g = 0.5 * (math.cos(x - 2 * math.pi / 3) + 1)
        y_g = int(y_g * 255)

        y_b = 0.5 * (math.cos(x - 4 * math.pi / 3) + 1)
        y_b = int(y_b * 255)

        colour = [y_r, y_g, y_b]
        win.rectangle(colour, [0, 0], SCREEN_WIDTH, SCREEN_HEIGHT)
        win.next_frame()

    win.display(loop=False)


def graph():
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.arange(0, 2 * np.pi, 0.1)
    w = np.cos(x)
    y = np.cos(x - np.pi * 2 / 3)
    z = np.cos(x - np.pi * 4 / 3)
    plt.plot(x, w, 'r', x, y, 'g', x, z, 'b')
    plt.title('Offset Cosine Curves')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['y = cos(x)', 'y = cos(x - 2π/3)', 'y = cos(x - 4π/3)'])
    plt.show()


if __name__ == '__main__':
    main()
    # graph()
