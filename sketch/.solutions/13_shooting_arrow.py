from sketch.sketch import Animation


def main():
    anim = Animation(500, 500)

    # Initial values - try and adjust this value to his the target
    initial_velocity = 10
    time = 0

    # Initial coordinates of the arrow start point
    initial_arrow_x = 10
    initial_arrow_y = 250

    # Coordinates of the arrow start point during animation
    arrow_x = initial_arrow_x
    arrow_y = initial_arrow_y

    # Constants
    ACCELERATION = 0.1

    # Animation loop
    for frame in range(5000):

        # Calculate the displacement along x
        vel_x = initial_velocity * 0.5
        dis_x = time * vel_x

        # Calculate the displacement along y
        vel_y = ACCELERATION * time - initial_velocity * 0.866
        dis_y = time * vel_y

        # Check if the arrow reaches the target
        # Don't animate the earlier or the later frames (just for better visibility)
        if arrow_x > 400 or frame<1000 or frame>3000:
            dis_x = 0
            dis_y = 0
        else:
            time += 0.05

        # Calculate the new position of the arrow
        arrow_x = initial_arrow_x + dis_x
        arrow_y = initial_arrow_y + dis_y

        # Fill the screen with a skyblue rectangle
        anim.rectangle([0, 125, 255], [0, 0], 500, 500)

        # Draw the 3d target always at the same position
        colours = [[0, 0, 0], [100, 255, 100], [255, 50, 50], [255, 255, 0]]
        for i in range(4):
            left = 350 + 15 * i
            top = 100 + 32 * i
            width = 150 - 40 * i
            height = 250 - 71 * i
            anim.ellipse(colours[i], [left, top, width, height])

        # Draw the arrow at the calculated position (challenge: align the arrow) 
        anim.line([50, 50, 50], [arrow_x, arrow_y], [arrow_x+40, arrow_y-30], 5)
        anim.line([50, 50, 50], [arrow_x+30, arrow_y-31], [arrow_x+40, arrow_y-31], 4)
        anim.line([50, 50, 50], [arrow_x+39, arrow_y-21], [arrow_x+39, arrow_y-31], 4)

        # or Draw a projectile ball at the calculated position
        # anim.circle([50, 50, 50], [arrow_x, arrow_y], 8)

        anim.next_frame()

    anim.display(framerate=-1)


if __name__ == "__main__":
    main()
