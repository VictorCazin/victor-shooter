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

from functions import *



class Ally(pygame.sprite.Sprite):
    """
       Create a creep
    """
    def __init__(self, unit_group):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        #self.image, self.rect = load_image('creep.bmp', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.units = unit_group

        self.attaque    = 0
        self.has_target = 0
        self.time_before_next_hit =  1

    def update(self):
        if self.has_target:
            if self.attaque:
                self.attaque = 0
            else:
                self._aim()
        else:
            self.find_new_target()

    def find_new_target(self):
        if self.time_before_next_hit > 1:
            self.time_before_next_hit -= 1
        self.has_target = 0


class Swordman(Ally):
    """
       Create a swordman
    """
    def __init__(self, unit_group):
        self.image, self.rect = load_image('swordman.bmp', colorkey=-1)
        Ally.__init__(self, unit_group)
        self.rect.midleft = BARRIERE, int((HEIGHT_MENU + HEIGHT)/2)

        self.speed   = 3
        self.damage  = 10
        self.cadence = 2 * FRAME_RATE

        self.can_attack = 0



    def _aim(self):
        if not self.can_attack:
            if self.time_before_next_hit > 1:
                self.time_before_next_hit -= 1
            if self.has_target:
                self._walk()
            else:
                self.find_new_target()
        else:
            self.time_before_next_hit -=1
            if self.time_before_next_hit == 0:
                self.time_before_next_hit = self.cadence
                self.attaque = 1


    def _walk(self):
        """
            move the swordman
        """
        if self.target.rect.centery == self.rect.centery:
            self.can_attack = 1
        else:
            if abs(self.target.rect.centery - self.rect.centery) <= self.speed:
                self.rect.centery = self.target.rect.centery
            else:
                if self.target.rect.centery > self.rect.centery:
                    signe = 1
                elif self.target.rect.centery < self.rect.centery:
                    signe = -1
                newpos = self.rect.move((0,signe*self.speed))
                self.rect = newpos

    def find_new_target(self):
        Ally.find_new_target(self)
        self.can_attack = 0
        distance = 2*HEIGHT
        for unit in self.units:
                    if unit.attaque: # On suppose pour l'instant que toutes les unites sont a la barriere lorsqu'elles attaquent
                        new_distance = abs(unit.rect.centery - self.rect.centery)
                        if new_distance < distance:
                            distance = new_distance
                            self.target = unit
                            self.has_target = 1

class Gunman(Ally):
    """
       Create a gunman
    """
    def __init__(self, unit_group):
        self.image, self.rect = load_image('gunman.bmp', colorkey=-1)
        Ally.__init__(self, unit_group)
        self.rect.midleft = BARRIERE + 40, int((HEIGHT_MENU + HEIGHT)/3)

        self.speed   = 3
        self.damage  = 10
        self.cadence = 2 * FRAME_RATE

    def _aim(self):
        """
            called when the gunman has a target and gets ready to shoot
        """
        self.time_before_next_hit -=1
        if self.time_before_next_hit == 0:
            self.time_before_next_hit = self.cadence
            self.attaque = 1


    def find_new_target(self):
        Ally.find_new_target(self)
        for unit in self.units:
            self.target = unit
            self.has_target = 1

