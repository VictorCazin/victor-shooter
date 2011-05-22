import os, sys
import pygame
from pygame.locals import *


if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

from functions import *


HB_TOPRIGHT = int(0.99*WIDTH) , int(0.33 * HEIGHT_MENU)
GC_TOPLEFT  = int(0.10*WIDTH) , int(0.25 * HEIGHT_MENU)


class HealthBar(pygame.sprite.Sprite):
    """
        Show how much health the main base has left
    """
    def __init__(self, health):
        pygame.sprite.Sprite.__init__(self)
        self.health = health
		#self._image = spritesheet.get_image(Rect((448, 0), (128, 64)))
        self.image = pygame.surface.Surface((self.health, 10))
    	#self.rect = Rect((320 - 64, 0), (128, 64))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.topright = HB_TOPRIGHT


    def update(self):
        "called when health decrease or increase"
        self.image  = pygame.transform.scale(self.image, (int(self.health), 10))
        self.rect = self.image.get_rect()
        self.rect.topright = HB_TOPRIGHT


class GoldCounter(pygame.sprite.Sprite):
    """
        Show how much gold the player has
    """

    def __init__(self, gold):
        self.font_size = 15
        pygame.sprite.Sprite.__init__(self)
        self.gold = gold
        self.image, self.rect = load_image('gold.bmp', colorkey=-1, reshape= (20,20))
        self.rect.topleft = GC_TOPLEFT


        self.font = pygame.font.Font(None, self.font_size)
        self.text = self.font.render(str(self.gold), 0, (255, 255, 255))
        self.textpos = self.text.get_rect()
        self.textpos.center= ( self.rect.centerx + 1.5 * self.rect.width,
                               self.rect.centery)



    def update(self):
        "called when the player earn or spend gold"
        self.font = pygame.font.Font(None, self.font_size)
        self.text = self.font.render(str(self.gold), 0, (255, 255, 255))
        self.textpos = self.text.get_rect()
        self.textpos.center= ( self.rect.centerx + 1.5 * self.rect.width,
                               self.rect.centery)

    def draw(self, surface):
        print 'test'
        #pygame.sprite.Sprite.draw(self, surface)
        surface_blit = self.surface.blit
        self.surface_blit(self.text, self.textpos)