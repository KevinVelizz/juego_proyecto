import pygame
from gui_form import *
from gui_botton import *
from gui_textbox import *

class FormTime(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master_surface, x, y, w, h, color_border, active, image_background, color_background)

        self.text_score = 10
        self.score = TextBox(self,10,0,100,100,None,None,None," ")

        self.lista_widget = [self.score]

    def puntos(self,lista_eventos,puntos):
        self.score._text = str(puntos)
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)
        

    def update(self, lista_eventos):

        pass

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()
        

    

