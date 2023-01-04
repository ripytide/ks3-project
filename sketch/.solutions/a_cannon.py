import math

from sketch.sketch import Animation


def main():
    # First, create the window.
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    win = Animation(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Let's define some colours.
    black = [0, 0, 0]
    dark_grey = [75, 75, 75]
    red = [200, 50, 50]
    white = [255, 255, 255]

    # These are the vertices of the triangle.
    pivot = [150, SCREEN_HEIGHT - 100]
    tri = [[100, SCREEN_HEIGHT],
           pivot,
           [200, SCREEN_HEIGHT]]

    # These are the initial start and end points, and width of the line.
    barrel_back = [100, SCREEN_HEIGHT - 100]
    barrel_front = [300, SCREEN_HEIGHT - 100]
    barrel_width = 100

    # This is the angle of rotation, measured in radians.
    start_angle = 0
    end_angle = math.pi * 0.2

    # Animation loop 1 (raising the cannon).
    n = 4
    for i in range(n):
        # Increment the angle
        angle = start_angle + (end_angle - start_angle) * (i / n)

        # Determine the new position for the front of the barrel.
        front_rad = barrel_front[0] - pivot[0]
        x = pivot[0] + front_rad * math.cos(angle)
        y = pivot[1] - front_rad * math.sin(angle)
        front = [x, y]

        # Determine the new position for the back of the barrel.
        back_rad = pivot[0] - barrel_back[0]
        x = pivot[0] - back_rad * math.cos(angle)
        y = pivot[1] + back_rad * math.sin(angle)
        back = [x, y]

        # Draw the shapes onto the screen.
        win.rectangle(white, [0, 0], SCREEN_WIDTH, SCREEN_HEIGHT)
        win.line(dark_grey, back, front, barrel_width)
        win.circle(dark_grey, back, barrel_width // 2)
        win.triangle(red, tri[0], tri[1], tri[2])
        win.next_frame()

    # Animation loop 2 (lowering the cannon).
    n = 15
    for i in range(n):
        # Increment the angle
        angle = end_angle - (end_angle - start_angle) * (i / n)

        # Determine the new position for the front of the barrel.
        front_rad = barrel_front[0] - pivot[0]
        x = pivot[0] + front_rad * math.cos(angle)
        y = pivot[1] - front_rad * math.sin(angle)
        front = [x, y]

        # Determine the new position for the back of the barrel.
        back_rad = pivot[0] - barrel_back[0]
        x = pivot[0] - back_rad * math.cos(angle)
        y = pivot[1] + back_rad * math.sin(angle)
        back = [x, y]

        # Draw the shapes onto the screen.
        win.rectangle(white, [0, 0], SCREEN_WIDTH, SCREEN_HEIGHT)
        win.line(dark_grey, back, front, barrel_width)
        win.circle(dark_grey, back, barrel_width // 2)
        win.triangle(red, tri[0], tri[1], tri[2])
        win.next_frame()

    # Animation loop 3 (static frames).
    for i in range(50):
        # Draw the shapes onto the screen.
        win.rectangle(white, [0, 0], SCREEN_WIDTH, SCREEN_HEIGHT)
        win.line(dark_grey, barrel_back, barrel_front, barrel_width)
        win.circle(dark_grey, barrel_back, barrel_width // 2)
        win.triangle(red, tri[0], tri[1], tri[2])
        win.next_frame()

    win.display(loop=True)


if __name__ == '__main__':
    main()
