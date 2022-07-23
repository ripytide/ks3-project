# Session 1

## Graphics


---

## Setting Up

Install PyCharm, Python 3.9 or later and Pygame.

Open up the aliens.py file in PyCharm.


---

## Python Basics

This is a comment. It doesn't do anything when you run your code; it's just a note for us programmers to read.

```python
# Here is a helpful comment.
```

This is a print statement. When it runs, its contents gets output to the console window.

```python
print("Hello World!")
```

![](../images/0_console.png)


---

## Running Code

![](../images/0_pycharm.png)

Order is important - when your code runs, it starts from the top of the file and carries out each instruction one after the other.

![](../images/0_execution_order.png)


---

## Searching

Code files can get pretty long quite quickly. To search for something in your file, use `Cmd+F` (Mac) or `Ctrl+F` (Windows).

![](../images/0_search.png)

Also notice the **line numbers** to the left of your code. These can be handy when looking for a particular line of code in your file.


---

## Handling Errors

Sometimes things don't go the way we expect. If you see an error in the console window after running your code, don't panic. Here are some general tips to fix things:

1. The error message will often say which line of code failed. Find this line to try and locate the problem.
2. A **syntax error** is like a spelling mistake for code. Maybe you forgot a closing bracket `)`, a colon `:`, or a quotation mark `"`?

![](../images/0_errors.png)

*Here I forgot to include a quotation mark at the end of my message. The error message says the problem is in line 5.*

3. If you're really stuck, try copying the error message into Google to search for solutions or ask for help!


---

# Example Game

Time to start making games!

We have an example game that ships with Pygame, called Aliens. Your player is a moon buggy at the bottom of the screen. The alien space ships descend from the top of the screen and drop bombs. If either a bomb or an alien hits you, you die.

![](../images/1_title.png)

* Use the **arrow keys** to move around.
* Press the **spacebar** to fire at the aliens.
* Press the `ESC` key or **red button** to quit the game.


---

## The Window Title

First, find the comment that says *'decorate the game window'*. Beneath this you should see the following line of code:

```python
pygame.display.set_caption("Pygame Aliens")
```

This sets the **window title**.

### Your Turn

Replace `"Pygame Aliens"` with a title for your own game.

![](../images/1_title.png)

Run the code to see the result!


---

## The Window Icon

Now you should find the following code nearby:

```python
icon = pygame.image.load("data/alien1.gif")
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_icon(icon)
```

1. The first line of code loads the image from the *alien1.gif* file in the *data* folder.
2. The second line scales the image to have a size of 32x32.
3. The final line sets the **window icon** for your game in the toolbar.

![](../images/2_icon.png)


---

## Your Turn
At the moment, it loads the image from the *alien1.gif* file. Replace 'alien1.gif' with the filename of your own icon image.

Run the code to see if the icon changed.

### Common Errors

At this point you might get an error. Make sure that the image you're trying to use is in the `data` folder. In the code, your image name needs to include both the folder (`data/`) at the start and the file extension (e.g. `.png, .jpg, .gif`, etc.) at the end.

```python
"data/image_name.png"
```


---

## The Window Size

Right at the top of the file, you should see the *game constants*. These are values that always stay the same during the game (hence the name 'constant').

In particular, `SCREENRECT` is a constant value for the size of the screen.

```python
SCREENRECT = pg.Rect(0, 0, 640, 480)
```

The first two values must be `(0, 0)` for the top left corner. The second two values are the width (640) and the height (480).

![](../images/3_screen_size.png)


---

## Your Turn

Try and change the size of the window to be:
* Small
* Large
* Wide but short
* Tall but narrow

Which is the easiest to play?

![](../images/4_widescreen.png)


---

## Intro to Computer Graphics

So how do computer graphics work?

So far, we've introduced the display, which is the window that displays our game. A window is a rectangular area made up of pixels.

<img src="../images/6_car.png" />

Each pixel is the smallest block of colour that can make up the image.

Originally, the window had a size of 640x480. That means it was 640 pixels wide and 480 pixels tall.


---

## Coordinates

In order to draw images onto the window, we need to know exactly where to place them. To do this, we use coordinates.

The top left pixel of the window is at coordinate (0, 0).

<img src="../images/7_coordinates.png" />


---

## Colours

Each pixel has one single colour. We use RGB values (red green blue) to express colours using numbers. 0 is the minimum and 255 is the maximum.

i.e. Colour(255, 0, 0) has maximum red but minimum green and blue.

![](../images/8_colours.jpg)


---


## Sprites

The objects in a game are called **sprites**. A sprite can be anything including the player, other characters, collectable items, enemies and obstacles.

![](../images/9_sprites.png)

Each type of sprite has a class definition for it. Here is the class definition for *Player* sprites:

```python
class Player(pg.sprite.Sprite):
    ...
```

### Your Turn

Can you spot the sprite classes in the code?

How many sprites are there and what are they called?


---

## Sprite Classes

Although there's a lot of code in these sprite classes, there are only two things every sprite needs:

`self.image` and `self.rect`

The image is obviously the sprite's image that gets displayed on the screen.

The rect is the rectangular area it takes up on the screen.

<img src="../images/10_player.png" />


---

## Sprite Classes

```python
self.image = pygame.image.load("data/player1.gif")
self.image = pygame.transform.scale(self.image, (90, 61))
self.rect = self.image.get_rect()
```

Here we load the image we want from a file, scale it to the desired size (90 x 61px) and then set the rect to fit that image.


---

## Your Turn

Change the image of each sprite in the game. You can use your own images or download images from free-to-use websites like [itch.io](https://itch.io/game-assets/free/tag-2d).

Can you change the entire look and feel of the game by using different images?

*See the next slide for inspiration...*


### How to Remove Backgrounds

You can remove the background from your sprite's image by using the following function. It takes in the RGB colour of the background as a parameter.

```python
self.image.set_colorkey((255, 0, 0))
```

This will make the red colour in the image transparent.


---

![](../images/11_alt_game.png)


