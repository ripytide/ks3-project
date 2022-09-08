from sketch.sketch import Window


def main():
    width = 50
    win = Window(width * 8, width * 8)
    white = (255, 255, 200)
    black = (60, 20, 20)
    colours = [black, white]
    for i in range(8):
        for j in range(8):
            colour = colours[(i + j) % 2]
            win.rectangle(colour, (j * width, i * width), width, width)
    win.display()


if __name__ == "__main__":
    main()
