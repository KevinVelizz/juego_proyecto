import pygame
from gui_form import *
from gui_botton import *
from gui_textbox import *

class FormRanking(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master_surface, x, y, w, h, color_border, active, image_background, color_background)

        self.text_score = 0

        self.score = TextBox(master=self,x=150,y=0,w=170,h=150,color_background=None,color_border=None,image_background=None,text= "Score",font="Arial",font_size=40,font_color=C_BLACK)

        self.puntos_lvl = TextBox(master=self,x=150,y=50,w=170,h=150,color_background=None,color_border=None,image_background=None,text= self.text_score,font="Arial",font_size=40,font_color=C_BLACK)

        self.atras = Button(master=self,x=0,y=200,w=100,h=80,color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/Menu/Buttons/Back.png",on_click=self.on_click_boton1,on_click_param="Menu",text=None,font="Verdana",font_size=30,font_color=C_WHITE)

        self.lista_widget = [self.puntos_lvl,self.atras,self.score]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
    
    def puntos(self,lista_eventos,puntos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)
        self.puntos_lvl._text = str(puntos)

    def update(self, lista_eventos):
        pass

    def draw(self): 
        super().draw()
        self.surface.blit(self.image_background,self.image_background_rect)
        for aux_boton in self.lista_widget:    
            aux_boton.draw()
        

    

