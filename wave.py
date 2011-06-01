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


TIME_WAVE = 5

class Wave:
    def __init__(self, units_group):
        self.units  = units_group
        self.number = 0
        self.next_wave()

    def next_wave(self):
        self.number += 1
        fullname = os.path.join('waves', "Wave" + str(self.number) + ".txt")
        self.file = open(fullname, "r")
        self.time = 0

    def release(self, creep, number=1):
        """
            Instancie un creep et l'ajoute au groupe de sprite units
        """
        for i in range(number):
            self.units.add(creep())


    # Autre possibilite, ajouter 1 a self.time toutes les 60 frames, on a une precision que de l'ordre de la sec pour
    # les events mais on s'en fout, et par contre on perd moins de temps de calcul pour test_time a chaque frame
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
        if self.time >= TIME_WAVE:
            print "Fin de la wave numero ", self.number
            self.file.close()
            self.next_wave()




class Wave1(Wave):
    def __init__(self, units_group):
        Wave.__init__(self, units_group)

    def update(self):
        Wave.update(self)
        if self.test_time(1):
            self.release(Mage, 4)
            self.release(Faucheur)
        if self.test_time(4):
            self.release(Faucheur, 5)
        if self.test_time(8):
            self.release(Faucheur, 3)
            self.release(Mage, 6)



