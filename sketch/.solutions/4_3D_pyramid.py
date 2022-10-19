from sketch.sketch import Window


def main():
    win = Window(500, 500)

    # sky
    win.rectangle([50, 50, 250], [0, 0], 500, 500)

    # sun
    win.circle([255, 255, 255], [50, 50], 20)

    # sand
    win.rectangle([230, 180, 30], [0, 430], 500, 70)

    # pyramid
    points = [[50, 450], [250, 250], [250, 500], [450, 450]]
    win.triangle([250, 200, 50], points[0], points[1], points[2])
    win.triangle([200, 150, 0], points[1], points[2], points[3])

    win.display()


if __name__ == "__main__":
    main()
