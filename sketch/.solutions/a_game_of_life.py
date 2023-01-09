import random
from sketch.sketch import Animation


# Duration is measured in seconds.
SCREEN_WIDTH = 50
SCREEN_HEIGHT = 50
DURATION = 3
PROBABILITY = 0.07
YELLOW = [255, 255, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]

# Variables
grid = [[1 if random.random() < PROBABILITY else 0 for _ in range(SCREEN_WIDTH)] for _ in range(SCREEN_HEIGHT)]
next_grid = grid.copy()


def neighbours_1(row, col):
    """With wraparound."""
    global grid
    t = row - 1 if row > 0 else SCREEN_HEIGHT - 1
    b = row + 1 if row < SCREEN_HEIGHT - 1 else 0
    l = col - 1 if col > 0 else SCREEN_WIDTH - 1
    r = col + 1 if col < SCREEN_WIDTH - 1 else 0
    return grid[t][l] + grid[t][col] + grid[t][r] + grid[row][l] + grid[row][r] + grid[b][l] + grid[b][col] + grid[b][r]


def neighbours_2(row, col):
    """Without wraparound but counting the current row/col twice if on the edge."""
    global grid
    t = row - 1 if row > 0 else 0
    b = row + 1 if row < SCREEN_HEIGHT - 1 else SCREEN_HEIGHT - 1
    l = col - 1 if col > 0 else 0
    r = col + 1 if col < SCREEN_WIDTH - 1 else SCREEN_WIDTH - 1
    return grid[t][l] + grid[t][col] + grid[t][r] + grid[row][l] + grid[row][r] + grid[b][l] + grid[b][col] + grid[b][r]


def neighbours(row, col):
    """No wraparound or doubling up if on the edge."""
    global grid
    total = 0

    # Check the row above.
    if row > 0:
        if col > 0:
            total += grid[row-1][col-1]
        if col < SCREEN_WIDTH - 1:
            total += grid[row - 1][col + 1]
        total += grid[row - 1][col]

    # Check the row below.
    if row < SCREEN_HEIGHT - 1:
        if col > 0:
            total += grid[row+1][col-1]
        if col < SCREEN_WIDTH - 1:
            total += grid[row+1][col + 1]
        total += grid[row+1][col]

    # Check the current row.
    if col > 0:
        total += grid[row][col - 1]
    if col < SCREEN_WIDTH - 1:
        total += grid[row][col + 1]

    return total


def draw(win):
    global grid

    # Fill in the background.
    win.rectangle(WHITE, [0, 0], SCREEN_WIDTH, SCREEN_HEIGHT)

    # Draw the grid.
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Draw the pixel.
            colour = WHITE if next_grid[row][col] else BLACK
            win.rectangle(colour, [row, col], 1, 1)
            # Calculate how many neighbours this pixel has.
            n = neighbours(row, col)
            # Determine whether the pixel lives or dies in the next round.
            if grid[row][col] == 0 and n == 3:
                next_grid[row][col] = 1
            elif grid[row][col] == 1 and n not in [2, 3]:
                next_grid[row][col] = 0
            else:
                next_grid[row][col] = grid[row][col]

    # Set the grid for the next round.
    grid = next_grid.copy()

    # Move onto the next frame.
    win.next_frame()


def main():
    # First, create the window.
    win = Animation(SCREEN_WIDTH, SCREEN_HEIGHT)

    for _ in range(30 * DURATION):
        draw(win)

    win.display(loop=False)


if __name__ == '__main__':
    main()
