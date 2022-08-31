from sketch.sketch import Window


def main():
    win = Window(255, 255)
    for i in range(0, 256):
        colour = (i, i, i)
        topleft = (i, 0)
        win.rectangle(colour, topleft, 1, 255)
    win.display()


if __name__ == "__main__":
    main()
