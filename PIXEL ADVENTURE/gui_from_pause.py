import pygame
from gui_form import *
from gui_botton import *
from gui_textbox import *

class FormPauseLvl(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master_surface, x, y, w, h, color_border, active, image_background, color_background)

        self.txt2 = Widget(master_form=self,x=80,y=-20,w=250,h=150,color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/Menu/Buttons/header.png",text=None,font="Arial",font_size=40,font_color=None)

        self.reanudar = Button(master=self,x=110,y=150,w=150,h=60,color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/Menu/play.png",on_click=self.on_click_boton1,on_click_param="level_uno",text=None,font="Verdana",font_size=30,font_color=C_WHITE)

        self.options = Button(master=self,x=110,y=250,w=150,h=60,color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/Menu/Buttons/boton_menu.png",on_click=self.on_click_boton1,on_click_param="Menu",text=None,font="Verdana",font_size=30,font_color=C_WHITE)

        self.lista_widget = [self.reanudar,self.options,self.txt2]

    def on_click_boton1(self,parametro):
        self.set_active(parametro)
        
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def cambiar_lvl(self,parametro):
        self.reanudar.on_click_param = parametro

    def draw(self): 
        super().draw()
        self.surface.blit(self.image_background,self.image_background_rect)
        for aux_boton in self.lista_widget:    
            aux_boton.draw()


        


    

