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
from random import randint

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'



from functions import *


class Barrier(pygame.sprite.Sprite):
    """
    Class of the barrier, when ennemies touch it they destroy it progressively
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.image, self.rect = load_image('bar.bmp', reshape=(25, HEIGHT))
        #screen = pygame.display.get_surface()
        screen = pygame.Surface((WIDTH, HEIGHT))
        self.area = screen.get_rect()


        self.rect.bottomleft = BARRIERE, HEIGHT + HEIGHT_MENU # The creep apparition is randomly distributed



    def update(self):
        pass
