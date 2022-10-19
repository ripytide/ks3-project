#!/usr/bin/env python
""" pygame.examples.aliens

Controls
--------

* Left and right arrows to move.
* Space bar to shoot
* f key to toggle between fullscreen.

"""

import os
import pygame
import random

from pygame.sprite import *


# game constants
MAX_SHOTS = 2  # most player bullets onscreen
ALIEN_ODDS = 22  # chances a new alien appears
BOMB_ODDS = 60  # chances a new bomb will drop
ALIEN_RELOAD = 12  # frames between new aliens
SCREENRECT = pygame.Rect(0, 0, 640, 480)

# colour constants
BLACK = pygame.color.Color(0, 0, 0)
WHITE = pygame.color.Color(255, 255, 255)

main_dir = os.path.split(os.path.abspath(__file__))[0]


class Player(Sprite):
    """ Representing the player as a moon buggy type car.
    """

    speed = 10
    bounce = 24
    gun_offset = -11
    image = None
    containers = None

    def __init__(self):
        Sprite.__init__(self, self.containers)
        self.image = pygame.transform.scale(self.image, (90, 61))
        self.rect = self.image.get_rect()
        self.rect.midbottom = SCREENRECT.midbottom
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        if direction:
            self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(SCREENRECT)
        self.rect.top = self.origtop - (self.rect.left // self.bounce % 2)

    def gunpos(self):
        pos = self.facing * self.gun_offset + self.rect.centerx
        return [pos, self.rect.top]


class Alien(Sprite):
    """ An alien space ship. That slowly moves down the screen.
    """

    speed = 13
    image = None
    containers = None

    def __init__(self):
        Sprite.__init__(self, self.containers)
        self.image = pygame.transform.scale(self.image, (80, 71))
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1, 1)) * Alien.speed
        if self.facing < 0:
            self.rect.right = SCREENRECT.right

    def update(self):
        self.rect.move_ip(self.facing, 0)
        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(SCREENRECT)


class Explosion(Sprite):
    """ An explosion. Hopefully the Alien and not the player!
    """

    defaultlife = 12
    animcycle = 3
    images = []
    containers = None

    def __init__(self, actor):
        Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = actor.rect.center
        self.life = self.defaultlife

    def update(self):
        """ called every time around the game loop.

        Show the explosion surface for 'defaultlife'.
        Every game tick(update), we decrease the 'life'.

        Also we animate the explosion.
        """
        self.life = self.life - 1
        self.image = self.images[self.life // self.animcycle % 2]
        if self.life <= 0:
            self.kill()


class Shot(Sprite):
    """ a bullet the Player sprite fires.
    """

    speed = -11
    image = None
    containers = None

    def __init__(self, pos):
        Sprite.__init__(self, self.containers)
        self.image = pygame.transform.scale(self.image, (9, 18))
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        """ called every time around the game loop.

        Every tick we move the shot upwards.
        """
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()


class HomingMissile(Sprite):
    image = None
    containers = None

    def __init__(self, pos):
        Sprite.__init__(self, self.containers)
        self.image = pygame.transform.scale(self.image, (9, 18))
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        horizontal = 0
        vertical = -5
        # TODO: control missile here.
        self.rect.move_ip(horizontal, vertical)
        if self.rect.top <= 0:
            self.kill()


class Bomb(Sprite):
    """ A bomb the aliens drop.
    """

    speed = 9
    image = None
    containers = None

    def __init__(self, alien):
        Sprite.__init__(self, self.containers)
        self.image = pygame.transform.scale(self.image, (16, 24))
        self.rect = self.image.get_rect()
        self.rect.midbottom = alien.rect.move(0, 5).midbottom

    def update(self):
        """ called every time around the game loop.

        Every frame we move the sprite 'rect' down.
        When it reaches the bottom we:

        - make an explosion.
        - remove the Bomb.
        """
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= SCREENRECT.bottom - 10:
            Explosion(self)
            self.kill()


class StatsBar(Sprite):
    containers = None

    def __init__(self):
        Sprite.__init__(self, self.containers)
        self.image = pygame.surface.Surface((SCREENRECT.width, 25))
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, BLACK, self.rect)


class Score(Sprite):
    """ to keep track of the score.
    """
    containers = None

    def __init__(self):
        Sprite.__init__(self, self.containers)
        self.font = pygame.font.SysFont("times", 18, bold=False, italic=False)
        self.message = "Score: 0"
        self.image = self.font.render(self.message, False, WHITE)
        self.rect = self.image.get_rect()
        self.rect.move_ip(10, 5)
        self.score = 0

    def increment_score(self):
        self.score += 1
        self.message = "Score: " + str(self.score)
        self.image = self.font.render(self.message, False, WHITE)


class Health(Sprite):
    containers = None

    def __init__(self):
        Sprite.__init__(self, self.containers)
        self.font = pygame.font.SysFont("times", 18, bold=False, italic=False)
        self.message = "Health: 10"
        self.image = self.font.render(self.message, False, WHITE)
        self.rect = self.image.get_rect()
        self.rect.move_ip(SCREENRECT.width - 80, 5)
        self.health = 10

    def reduce_health(self):
        self.health -= 1
        self.message = "Health: " + str(self.health)
        self.image = self.font.render(self.message, False, WHITE)


