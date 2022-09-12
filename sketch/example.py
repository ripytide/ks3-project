from sketch import Window
import random


def main():
    win = Window(500, 500)

    size = input("How big is your creature? (small/medium/large): ")
    legs = input("How many legs does your creature have? (enter a positive integer): ")
    eyes = input("How many eyes does your creature have? (enter a positive integer): ")
    print("What is the main colour of your creature?")
    red = input("Enter amount of red (0-255): ")
    green = input("Enter amount of green (0-255): ")
    blue = input("Enter amount of blue (0-255): ")

    win.display()


if __name__ == "__main__":
    main()
