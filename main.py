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

from unit       import *
from weapon     import *
from menu       import *
from barrier    import *
from functions  import *
from wave       import *
from allies     import *




class Main():

    def __init__(self):
        # Modele du jeu
        self.gold   = 1000
        self.health = 200

        # Initialization of the window
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT + HEIGHT_MENU))

        pygame.display.set_caption('Victor Shooter')
        pygame.mouse.set_visible(0)


        # Initialization of the background (part of the creeps)
        self.background = pygame.Surface((WIDTH, HEIGHT))
        self.background = self.background.convert()
        self.background.fill((100, 100, 100))

        self.screen.blit(self.background, (0, HEIGHT_MENU))

        # Barre du menu
        self.menubar = pygame.Surface((WIDTH, HEIGHT_MENU))
        self.menubar = self.menubar.convert()
        self.menubar.fill((101, 67, 33))

        # Sprite groups
        self.barre_menu = pygame.sprite.RenderPlain()
        self.units      = pygame.sprite.RenderPlain()
        self.allies     = pygame.sprite.RenderPlain()
        self.others     = pygame.sprite.RenderPlain()


        # Instanciations of creeps
        self.wave = Wave(self.units)
        '''
        for i in range(3):
            units.add(Faucheur())

        for i in range(5):
            units.add(Mage())
        '''


        # Instanciation of main elements
        self.barrier = Barrier()
        self.others.add(self.barrier)

        self.weapon = SimpleGun()
        self.others.add(self.weapon)

        self.swordman = Swordman(self.units)
        self.allies.add(self.swordman)

        self.gunman = Gunman(self.units)
        self.allies.add(self.gunman)

        #********************
        # Barre de vie
        #********************

        # Barre de vie rouge
        self.HEALTHBAR_HEIGHT = 10
        self.HB_TOPRIGHT      = (int(0.99*WIDTH) , int(0.33 * HEIGHT_MENU))
        self.healthbar = HealthBar(self.health, self.HB_TOPRIGHT, self.HEALTHBAR_HEIGHT)
        self.barre_menu.add(self.healthbar)

        # Barre vide (rectangle blanc) a coller derriere la pleine, permet de voir la barre "se vider"
        self.BV_TOPLEFT = (self.HB_TOPRIGHT[0] - self.health, self.HB_TOPRIGHT[1]) # Barre Vide Topleft
        self.barre_vide = pygame.surface.Surface((self.health, self.HEALTHBAR_HEIGHT))
        self.barre_vide.convert()
        self.barre_vide.fill((255,255,255))


        # Gold counter
        self.goldcounter = GoldCounter(self.gold)
        self.barre_menu.add(self.goldcounter)

        self.screen.blit(self.goldcounter.text, self.goldcounter.textpos)

        # Clock
        self.clock = pygame.time.Clock()


        pygame.display.flip()

        # Ajout d'une musique mais ne boucle pas
        #pygame.mixer.music.load("defcon.mp3")
        #pygame.mixer.music.play()

        self.debut_jeu()



    def weapon_attack_unit(self, unit):
        self.weapon.shoot()
        self.unit_attacked(unit, self.weapon.damage)

    def unit_attacked(self, unit, damage):
        """
            called when a unit is attacked
            decrease health of unit, kill it if necessary
            handle animation of the unit touched
            increase corresponding gold
        """
        unit.touched(damage)
        if unit.dead :
            self.gold += unit.gold
            self.goldcounter.gold = self.gold
            self.others.add(Killed(unit.rect.center))
            unit.kill()
        else:
            self.others.add(Touched(unit.rect.center, unit.speed))

    def debut_jeu(self):
       #*****************************
       # DEBUT DE LA BOUCLE
       #*****************************

        while 1:
            self.clock.tick(FRAME_RATE)

            #*****************************
            # User events
            #*****************************
            for event in pygame.event.get():

                if event.type == QUIT:
                    return

                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    return


                # ADMIN
                #****************
                elif event.type == KEYDOWN and event.key == K_o:
                    self.wave.start_wave = 0
                    print "Force stop wave"

                elif event.type == KEYDOWN and event.key == K_p:
                    self.wave.next_wave()
                    print "Force next wave"
                #****************
                # ADMIN

                elif event.type == MOUSEBUTTONDOWN:
                    for unit in pygame.sprite.spritecollide(self.weapon, self.units, 0):
                        if self.weapon.touch(unit):
                            self.weapon_attack_unit(unit)

            #*****************************
            # Modele du jeu
            #*****************************

            # Les unit a la barriere attaquent
            for unit in self.units:
                if unit.attaque:
                    if self.health > 0:
                        self.health -= unit.damage
                        self.healthbar.health = self.health

            # Gere les attaques des allies
            for ally in self.allies:
                if ally.has_target and ally.target.dead: # Verifie que la target est encore en vie
                    ally.find_new_target()
                elif ally.attaque:
                    self.unit_attacked(ally.target, ally.damage)

            #*****************************
            # Prepare la frame suivante
            #*****************************

            # Update les sprites
            self.barre_menu.update()
            self.units.update()
            self.allies.update()
            self.others.update()

            # Update la wave pour l'ecoulement du temps
            self.wave.update()

            # Recolle les surfaces
            self.screen.blit(self.background, (0, HEIGHT_MENU))
            self.screen.blit(self.menubar, (0,0))
            self.screen.blit(self.barre_vide, self.BV_TOPLEFT)
            self.screen.blit(self.goldcounter.text, self.goldcounter.textpos)


            self.barre_menu.draw(self.screen)
            self.units.draw(self.screen)
            self.others.draw(self.screen)
            self.allies.draw(self.screen)

            pygame.display.flip()




if __name__ == '__main__':
    main = Main()
