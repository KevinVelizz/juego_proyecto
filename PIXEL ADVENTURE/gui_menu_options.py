import pygame
from gui_form import *
from gui_botton import *
from gui_textbox import *
from progressbar import *

class FormOptions(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master_surface, x, y, w, h, color_border, active, image_background, color_background)

        self.back = Button(master=self,x=10,y=700,w=100,h=80,color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/Menu/Buttons/Back.png",on_click=self.on_click_boton1,on_click_param="Menu",text=None,font="Verdana",font_size=30,font_color=C_WHITE)

        #volumen
        self.subir = Button(master=self,x=890,y=250,w=50,h=50,color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/Menu/Buttons/Next.png",on_click=self.on_click_boton2,on_click_param="Options",text=None,font="Verdana",font_size=30,font_color=C_WHITE)
        self.bajar = Button(master=self,x=600,y=250,w=50,h=50,color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/Menu/Buttons/Previous.png",on_click=self.on_click_boton3,on_click_param="Options",text=None,font="Verdana",font_size=30,font_color=C_WHITE)

        self.pb1 = ProgressBar(master=self,x=650,y=250,w=240,h=50,color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/Other/Shadow.png",image_progress="PIXEL ADVENTURE/Recursos/Other/Confetti (16x16).png",value = 3, value_max=8)

        self.text_sound = TextBox(master=self,x=650,y=190,w=240,h=50,color_background=None,color_border=None,image_background=None,text="SOUND",font="Arial",font_size=40,font_color=C_BLACK)

        self.lista_widget = [self.back,self.subir,self.bajar,self.pb1,self.text_sound]

    def on_click_boton2(self, parametro):
        self.pb1.value += 1

    def on_click_boton3(self, parametro):
        self.pb1.value -= 1

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
        

    

