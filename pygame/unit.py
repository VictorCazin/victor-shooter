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
from random import randint

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'



from functions import *


def DPS(damage_per_second):
    """
        compute the damage per frame from the damage per second
    """
    damage_per_frame = damage_per_second / FRAME_RATE
    return damage_per_frame


class Creep(pygame.sprite.Sprite):
    """
       Create a creep
    """
    def __init__(self, position=None):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        #self.image, self.rect = load_image('creep.bmp', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.attaque= 0

        if position is None:
            position_depart = randint(HEIGHT_MENU + self.rect.width, HEIGHT - self.rect.height)
        else:
            position_depart = position

        self.rect.topleft = 0, position_depart - self.rect.width # The creep apparition is randomly distributed

    def update(self):
        if self.attaque:
            pass
        else:
            self._walk()

    def _walk(self):
        "move the creep"
        newpos = self.rect.move((self.speed,0))

        if newpos.right >= BARRIERE:
            newpos = self.rect.move((BARRIERE - self.rect.right, 0))
            self.attaque = 1

        self.rect = newpos




    def touched(self):
        "this will cause the monkey to start spinning"
        print 'touched'





class Killed(pygame.sprite.Sprite):
    """
       Animation when a creep is killed
    """
    def __init__(self, position):

        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.image, self.rect = load_image('explosion.bmp', colorkey=-1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.center = position
        self.compteur = 15


    def update(self):
        "walk or spin, depending on the monkeys state"
        if (self.compteur == 0):
            self.kill()
        else:
            self.compteur = self.compteur - 1



class Faucheur(Creep):
    """
       Create a faucheur
    """
    def __init__(self, position=None):
        self.image, self.rect = load_image('faucheur.bmp', colorkey=-1)
        Creep.__init__(self, position)
        self.health = 50
        self.speed  = 10
        self.damage = DPS(1)

class Mage(Creep):
    """
       Create a mage
    """
    def __init__(self, position=None):
        self.image, self.rect = load_image('mage.bmp', colorkey=-1)
        Creep.__init__(self, position)
        self.health  = 10
        self.speed   = 1
        self.damage  = DPS(3)

