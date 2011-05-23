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
from unit import *




class Wave:
    def __init__(self, units_group):
        self.units = units_group
        self.time = 0

    def release(self, creep):
        """
            Instancie un creep et l'ajoute au groupe de sprite units
        """
        self.units.add(creep())

    def test_time(self, date):
        """
            verifie si self.time est a peu pres egal a date, avec un intervalle de largeur 1/FRAME_RATE
        """
        if (self.time >= date - (1.0 / (2*FRAME_RATE))) and (self.time < date + (1.0 / (2*FRAME_RATE))):
            return True
        else:
            return False

    def update(self):
        self.time = self.time +   1.0 / FRAME_RATE

        if self.test_time(2):
            self.release(Mage)