class WeaponType(Sprite):
    containers = None

    def __init__(self):
        Sprite.__init__(self, self.containers)
        self.font = pygame.font.SysFont("times", 18, bold=False, italic=False)
        self.weapon = "Default"
        self.message = "Weapon: " + self.weapon
        self.image = self.font.render(self.message, False, WHITE)
        self.rect = self.image.get_rect()
        self.rect.move_ip(SCREENRECT.width * 0.4, 5)

    def set_weapon(self, new_weapon):
        self.weapon = new_weapon
        self.message = "Weapon: " + new_weapon
        self.image = self.font.render(self.message, False, WHITE)
    

def main(winstyle=0):
    # Initialise pygame
    if pygame.get_sdl_version()[0] == 2:
        pygame.mixer.pre_init(44100, 32, 2, 1024)
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print("Warning, no sound")
        pygame.mixer = None

    fullscreen = False
    # Set the display mode
    winstyle = 0  # FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    # Load images, assign to sprite classes
    # (do this before the classes are used, after screen setup)
    img = pygame.image.load("data/explosion1.gif")
    Explosion.images = [img, pygame.transform.flip(img, 1, 1)]

    # decorate the game window
    pygame.display.set_caption("Pygame Aliens")
    icon = pygame.image.load("data/alien1.gif")
    icon = pygame.transform.scale(icon, (32, 32))
    pygame.display.set_icon(icon)
    pygame.mouse.set_visible(0)

    # create the background, tile the bgd image
    bgdtile = pygame.image.load("data/background.gif")
    bgdtile = pygame.transform.scale(bgdtile, (bgdtile.get_width(), SCREENRECT.height))
    background = pygame.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # load the sound effects
    boom_sound = pygame.mixer.Sound("data/boom.wav")
    shoot_sound = pygame.mixer.Sound("data/car_door.wav")
    if pygame.mixer:
        music = os.path.join(main_dir, "data", "house_lo.wav")
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)

    # Initialize Game Groups
    aliens = Group()
    shots = Group()
    bombs = Group()
    all = RenderUpdates()
    hud = Group()
    lastalien = GroupSingle()

    # assign default groups to each sprite class
    Player.containers = all
    Alien.containers = aliens, all, lastalien
    Shot.containers = shots, all
    Bomb.containers = bombs, all
    Explosion.containers = all
    StatsBar.containers = hud
    Score.containers = hud
    Health.containers = hud
    WeaponType.containers = hud
    HomingMissile.containers = shots, all

    # Assign default images to each sprite class.
    Player.image = pygame.image.load("data/player1.gif")
    Alien.image = pygame.image.load("data/alien1.gif")
    Shot.image = pygame.image.load("data/shot.gif")
    Bomb.image = pygame.image.load("data/bomb.gif")
    HomingMissile.image = pygame.image.load("data/shot.gif")

    # Create Some Starting Values.
    alienreload = ALIEN_RELOAD
    clock = pygame.time.Clock()

    # Initialize our starting sprites.
    player = Player()
    Alien()
    StatsBar()
    score = Score()
    health = Health()
    weapon_type = WeaponType()

    paused = False

    # Run our main loop whilst the player is alive.
    while player.alive():

        # Get input.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        keystate = pygame.key.get_pressed()

        if not paused:

            # Clear/erase the last drawn sprites.
            all.clear(screen, background)
            hud.clear(screen, background)

            # Update all the sprites.
            all.update()
            hud.update()

            # Handle player input.
            direction = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
            player.move(direction)
            firing = keystate[pygame.K_SPACE]
            if not player.reloading and firing and len(shots) < MAX_SHOTS:
                Shot(player.gunpos())
                if pygame.mixer:
                    shoot_sound.play()
            player.reloading = firing

            # Create new alien
            if alienreload:
                alienreload = alienreload - 1
            elif not int(random.random() * ALIEN_ODDS):
                Alien()
                alienreload = ALIEN_RELOAD

            # Drop bombs
            if lastalien and not int(random.random() * BOMB_ODDS):
                Bomb(lastalien.sprite)

            # Detect collisions between aliens and players.
            for alien in spritecollide(player, aliens, 1):
                if pygame.mixer:
                    boom_sound.play()
                Explosion(alien)
                Explosion(player)
                health.reduce_health()

            # See if shots hit the aliens.
            for alien in groupcollide(shots, aliens, 1, 1).keys():
                if pygame.mixer:
                    boom_sound.play()
                Explosion(alien)
                score.increment_score()

            # See if alien bombs hit the player.
            for bomb in spritecollide(player, bombs, 1):
                if pygame.mixer:
                    boom_sound.play()
                Explosion(player)
                Explosion(bomb)
                health.reduce_health()

            # See if the player has run out of health.
            if health.health == 0:
                player.kill()

            # draw the scene
            all.draw(screen)
            hud.draw(screen)
            pygame.display.update()

            # cap the framerate at 40fps. Also called 40HZ or 40 times per second.
            clock.tick(40)

    if pygame.mixer:
        pygame.mixer.music.fadeout(1000)
    pygame.time.wait(1000)
    pygame.quit()


# call the "main" function if running this script
if __name__ == "__main__":
    main()
