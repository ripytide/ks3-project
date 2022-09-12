from sketch.sketch import Window
import random


def main():
    win = Window(500, 500)

    # colours
    sky_colour = [40, 150, 250]
    brick_colour = [250, 200, 50]
    brick_colour2 = [200, 150, 0]
    brick_colour3 = [230, 180, 30]
    white = [255, 255, 255]

    # sky
    win.rectangle(sky_colour, (0, 0), 500, 500)
    #
    # # sand
    # win.rectangle(brick_colour3, [0, 430], 500, 70)
    # sand_colour = list(brick_colour3)
    # for i in range(21):
    #     win.line(sand_colour, [0, 430 - i], [500, 430 - i], 1)
    #     sand_colour = [sand_colour[i] + (sky_colour[i] - sand_colour[i]) / 21 for i in range(3)]
    #
    # # pyramid
    # win.triangle(brick_colour, [50, 450], [250, 200], [250, 500])
    # win.triangle(brick_colour2, [250, 200], [250, 500], [450, 450])
    #
    # # sun
    # sun_colour = list(sky_colour)
    # sun_diff = [(white[i] - sun_colour[i]) / 20 for i in range(3)]
    # for i in range(20):
    #     win.circle(sun_colour, [50, 50], 40 - i)
    #     sun_colour = [sun_colour[j] + sun_diff[j] for j in range(3)]
    # win.circle(white, [50, 50], 20)

    # pyramid

    pyramid_colour = [250, 200, 50]
    x = 70
    y = 499
    width = 360
    win.rectangle(pyramid_colour, (x, y), width, 1)
    for i in range(180):
        y = y - 1
        x = x + 1
        width = width - 2
        win.rectangle(pyramid_colour, (x, y), width, 1)

    win.display()


if __name__ == "__main__":
    main()
