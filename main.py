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




def main():
    # Modele du jeu
    gold   = 1000
    health = 200

    # Initialization of the window
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT + HEIGHT_MENU))

    pygame.display.set_caption('Victor Shooter')
    pygame.mouse.set_visible(0)


    # Initialization of the background (part of the creeps)
    background = pygame.Surface((WIDTH, HEIGHT))
    background = background.convert()
    background.fill((100, 100, 100))

    screen.blit(background, (0, HEIGHT_MENU))

    # Barre du menu
    menubar = pygame.Surface((WIDTH, HEIGHT_MENU))
    menubar = menubar.convert()
    menubar.fill((101, 67, 33))

    # Sprite groups
    barre_menu = pygame.sprite.RenderPlain()
    units      = pygame.sprite.RenderPlain()
    others     = pygame.sprite.RenderPlain()


    # Instanciations of creeps
    wave = Wave1(units)
    '''
    for i in range(3):
        units.add(Faucheur())

    for i in range(5):
        units.add(Mage())
    '''


    # Instanciation of main elements
    barrier = Barrier()
    others.add(barrier)

    weapon = SimpleGun()
    others.add(weapon)


    #********************
    # Barre de vie
    #********************

    # Barre de vie rouge
    HEALTHBAR_HEIGHT = 10
    HB_TOPRIGHT      = (int(0.99*WIDTH) , int(0.33 * HEIGHT_MENU))
    healthbar = HealthBar(health, HB_TOPRIGHT, HEALTHBAR_HEIGHT)
    barre_menu.add(healthbar)

    # Barre vide (rectangle blanc) a coller derriere la pleine, permet de voir la barre "se vider"
    BV_TOPLEFT = (HB_TOPRIGHT[0] - health, HB_TOPRIGHT[1]) # Barre Vide Topleft
    barre_vide = pygame.surface.Surface((health, HEALTHBAR_HEIGHT))
    barre_vide.convert()
    barre_vide.fill((255,255,255))


    # Gold counter
    goldcounter = GoldCounter(gold)
    barre_menu.add(goldcounter)

    screen.blit(goldcounter.text, goldcounter.textpos)

    # Clock
    clock = pygame.time.Clock()


    pygame.display.flip()



   #*****************************
   # DEBUT DE LA BOUCLE
   #*****************************

    while 1:
        clock.tick(FRAME_RATE)

        #*****************************
        # User events
        #*****************************
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                for unit in pygame.sprite.spritecollide(weapon, units, 0):
                    if weapon.touch(unit):
                        unit.touched(weapon.damage)
                        if (unit.health <= 0):
                            gold = gold + unit.gold
                            goldcounter.gold = gold
                            others.add(Killed(unit.rect.center))
                            unit.kill()
                        else:
                            others.add(Touched(unit.rect.center, unit.speed))

            elif event.type == MOUSEBUTTONUP:
                weapon.unpunch()


        #*****************************
        # Modele du jeu
        #*****************************
        for unit in units:
            if unit.attaque:
                if health > 0:
                    health = health - unit.damage
                    healthbar.health = health



        #*****************************
        # Prepare la frame suivante
        #*****************************

        # Update les sprites
        barre_menu.update()
        units.update()
        others.update()

        # Update la wave pour l'ecoulement du temps
        wave.update()

        # Recolle les surfaces
        screen.blit(background, (0, HEIGHT_MENU))
        screen.blit(menubar, (0,0))
        screen.blit(barre_vide, BV_TOPLEFT)
        screen.blit(goldcounter.text, goldcounter.textpos)


        barre_menu.draw(screen)
        units.draw(screen)
        others.draw(screen)

        pygame.display.flip()




if __name__ == '__main__':
    main()