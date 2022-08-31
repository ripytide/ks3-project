from sketch import Window


def main():
    win = Window(500, 500)
    radius = int(input("Enter radius: "))
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    red = int(input("Enter red: "))
    green = int(input("Enter green: "))
    blue = int(input("Enter blue: "))
    win.circle((red, green, blue), (x, y), radius)
    win.display()


if __name__ == "__main__":
    main()
