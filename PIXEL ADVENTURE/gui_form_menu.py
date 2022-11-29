import pygame
from gui_form import *
from gui_botton import *
from gui_textbox import *
from constantes import *

class FormMenu(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master_surface, x, y, w, h, color_border, active, image_background, color_background)


        self.texto_menu = TextBox(master=self,x=ANCHO_VENTANA/2 - 400/ 2,y=100,w=400,h=150,color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/Menu/Banner06.png",text="MENU",font="Arial",font_size=40,font_color=C_BLACK)

        self.options = Button(master=self,x=ANCHO_VENTANA/2 - 150/ 2,y=400,w=150,h=60,color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/Menu/Buttons/boton_options.png",on_click=self.on_click_boton1,on_click_param="Options",text=None,font="Verdana",font_size=30,font_color=C_WHITE)

        self.levels = Button(master=self,x=ANCHO_VENTANA/2 - 150/ 2,y=500,w=150,h=60,color_background=None,color_border=None,
        image_background="PIXEL ADVENTURE/Recursos/Menu/Buttons/Levels.png",on_click=self.on_click_boton1,on_click_param="levels",text=None,font="Verdana",font_size=30,font_color=C_WHITE)

        self.ranking = Button(master=self,x=ANCHO_VENTANA/2 - 70/ 2,y=600,w=70,h=70,color_background=None,color_border=None,
        image_background="PIXEL ADVENTURE/Recursos/Menu/Buttons/Leaderboard.png",on_click=self.on_click_boton1,on_click_param="ranking",text=None,font="Verdana",font_size=30,font_color=C_WHITE)

        self.lista_widget = [self.options,self.levels,self.ranking,self.texto_menu]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        self.surface.blit(self.image_background,self.image_background_rect)
        for aux_boton in self.lista_widget:    
            aux_boton.draw()
        

    

