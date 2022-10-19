from sketch.sketch import Animation


def main():
    anim = Animation(500, 500)

    # Initial values
    initial_height = 0
    height = 0
    initial_velocity = 0
    time = 0

    # Constants
    ACCELERATION = 0.1
    DAMPING_FACTOR = 0.8

    # Animation loop
    for _ in range(765):
        # Check if the ball reaches the bottom of the screen.
        if height > 450:
            # Set the initial height to the current height.
            initial_height = height
            # Set the initial velocity to the current velocity, but in the opposite direction.
            # Include damping to reduce the speed due to energy loss on impact.
            initial_velocity = -DAMPING_FACTOR * (initial_velocity + ACCELERATION * time)
            # Reset the time to 1 (a value of 0 will prevent any further motion).
            time = 1

        # Calculate the displacement using a SUVAT equation.
        displacemnt = initial_velocity * time + 0.5 * ACCELERATION * time ** 2
        # Calculate the new height of the ball.
        height = initial_height + displacemnt
        # Increment the time.
        time += 1

        # Fill the screen with a white rectangle.
        anim.rectangle([255, 255, 255], [0, 0], 500, 500)

        # Draw a black circle at the calculated height.
        anim.circle([0, 0, 0], [250, height], 50)

        anim.next_frame()

    anim.display()


if __name__ == "__main__":
    main()
