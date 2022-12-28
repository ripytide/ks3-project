import random
from sketch.sketch import Animation


def main():
    # Constants
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    SPEED = 10
    BALL_RADIUS = 10

    # Initial values
    velocity = [random.random() for _ in range(2)]
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)

    # Animation loop
    anim = Animation(SCREEN_WIDTH, SCREEN_HEIGHT)
    for t in range(300):
        # Fill the screen with a white rectangle.
        anim.rectangle([255, 255, 255], [0, 0], 500, 500)

        # Detect whether the ball has collided with a wall.
        # If so, change its direction.
        if x < BALL_RADIUS:
            velocity[0] = abs(random.random())
        elif x > SCREEN_WIDTH - BALL_RADIUS:
            velocity[0] = -abs(random.random())
        elif y < BALL_RADIUS:
            velocity[1] = abs(random.random())
        elif y > SCREEN_HEIGHT - BALL_RADIUS:
            velocity[1] = -abs(random.random())

        # Calculate the new position of the ball.
        x += velocity[0] * SPEED
        y += velocity[1] * SPEED

        # Draw a black ball at the given coordinates.
        anim.circle([0, 0, 0], [int(x), int(y)], 50)

        anim.next_frame()

    anim.display(loop=True)


if __name__ == "__main__":
    main()
