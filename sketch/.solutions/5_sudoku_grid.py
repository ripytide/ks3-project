from sketch.sketch import Window


def main():
    square_width = 50
    width = square_width * 9
    win = Window(width, width)

    # black background
    win.rectangle([0, 0, 0], [0, 0], width, width)

    # white squares
    for row in range(9):
        for col in range(9):
            x = col * square_width + 1
            y = row * square_width + 1
            win.rectangle([255, 255, 255], [x, y], square_width - 2, square_width - 2)

    win.display()


if __name__ == "__main__":
    main()
