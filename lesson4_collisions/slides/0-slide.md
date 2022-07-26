# Session 4

## Collisions


---

## Importance of Collisions

A collision is where the rects of two sprites intersect.

This is very important in games where we may need to check if...

* the player is touching an obstacle,
* a projectile hits its target,
* the player collides with a collectible pickup,
* etc.

Today we're going to add collectible power-ups to the game.

![](../../extra/images/powerup.png)


---

## Power Up Sprite

Search for the following code.
This is a new sprite class for powerup sprites.

![](../../extra/images/powerup_class.png)

In the initialisation function, it sets the image and randomly chooses its starting position.

The update function (which gets triggered every frame) moves the collectible up and down.


---

## Sprite Groups

A sprite group is a set of related sprites.
Here we've made a group for all the aliens in the game, all the heads-up display (HUD) text, etc.
The `all` group is used to contain every sprite in the game, so we can render them.

![](../../extra/images/groups.png)

### Your Turn

Can you create a new group for powerups?


---

## Adding Sprites to Groups

We can specify which groups a sprite should belong to by setting their containers:

![](../../extra/images/containers.png)

### Your Turn

Can you set the power up sprite to belong to both the `all` group as well as the new one you just created?


---

## Removing Sprites from Groups

To remove a sprite from the game we use the following command:

```python
<sprite>.kill()
```

This automatically removes it from any groups it was in.

### Your Turn

Find each instance where we trigger the `kill()` function.


---

# Collision Detection

There are a few ways we can detect collisions in Pygame.
If you search through the code, you'll notice a few different approaches.

The first is `groupcollide(group1, group2)`, which checks if any sprite from group2 collided with a sprite from group1.

The second is `spritecollide(sprite, group)`, which checks if the given sprite collided with a member of the given group.

### Your Turn

*Hint: Check out the code when the bomb hits the player for inspiration.*

1. Use the `spritecollide()` function to check if the player collided with a member of your powerup group.
2. If so, use the `kill()` function to remove that powerup from the game, and
3. Use the new `increase_health()` function on the `health` sprite to add to the player's health.

---

## Creating Powerups

### Your Turn

Search for the following code:

![](../../extra/images/create_alien.png)

This code creates a new alien randomly at regular intervals.
Try to use a similar approach to create new powerups.

We've already defined the following variables/constants to help you:

* `powerup_reload`
* `POWERUP_ODDS`
* `POWERUP_RELOAD`

Once done, you should be able to run the game and see collectible powerups appear!

---

## Loops

By now, you will have seen a lot of loops.
A loop is used to repeat the same section of code multiple times. For example...

A `while` loop repeats while the condition is true.
In this case, we repeat the code inside the loop as long as the player is alive:

![](../../extra/images/while_loop.png)

A `for` loop repeats for a set number of times.
In this case, we repeat the code inside the loop for each event that has been triggered:

![](../../extra/images/for_loop.png)

### Your Turn

Can you find other examples of `for` and `while` loops in the code?


---

### WHILE Loops

A while loop is very similar to an if statement.
It checks if a *condition* is true and if so, repeats the *code* inside the loop.

```python
while <condition>:
    <code>
```

Beware! A common pitfall with while loops is that if the condition stays true, the loop will repeat infinitely.
It's important to make sure your condition is possible to be reached.
If you find your code freezes because it's stuck in an infinite loop, you can always press `Ctrl+C` to force it to stop.


---

## Your Turn

Using the Python Console...
1. Ask the user to enter a password.
2. While the password is not equal to "password123",
3. Ask them to retry.
4. Once they enter the correct password, output "correct!".


---

## FOR Loops

We use while loops when we're not sure how many times we'll have to repeat for.
If you do know exactly how many iterations you need, you can use a for loop instead.

So far, we've seen for loops used a lot to iterate over the items in a group.
A more common use you'll have is to repeat a block of code an exact number of times:

```python
for i in range(0, 10):
    print(i)
```

This repeats 10 times.
The variable `i` starts off at 0 and each time it repeats, its value increases by 1.


---

## Your Turn

Using the Python Console...
1. Ask the user to input a number between 1 and 12.
2. Use a for loop to output the times table for that number.

e.g. if the user enters 5, the output should be:

```python
5
10
15
20
25
30
35
40
45
50
55
60
```


---

## Challenges

1. Add another type of collectible powerup to the game. Once collected, it should increase the player's speed.
2. Add a new type of weapon that creates a random number of shots at once. *Hint: check out the rapid fire code, [Python's random module](https://www.w3schools.com/python/module_random.asp) and make sure to use a for loop!*
3. Add another type of alien that drops vertically down from the sky instead of zig-zagging. It should kill anything it touches (including other aliens).