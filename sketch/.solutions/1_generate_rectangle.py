from sketch.sketch import Window


def main():
    win = Window(500, 500)

    red = int(input("Enter the amount of red: "))
    while red < 0 or red > 255:
        red = int(input("Please enter a value between 0 and 255: "))

    green = int(input("Enter the amount of green: "))
    while green < 0 or green > 255:
        green = int(input("Please enter a value between 0 and 255: "))

    blue = int(input("Enter the amount of blue: "))
    while blue < 0 or blue > 255:
        blue = int(input("Please enter a value between 0 and 255: "))

    colour = [red, green, blue]

    x = int(input("Enter the x position of the top left corner: "))
    while x < 0 or x > 500:
        x = int(input("Please enter a value between 0 and 500: "))

    y = int(input("Enter the y position of the top left corner: "))
    while y < 0 or y > 500:
        y = int(input("Please enter a value between 0 and 500: "))

    top_left = [x, y]

    width = int(input("Enter the width: "))
    while width < 0:
        width = int(input("Please enter a positive integer: "))

    height = int(input("Enter the height: "))
    while height < 0:
        height = int(input("Please enter a positive integer: "))

    win.rectangle(colour, top_left, width, height)
    win.display()


if __name__ == "__main__":
    main()
