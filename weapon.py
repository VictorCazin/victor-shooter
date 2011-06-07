#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Victor
#
# Created:     17/05/2011
# Copyright:   (c) Victor 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from __future__ import division

import pygame
from pygame.locals import *


if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

from functions import *

from random import randint


class Weapon(pygame.sprite.Sprite):
    """
        moves a cursor on the screen, following the mouse
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = load_image('viseur.bmp', colorkey=-1)
        self.shooting = 0
        self.RELOAD_FIRE_RATE = self.fire_rate


    def update(self):
        """ move the cursor based on the mouse position"""

        if self.shooting:
            self.reload()
        else:
            pos = pygame.mouse.get_pos()
            self.rect.midtop = pos

    def touch(self, target):
        """ returns true if the fist collides with the target """
        if self.shooting:
            return 0
        else:
            hitbox = self.rect.inflate(-5, -5) # Reduit le rect du sprite au moment ou on tire
                                               # pour une meilleure precision
            return hitbox.colliderect(target.rect)


    def shoot(self):
        self.shooting = 1
        self.sound.play()


    def reload(self):
        direction = randint(0,3)
        if direction == 0:
            movement = [0,5]
        elif direction == 1:
            movement = [0,-5]
        elif direction == 2:
            movement = [5,0]
        elif direction == 3:
            movement = [-5, 0]

        # Bring the cursor a little closer to the mouse position
        pos = pygame.mouse.get_pos()
        movement[0] = movement[0] + int((pos[0] - self.rect.centerx) /10)
        movement[1] = movement[1] + int((pos[1] - self.rect.centery) /10)


        newpos = self.rect.move(movement)
        self.rect = newpos

        self.fire_rate -= 1
        if self.fire_rate == 0:
            self.unpunch()

    def unpunch(self):
        """called to pull the cursor back"""
        self.fire_rate = self.RELOAD_FIRE_RATE
        self.shooting = 0



class SimpleGun(Weapon):
    def __init__(self):
        self.fire_rate = 1 * 60
        Weapon.__init__(self)
        self.damage = 10
        self.sound = load_sound("gunshot.ogg")
