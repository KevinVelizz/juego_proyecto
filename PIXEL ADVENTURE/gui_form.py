import pygame
from pygame.locals import *
from gui_widget import Widget
from constantes import *

class Form:
    forms_dict = {}
    def __init__(self,name,master_surface,x,y,w,h,color_border,active,image_background=None,color_background=None):
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border
        self.image = image_background

        self.surface = pygame.Surface((w,h))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active
        self.x = x
        self.y = y

        if(self.color_background != None):
            self.surface.fill(self.color_background)
        
        if(self.image != None):
            self.image_background = pygame.image.load(PATH_IMAGE + self.image).convert()
            self.image_background = pygame.transform.scale(self.image_background,(self.w,self.h))
            self.image_background_rect = self.image_background.get_rect()

    def set_active(self,name):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True

    def render(self):
        pass

    def update(self,lista_eventos):
        pass

    def draw(self):
        self.master_surface.blit(self.surface,self.slave_rect)
        
