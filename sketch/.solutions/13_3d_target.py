from sketch.sketch import Window

def main():
    win = Window(500, 500)

    # Draw the 3d target
    colours = [[0, 0, 0], [100, 255, 100], [255, 50, 50], [255, 255, 0]]
    for i in range(4):
        ## An ellipse needs to be bounded by a rectangle: (left, top, width, height)
        left = 350 + 15 * i
        top = 100 + 32 * i
        width = 150 - 40 * i
        height = 250 - 71 * i

        # An ellipse gives a 3D perspective to an image
        win.ellipse(colours[i], [left, top, width, height])

    win.display()

if __name__ == "__main__":
    main()
