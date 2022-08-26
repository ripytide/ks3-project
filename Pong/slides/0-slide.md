# Pong

![main0](/images/main0.png)

---
# Part 1: Initialisation
This code initialises pygame and quits if we try to close the window.

It also makes sure the framerate stays the same.

```python
import pygame

black = (0, 0, 0)
white = (255, 255, 255)
framerate = 30

pygame.init()
screen = pygame.display.set_mode([500, 500]);

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    #draw game
    screen.fill(black);

    pygame.display.flip();

    #enable framerate
    clock.tick(framerate)
```

Write out and then run this code in a file named "main.py"

---
## Expected Output
If you wrote everything out correctly the window should look like this when you run the code.

![main6](/images/main6.png)

---

# Part 2: Paddles
Next we are going to start making the sprites needed for our game. We will
start with the paddles.

Create a new file called "paddle.py" and write out the following code.

```python
import pygame

white = (255, 255, 255)
width = 10
height = 60

class Paddle(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(white)

        self.rect = self.image.get_rect()
        self.rect.center = position
```

This code shows a new sprite class called "Paddle" it takes a position as a parameter
and then draws a rectangle at the given position.

We have given the rectangle a width of 10 and a height of 60 pixels.

Now we have created a paddle sprite we can add them to our game.

First Import the class into our "main.py" file by placing this line at the top:
```python
from paddle import Paddle
```

Then before the game loop, initialise two paddles and add them to a sprite group.

```python
paddleA = Paddle((10, 200))
paddleB = Paddle((480, 200))

#create sprit group
sprite_group = pygame.sprite.Group()
sprite_group.add(paddleA)
sprite_group.add(paddleB)
```

Finally, inside the game loop just after filling the screen with black but before flipping it,
add the folling line of code to draw the sprite group on the screen.

```python
    #draw sprites
    sprite_group.draw(screen)
```

---

## Expected Output

![main5](/images/main5.png)

---

# Part 3: Making the paddles move

Now we have paddles we need to be able to move the paddles up and down using our
keyboard.

Firstly, change the code in the "paddle.py" file so it looks like this:
```python
import pygame

white = (255, 255, 255)
width = 10
height = 60

class Paddle(pygame.sprite.Sprite):
    def __init__(self, position, up_key, down_key):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(white)

        self.rect = self.image.get_rect()
        self.rect.center = position

        self.up_key = up_key
        self.down_key = down_key

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.up_key]:
            self.rect.y = self.rect.y - 4
        if keys[self.down_key]:
            self.rect.y = self.rect.y + 4
```

We changed a few things here, we changed the __init__ function to take two more parameters:
```up_key``` and ```down_key```.


Then we create a new function in the class called ```update```.
Within ```update``` we get a list of the currently pressed keys on the keyboard via

```python
keys = pygame.key.get_pressed()
```

If the ```up_key``` is pressed we subtract 4 pixel from the rectangles y coordinate and if the ```down_key``` is pressed then
we add 4 pixels.

Before we can see the new paddles in action we need to adjust our code in "main.py" to add the two
new parameters we just added to our Paddle class.

Change the Paddle Initialisations to this:
```python
paddleA = Paddle((10, 200), pygame.K_w, pygame.K_s)
paddleB = Paddle((480, 200), pygame.K_UP, pygame.K_DOWN)
```

This code tells ```paddleA``` that it's ```up_key``` is the "w" key, and it's ```down_key``` is the "s" key.
And it tells ```paddleB``` that it's ```up_key``` is the up arrow key and it's ```down_key``` is the down arrow key.

---

## Expected Output

If you wrote all that code out correctly then you should see the following when you run "main.py".
You should be able to move the paddles up and down now using the "w", "s" and arrow keys.

![main4](/images/main4.png)

---

# Part 4: The Ball

Now we have paddles the next sprite we need is the ball.

Create another new file called "ball.py" and add the following code:

```python
import pygame

white = (255, 255, 255)
starting_position = [250, 250]
width = 10
height = 10

class Ball(pygame.sprite.Sprite):
    def __init__(self, x_velocity, y_velocity):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(white)

        self.rect = self.image.get_rect()
        self.rect.center = starting_position

        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    #update ball position based on velocity
    def update(self):
        self.rect.x = self.rect.x + self.x_velocity;
        self.rect.y = self.rect.y + self.y_velocity;
```

Similar to the Paddle sprite we draw a rectangle, but this time with a width of 10 and a height of 10.

We also take two parameters: ```x_velocity``` and ```y_velocity```. The velocity parameters will tell us the initial velocity of the ball. (Speed and direction)

Finally, just like the paddles we have an ```update``` function but this time we update the position
of the ball not based on what keys are being pressed but on the current velocities of the ball.

If the ball has a higher velocity then it moves faster if it has a smaller velocity then the ball
should move slower.

```python
from ball.py import Ball
```
Just like when we added the paddles we first need to import the ball class so add this line
to the top of the "main.py" file.

```python
ball = Ball(3, 1)
```

Then next to the Initialisations of the paddles add this line to initialise the ball in the middle
of the screen.

This line gives the ball a starting ```x_velocity``` of 3 units and a ```y_velocity``` of 1 unit.

```python
sprite_group.add(ball)
```
Add this line next to where we added the two paddles to the ```sprite_group``` so the ball gets drawn too.

---

## Expected Output

Now we have ball sprite, notice however that the ball will not bounce when it hits
either the edge of the screen or the paddle. That is what we shall fix in the next part.

![main3](/images/main3.png)

---

# Part 5: Making the ball bounce off the walls

Inside the game loop in "main.py" just after the line:

```python
sprite_group.update()
```
Add this code:
```python
#update ball
#bouncing off the top, bottom, left and right
if ball.rect.centery < 0:
	ball.y_velocity = -ball.y_velocity

if ball.rect.centery > 500:
	ball.y_velocity = -ball.y_velocity

if ball.rect.centerx < 0:
	ball.x_velocity = - ball.x_velocity

if ball.rect.centerx > 500:
	ball.x_velocity = - ball.x_velocity
```

This code check if the coordinates of the ball mean it has hit any of the four
edges of the game. If it has hit the top or the bottom then it reverses the sign of
the balls ```y_velocity``` for example if the ball had a ```y_velocity = -4``` and it hit
the top then it's ```y_velocity``` would become 4 and it would start moving downwards.
The same thing is done for the left and right edges with ```x_velocity```.

---

## Expected Output

You should not see the ball bouncing off the 4 edges of the screen, but not off of
the paddles, that is what we shall add next.

![main2](/images/main2.png)

---

# Part 6: Making the ball bounce off of the paddles

All we need now is for the ball to also bounce off of the paddles.

Add this code just after the if statements we added in the previous part.
```python
#bouncing off the paddles
if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
	ball.x_velocity = - ball.x_velocity
```

This code checks for either a collision of ```ball``` with ```paddleA``` "or" a collistion of ```ball``` with ```paddleB```.
"if" either of those two things are true then we reverse the balls ```x_velocity``` by negating it.

---

## Expected Output

Now the ball should also bounce off of the paddles instead of phasing through them.

![main1](/images/main1.png)

---

# Part 7: Scoring (Final Part)

To be written..


---

# Extensions

- Can you give the ball a random starting velocity?

- Can you make the ball speed up each time it hits a paddle?

- Can you make the game quit when a player reaches a score of 5?

- (Hard) Can you make the game display a "Game Over" message when a player reaches a score of 5?
