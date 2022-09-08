from sketch.sketch import Window


def main():
    win = Window(400, 400)
    white = (255, 255, 255)
    red = (200, 50, 50)
    blue = (20, 20, 100)
    centre = (200, 200)
    win.circle(red, centre, 150)
    win.circle(white, centre, 100)
    win.rectangle(blue, (10, 180), 380, 60)
    win.display()


if __name__ == "__main__":
    main()
