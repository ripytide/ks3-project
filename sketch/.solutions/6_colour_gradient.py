from sketch.sketch import Window


def main():
    WIDTH = 500
    HEIGHT = 500

    win = Window(WIDTH, HEIGHT)

    start_colour = [100, 150, 200]
    end_colour = [200, 150, 100]

    red = start_colour[0]
    green = start_colour[1]
    blue = start_colour[2]

    red_increment = (end_colour[0] - start_colour[0]) / WIDTH
    green_increment = (end_colour[1] - start_colour[1]) / WIDTH
    blue_increment = (end_colour[2] - start_colour[2]) / WIDTH

    for i in range(500):
        colour = [red, green, blue]
        win.line(colour, [i, 0], [i, HEIGHT - 1], 1)
        red = red + red_increment
        green = green + green_increment
        blue = blue + blue_increment

    win.display()


if __name__ == "__main__":
    main()
