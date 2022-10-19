from sketch.sketch import Window


def main():
    win = Window(500, 500)

    # background
    win.rectangle([50, 50, 250], [0, 0], 500, 500)

    # pyramid
    pyramid_colour = [250, 200, 50]
    x = 70
    y = 460
    width = 360
    win.rectangle(pyramid_colour, [x, y], width, 40)
    for i in range(5):
        y = y - 40
        x = x + 30
        width = width - 60
        win.rectangle(pyramid_colour, [x, y], width, 40)

    win.display()


if __name__ == "__main__":
    main()
