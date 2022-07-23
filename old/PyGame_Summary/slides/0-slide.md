# Pygame Tutorial

---

## Screen Setup 1

This initialises Pygame:

```python
pygame.init()
```


This sets the **window title**. Replace 'Title Here' with your own title.

```python
pygame.display.set_caption('Title Here')
```


This sets the **window icon**. Replace 'icon_filename.png' with the filename of your own icon image.

```python
icon = pygame.image.load('icon_filename.png')
pygame.display.set_icon(icon)
```

![image1](/images/image1.png)


---

## Screen Setup 2

This sets the **window size**. Use different values to change the width and height of the window.

```python
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
```


This sets the **background image** for the window. Replace 'background_filename.png' with the filename of your background image.

```python
background = pygame.image.load('background_filename.png')
```

![image2](/images/image3.png)

![image3](/images/image5.png)


---

## Game Objects (Sprites)

A **sprite** is an object in the game. It could be anything from a character to an obstacle, a collectable item or a projectile. Any object you see in the game is a sprite.

To have sprites in our game, there are two steps:
1. Define the blueprint for that class of sprite.
2. Create an actual sprite from that blueprint.

![image4](/images/image6.png)

![image5](/images/image7.png)


---

# Sprite Classes

A **sprite class** is the blueprint for our sprite. For example:

```python
class Player(Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('player_filename.png').convert()
        self.rect = self.image.get_rect()
```

* `Player` is the name of the sprite.

* `self.image` contains the sprite's image.

* `self.rect` defines the rectangle of space that the sprite takes up on the screen.


---

# Sprite Groups

A **sprite group** contains a set of sprites. We can use them to group together similar sprites (enemies, collectables, etc.). 

Here, we define a new group to contain all the sprites in the game:

```python
all_sprites = Group()
```

Now we can create a new player sprite and add it to the group:

```python
my_player = Player()
all_sprites.add(my_player)
```


---

## Game Loop

The **game loop** is a `WHILE` loop, which repeatedly runs the code inside it 30 times every second (30 fps).

```python
running = True
while running:
    # Add code here to handle EVENTS.

    # Add code here to check for COLLISIONS.

    # Add code here to RENDER the screen.
```


---

## Events

We can use **events** to check for user input while the game is running. 

* We use a `FOR` loop to go through all the events that have been triggered.

* We use `IF` and `ELIF` statements to check the type of the event.

```python
for event in pygame.event.get():
    if event.type == QUIT:
        running = False

    elif event.type == KEYDOWN:
        print('The user pressed a key!')
    
    elif event.type == MOUSEBUTTONDOWN:
        print('The user pressed a mouse button!')
```

Some other events you can check for include:
* `KEYUP`
* `MOUSEBUTTONUP`


---

## KEYDOWN EVENTS

Once we know which event has been triggered, we can use more `IF-ELIF` statements to check which specific key or button was pressed:

```python
for event in pygame.event.get():
    ...
    
    elif event.type == KEYDOWN:
        if event.key == K_UP:
            print('Up arrow key pressed.')

        elif event.key == K_DOWN:
            print('Down arrow key pressed.')
        
        elif event.key == K_LEFT:
            print('Left arrow key pressed.')
        
        elif event.key == K_RIGHT:
            print('Right arrow key pressed.')

    ...
```

You can find the full list of key codes here:
https://www.pygame.org/docs/ref/key.html


---

## Sprite Movement 1

Remember, each sprite has a `rect`, which tells Pygame about the sprite's rectangle location on-screen. To move the sprite, we need to change the `rect`. There are a few ways to do this...

The 'move in-place' function translates the sprite's position.

```python
my_player.rect.move_ip(5, 2)
```

This tells pygame to move the sprite 5 pixels to the right and 2 pixels down.


---

## Sprite Movement 2

Another way to move sprites is to tell Pygame exactly which pixel on the screen we want to place them at.

This moves the sprite so that its topleft corner is at coordinate (50,100):

```python
my_player.rect.topleft = (50, 100)
```

This moves the sprite so that its centre is at coordinate (40,20):

```python
my_player.rect.center = (40, 20)
```

Here are some other options for setting position:

`bottomleft, topright, bottomright, midtop, midleft, midbottom, midright`


---

## Collisions

Sprite `rect`s are also great if we want to check if two sprites have collided with each other. This can be used if you want to check if...

* Your player has touched a collectable item,

* A projectile has hit your player,

* Your player has bumped into an obstacle,

* etc.

Here we are checking if our player has collided with another sprite called `player2`:

```python
if my_player.rect.colliderect(player2.rect):
    print('my_player collided with player2!')
```


---

## Rendering

Finally, after we've made all the changes, we need to update the display. This part is called rendering and involves the following steps:

1. Fill the screen with the background image.

2. Go through each sprite in the `all_sprites` group.

3. Draw the sprite's **image** onto the screen at the position given by its **rect**.

4. Update the screen.

```python
screen.blit(background, (0, 0))
for sprite in all_sprites:
    screen.blit(sprite.image, sprite.rect)
screen.flip()
```

* `blit` pastes an image onto the screen.

* `flip` updates the screen.


---

## Music

To add music to the game, first load the music file:

```python
music.load('my_song.mp3')
```

Then start the music, use the following function. If you want it to keep looping without stopping, include `–1` in the parentheses.

```python
music.play()
```

To force the music to stop, use:

```python
music.stop()
```


---

## Sound Effects

To add a sound effect, first load it into the game:

```python
my_sound = Sound('sound_filename.mp3')
```

Then use the play function each time you want it to start:

```python
my_sound.play()
```

And the stop function to stop it from playing:

```python
my_sound.stop()
```
