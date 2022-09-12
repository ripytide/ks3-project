from sketch.sketch import Window


def main():
    win = Window(256, 256)
    for i in range(0, 256):
        colour = (i, i, i)
        topleft = (i, 0)
        win.rectangle(colour, topleft, 1, 256)
    win.display()


if __name__ == "__main__":
    main()
