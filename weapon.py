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


import pygame
from pygame.locals import *


if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

from functions import *
'''
class Weapon(pygame.sprite.Sprite):
    """
        moves a cursor on the screen, following the mouse
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = load_image('viseur.bmp', colorkey=-1)
        self.shooting = 0

    def update(self):
        """ move the cursor based on the mouse position"""
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.shooting:
            self.rect.move_ip(5, 10) # Gere le deplacement du viseur si on tire

    def touch(self, target):
        """ returns true if the fist collides with the target """
        if not self.shooting:
            self.shooting = 1
            hitbox = self.rect.inflate(-5, -5) # Reduit le rect du sprite au moment ou on tire
                                               # pour une meilleure precision
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        """called to pull the cursor back"""
        self.shooting = 0
'''

class Weapon(pygame.sprite.Sprite):
    """
        moves a cursor on the screen, following the mouse
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = load_image('viseur.bmp', colorkey=-1)
        self.shooting = 0
        self.fire_rate = 1 * 60

    def update(self):
        """ move the cursor based on the mouse position"""
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.shooting:
            self.shoot()

    def touch(self, target):
        """ returns true if the fist collides with the target """
        if not self.shooting:
            self.shooting = 1
            hitbox = self.rect.inflate(-5, -5) # Reduit le rect du sprite au moment ou on tire
                                               # pour une meilleure precision
            return hitbox.colliderect(target.rect)
        else:
            return 0

    def shoot(self):
        self.rect.move_ip(5, 10) # Gere le deplacement du viseur si on tire
        self.fire_rate -= 1
        if self.fire_rate == 0:
            self.fire_rate = 1 * 60
            self.unpunch()

    def unpunch(self):
        """called to pull the cursor back"""
        self.shooting = 0



class SimpleGun(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.damage = 10