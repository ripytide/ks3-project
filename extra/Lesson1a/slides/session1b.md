# Session 1: Intro to Making Games

---

## Setup

This code imports the PyGame library and initialises it, ready for us to use:

```python
import pygame
pygame.init()
```

This creates a window that is 500 pixels wide and 500 pixels tall. It saves the window as a variable called `screen`:

```python
screen = pygame.display.set_mode([500, 500])
```

Finally, we have an infinite loop, which keeps the window open for us:

```python
while True:
    pass
```

---

## Task 1

1. Create a new Python file.
2. Add the code on the previous page.
3. Run the code and you should see a square window appear.
4. Play around with the numbers in the `set_mode()` function to create different window sizes. Can you make the window small? Large? Tall? Wide?

If a window doesn't appear, try replacing the infinite loop with the following:

```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```

Don't worry about what it does for now. We'll come back to it another time.

---

## Background Colour

Use the following command to change the background colour of the window:

```python
screen.fill([255,255,255])
```

And then update the display:

```python
pygame.display.flip()
```

Make sure to write this code AFTER you created the screen but BEFORE you start the infinite loop - order is important!

The three numbers represent the RGB value `[red, green, blue]` of the colour. The maximum is 255 (bright) and the minimum is 0 (dark).

---

## Task 2

What colour does each of the following RGB values create?

`[255, 0, 0]`

`[0, 255, 0]`

`[0, 0, 255]`

`[0, 0, 0]`

`[255, 255, 255]`

`[100, 100, 0]`

`[0, 200, 75]`

Can you find out how to make other colours?

---

## Drawing Rectangles

Now we want to draw shapes on the screen.

In PyGame, we can create a rectangle called `my_rect` like this:

```python
my_rect = pygame.rect.Rect((0, 0), (50, 50))
```

The first pair of values is the coordinate of the top left corner. The second pair is the size of the rectangle.

We can then draw the rectangle onto the screen like this:

```python
pygame.draw.rect(screen, [255, 0, 0], my_rect)
```

This draws `my_rect` onto the `screen` and fills it in with a red `(255, 0, 0)` colour.

---

## Task 3

Try and recreate the following images by drawing rectangles onto the screen.

To help figure them out, try using a methodical, step-by-step process. For example:

1. Identify the rectangles that make up the image.
2. For each rectangle, find the coordinate of its top left corner.
3. Find the width and height of the rectangle.
4. Find the colour of the rectangle.

The coordinate of the top left corner is always `(0, 0)`.

![colours1](/images/colours1.png)

![colours2](/images/colours2.png)

![colours3](/images/colours3.png)
