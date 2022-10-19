from sketch.sketch import Window


def main():
    win = Window(256, 256)

    for i in range(256):
        colour = [i, i, i]
        win.line(colour, [i, 0], [i, 256], 1)

    win.display()


if __name__ == "__main__":
    main()
