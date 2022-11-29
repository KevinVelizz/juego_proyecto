import pygame
from gui_form import *
from gui_botton import *
from gui_textbox import *
from progressbar import *

class FormLevels(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master_surface, x, y, w, h, color_border, active, image_background, color_background)

        self.level1 = Button(master=self,x=375,y=45,w=70,h=70,color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/Menu/Levels/01.png",on_click=self.iniciar_level,on_click_param="level_uno",text=None,font="Verdana",font_size=30,font_color=C_WHITE)

        self.level2 = Button(master=self,x=750,y=45,w=70,h=70,color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/Menu/Levels/02.png",on_click=self.iniciar_level,on_click_param="level_dos",text=None,font="Verdana",font_size=30,font_color=C_WHITE)

        self.level3 = Button(master=self,x=1125,y=45,w=70,h=70,color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/Menu/Levels/03.png",on_click=self.iniciar_level,on_click_param="level_tres",text=None,font="Verdana",font_size=30,font_color=C_WHITE)

        self.volver_menu = Button(master=self,x=10,y=700,w=100,h=80,color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/Menu/Buttons/Back.png",on_click=self.iniciar_level,on_click_param="Menu",text=None,font="Verdana",font_size=30,font_color=C_WHITE)

        self.txt1 = TextBox(master=self,x=330,y=20,w=170,h=150,color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/Menu/Buttons/imagen_levels.png",text=None,font="Arial",font_size=40,font_color=C_BLACK)

        self.txt2 = TextBox(master=self,x=705,y=20,w=170,h=150,color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/fondo/fondolvl2.png",text=None,font="Arial",font_size=40,font_color=C_BLACK)

        self.txt3 = TextBox(master=self,x=1080,y=20,w=170,h=150,color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/fondo/fondolvl3.png",text=None,font="Arial",font_size=40,font_color=C_BLACK)

        self.lista_widget = [self.txt1,self.txt2,self.txt3,self.level1,self.level2,self.level3,self.volver_menu]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
    
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def iniciar_level(self,parametro):
        self.on_click_boton1(parametro)
        self.forms_dict["pause"].cambiar_lvl(parametro)

    def draw(self): 
        super().draw()
        self.surface.blit(self.image_background,self.image_background_rect)
        for aux_boton in self.lista_widget:    
            aux_boton.draw()
        

    

