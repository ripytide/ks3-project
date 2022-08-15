# Session 6

## Sound


---

## Loading Sounds

Search for the following code:

```python
# Load the sound effects.
boom_sound = pygame.mixer.Sound("data/boom.wav")
shoot_sound = pygame.mixer.Sound("data/car_door.wav")
if pygame.mixer:
    pygame.mixer.music.load("data/house_lo.wav")
    pygame.mixer.music.play(loops=-1)
```

This demonstrates how to load sound effects and music to the game.
Here we load two sounds and store them in variables called `boom_sound` and `shoot_sound`.
We also load a music file called "house_lo.wav".

### Your Turn

1. Find alternative sounds and music*.
2. Make sure to move them to the `data/` folder.
3. Replace the sounds and music in the code above with your own.
4. Run the game to hear your new sounds play throughout the game.

\* When looking for music and sound effects online, search for results that are copyright free (you're allowed to download and use) and royalty free (you don't have to pay money for).


---

## Playing Sounds

Once we've loaded sounds and music into the game, we can use the `play()` function to play them.

```python
pygame.mixer.music.play(loops=-1)
```

For music, you can specify the number of times you want the music to loop (repeat) for.
0 is the default and -1 causes it to loop infinitely.

### Your Turn

Can you find all the places where we trigger our sound effects to play?

<details>
    <summary>Hint</summary>

Search for `.play()`.
</details>


---

## Your Turn

Over the last few sessions we've added new features to the game.
It's time to give them their own sound effects!

1. Load totally new sound effects to the game.
2. Trigger them at the appropriate moments using the `play()` function.

Make sure to do this for all the new types of weapons, aliens and collectibles you've added to the game.


---

## Challenges

1. Add a new feature where the user can press a button whose only purpose is to play a sound of your choice.
