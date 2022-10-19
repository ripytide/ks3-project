from sketch.sketch import Window


def main():
    win = Window(400, 400)

    # background
    win.rectangle([100, 250, 100], [0, 0], 400, 400)

    # target
    win.circle([255, 255, 255], [200, 200], 200)
    win.circle([0, 0, 0], [200, 200], 160)
    win.circle([50, 50, 200], [200, 200], 120)
    win.circle([200, 50, 50], [200, 200], 80)
    win.circle([240, 240, 50], [200, 200], 40)

    win.display()


if __name__ == "__main__":
    main()
