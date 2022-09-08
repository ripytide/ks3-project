from sketch.sketch import Window


def main():
    win = Window(400, 400)
    win.rectangle((100, 250, 100), (0, 0), 400, 400)
    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (50, 50, 200)
    red = (200, 50, 50)
    yellow = (240, 240, 50)
    colours = [white, black, blue, red, yellow]
    centre = (200, 200)
    radius = 200
    for i in range(5):
        win.circle(colours[i], centre, radius - 40 * i)
    win.display()


if __name__ == "__main__":
    main()
