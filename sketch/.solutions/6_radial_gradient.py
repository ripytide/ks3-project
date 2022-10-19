from sketch.sketch import Window


def main():
    WIDTH = 500
    HEIGHT = 500

    win = Window(WIDTH, HEIGHT)

    start_colour = [0, 50, 150]
    end_colour = [200, 150, 100]

    red = start_colour[0]
    green = start_colour[1]
    blue = start_colour[2]

    red_increment = (end_colour[0] - start_colour[0]) / 250
    green_increment = (end_colour[1] - start_colour[1]) / 250
    blue_increment = (end_colour[2] - start_colour[2]) / 250

    # background
    win.rectangle(start_colour, [0, 0], WIDTH, HEIGHT)

    # circles

    for i in range(250):
        colour = [red, green, blue]
        win.circle(colour, [250, 250], 250 - i)
        red = red + red_increment
        green = green + green_increment
        blue = blue + blue_increment

    win.display()


if __name__ == "__main__":
    main()
