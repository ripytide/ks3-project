from sketch.sketch import Window


def main():
    win = Window(500, 500)

    shape = input("Choose the shape (circle, rectangle, triangle or line): ")

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

    point_name = "top left corner"
    if shape == "circle":
        point_name = "centre"
    elif shape == "triangle" or shape == "line":
        point_name = "first point"

    x = int(input("Enter the x position of the " + point_name + ": "))
    while x < 0 or x > 500:
        x = int(input("Please enter a value between 0 and 500: "))

    y = int(input("Enter the y position of the " + point_name + ": "))
    while y < 0 or y > 500:
        y = int(input("Please enter a value between 0 and 500: "))

    point1 = [x, y]

    if shape == "triangle" or shape == "line":
        x = int(input("Enter the x position of the second point: "))
        while x < 0 or x > 500:
            x = int(input("Please enter a value between 0 and 500: "))

        y = int(input("Enter the y position of the second point: "))
        while y < 0 or y > 500:
            y = int(input("Please enter a value between 0 and 500: "))

    point2 = [x, y]

    if shape == "triangle":
        x = int(input("Enter the x position of the third point: "))
        while x < 0 or x > 500:
            x = int(input("Please enter a value between 0 and 500: "))

        y = int(input("Enter the y position of the third point: "))
        while y < 0 or y > 500:
            y = int(input("Please enter a value between 0 and 500: "))

    point3 = [x, y]

    width = 1

    if shape == "rectangle" or shape == "line" or shape == "circle":
        if shape == "circle":
            width = int(input("Enter the radius: "))
        else:
            width = int(input("Enter the width: "))
        while width < 0:
            width = int(input("Please enter a positive integer: "))

    height = 1

    if shape == "rectangle":
        height = int(input("Enter the height: "))
        while height < 0:
            height = int(input("Please enter a positive integer: "))

    if shape == "circle":
        win.circle(colour, point1, width)
    elif shape == "rectangle":
        win.rectangle(colour, point1, width, height)
    elif shape == "triangle":
        win.triangle(colour, point1, point2, point3)
    elif shape == "line":
        win.line(colour, point1, point2, width)
    else:
        print("Invalid shape")
        quit()

    win.display()


if __name__ == "__main__":
    main()
