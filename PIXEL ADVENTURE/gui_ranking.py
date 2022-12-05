import pygame
from gui_form import *
from gui_botton import *
from gui_textbox import *
import sqlite3 as sql
from controller import *

class FormRanking(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master_surface, x, y, w, h, color_border, active, image_background, color_background)

        self.data_player = readRows2(name)
        self.name = name

        self.name_player = Widget(master_form=self,x=60,y=110,w=160,h=70,color_background=None,color_border=None,image_background=None,text= self.data_player[0][1],font="Arial",font_size=40,font_color=C_BLACK)

        self.name_player2 = Widget(master_form=self,x=60,y=180,w=160,h=70,color_background=None,color_border=None,image_background=None,text= self.data_player[1][1],font="Arial",font_size=40,font_color=C_BLACK)

        self.name_player3 = Widget(master_form=self,x=60,y=250,w=160,h=70,color_background=None,color_border=None,image_background=None,text= self.data_player[2][1],font="Arial",font_size=40,font_color=C_BLACK)

        self.puntos_player = Widget(master_form=self,x=240,y=110,w=70,h=70,color_background=None,color_border=None,image_background=None,text= self.data_player[0][2],font="Arial",font_size=40,font_color=C_BLACK)

        self.puntos_player2 = Widget(master_form=self,x=240,y=180,w=70,h=70,color_background=None,color_border=None,image_background=None,text= self.data_player[1][2],font="Arial",font_size=40,font_color=C_BLACK)
    
        self.puntos_player3 = Widget(master_form=self,x=240,y=250,w=70,h=70,color_background=None,color_border=None,image_background=None,text= self.data_player[2][2],font="Arial",font_size=40,font_color=C_BLACK)

        self.score = Widget(master_form=self,x=150,y=20,w=100,h=150,color_background=None,color_border=None,image_background=None,text= "Score",font="Arial",font_size=40,font_color=C_BLACK)
    
        self.atras = Button(master=self,x=0,y=500,w=100,h=80,color_background=None,color_border=None,image_background="PIXEL ADVENTURE/Recursos/Menu/Buttons/Back.png",on_click=self.on_click_boton1,on_click_param="ranking",text=None,font="Verdana",font_size=30,font_color=C_WHITE)

        self.lista_widget = [self.atras,self.score,self.name_player,self.name_player2,self.name_player3,self.puntos_player,self.puntos_player2,self.puntos_player3]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
    
    def update(self,lista_eventos):
        
        self.data_player = readRows2(self.name)
    
        self.name_player._text = self.data_player[0][1]
        self.puntos_player._text = self.data_player[0][2]
    
        self.name_player2._text = self.data_player[1][1]
        self.puntos_player2._text = self.data_player[1][2]
    
        self.name_player3._text = self.data_player[2][1]
        self.puntos_player3._text = self.data_player[2][2]

        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        self.surface.blit(self.image_background,self.image_background_rect)
        for aux_boton in self.lista_widget:    
            aux_boton.draw()
        


    

