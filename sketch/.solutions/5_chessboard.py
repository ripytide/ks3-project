from sketch.sketch import Window


def main():
    square_width = 50
    width = square_width * 8
    win = Window(width, width)

    colours = [[50, 10, 10], [230, 230, 200]]

    for row in range(8):
        for col in range(8):
            x = col * square_width
            y = row * square_width
            i = (row + col) % 2
            win.rectangle(colours[i], [x, y], square_width, square_width)

    win.display()


if __name__ == "__main__":
    main()
