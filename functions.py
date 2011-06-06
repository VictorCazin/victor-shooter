##
## Contient des variables et fonctions utiles a tous les modules
##

from __future__ import division

import os, sys
import pygame
from pygame.locals import *



FRAME_RATE   = 60

WIDTH        = 1300
HEIGHT       = 500
HEIGHT_MENU  = 30
BARRIERE     = 800

HEALTH = 200

def load_image(name, colorkey=None, reshape=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if reshape is not None:
            image = pygame.transform.scale(image, reshape)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', wav
        raise SystemExit, message
    return sound


def DPS(damage_per_second):
    """
        compute the damage per frame from the damage per second
    """
    damage_per_frame = damage_per_second / FRAME_RATE
    return damage_per_frame

