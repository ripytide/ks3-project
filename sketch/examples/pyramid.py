from sketch.sketch import Window
import random


def main():
    win = Window(500, 500)
    # background
    win.rectangle((40, 150, 250), (0, 0), 500, 500)

    # sun
    r = 40
    g = 150
    b = 250
    for i in range(10):
        r_new = round(r + (255 - r) * i / 10)
        g_new = round(g + (255 - g) * i / 10)
        b_new = round(b + (255 - b) * i / 10)
        win.circle((r_new, g_new, b_new), (50, 50), 30 - i)
    win.circle((255, 255, 255), (50, 50), 20)

    # pyramid
    brick = (250, 200, 50)
    grunge = (200, 150, 10)
    for i in range(6):
        width = 360 - i * 60
        x = 250 - 0.5 * width
        y = 460 - i * 40
        win.rectangle(brick, (x, y), width, 40)

        # grunge
        for j in range(6 - i):
            w = random.randint(7, 10)
            h = random.randint(3, 4)
            xg = random.randint(x, x + width - 10)
            yg = random.randint(y, y + 36)
            win.rectangle(grunge, (xg, yg), w, h)
    win.display()


if __name__ == "__main__":
    main()
