import pygame
from gui_form import *
from pygame.locals import *
import sys
from constantes import *
from player import *
from plataforma import *
from score import *
from gui_barravida import *
from gui_textbox import *
from info_levels import *

class LevelDos(Form):
    def __init__(self, name, master_form, x, y, w, h, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master_form, x, y, w, h, color_border, active, image_background, color_background)

        self.master_form = master_form
        self.lista_info = Datalevels(master_form,"level_two")
        self.imagen_fondo = pygame.image.load(PATH_IMAGE + self.lista_info.lista_data ["background"]).convert()
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
        self.player_dos = PlayerDos(100,500,10,10,50,10,15,10,master_form)
        self.barra_vida = BarraVida(self,x=10,y=10,w=500,h=50,color_background=C_BLACK,color_border=C_BLUE,image_background=None,image_progress=None,value = self.player_dos.hp, value_max=self.player_dos.hp,color_vida=C_WHITE)
        self.lista_plataformas = self.lista_info.lista_platform
        self.contador_puntos = 0
        self.acumulador_time = 0
        self.win_lvl2 = self.lista_info.win
        self.time_juego = 60
        self.time = Widget(self,600,0,200,50,None,None,"PIXEL ADVENTURE/Recursos/Menu/Buttons/fondo_botones.png",self.time_juego,"Arial",30,C_BLACK)
        self.score = Widget(self,1300,0,200,50,None,None,"PIXEL ADVENTURE/Recursos/Menu/Buttons/fondo_botones.png",self.lista_info.puntos,"Arial",30,C_BLACK)
        self.win = Widget(self,ANCHO_VENTANA / 2 - 450/2,150,500,300,None,None,"PIXEL ADVENTURE/Recursos/Menu/Buttons/you win.png",None,"Arial",30,C_BLACK)
        self.lose = Widget(self,ANCHO_VENTANA / 2 - 450/2,170,500,300,None,None,"PIXEL ADVENTURE/Recursos/Menu/Buttons/you lose.png",None,"Arial",30,C_BLACK)
        self.lista_widget = [self.time,self.score]
        
        self.lista_enemigos = self.lista_info.lista_enemy

        self.tick_1s = pygame.USEREVENT+0
        pygame.time.set_timer(self.tick_1s,1000)
       
        self.fruits = self.lista_info.list_fruits


    def draw(self):
        super().draw()
        self.surface.fill((0,0,0))
        self.surface.blit(self.imagen_fondo,(0,0))
    
    def resetear(self):
        self.lista_info = Datalevels(self.master_form,"level_two")
        self.imagen_fondo = pygame.image.load(PATH_IMAGE + self.lista_info.lista_data ["background"]).convert()
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
        self.player_dos = PlayerDos(100,500,10,10,50,10,15,10,self.master_form)
        self.barra_vida = BarraVida(self,x=10,y=10,w=500,h=50,color_background=C_BLACK,color_border=C_BLUE,image_background=None,image_progress=None,value = self.player_dos.hp, value_max=self.player_dos.hp,color_vida=C_WHITE)
        self.lista_plataformas = self.lista_info.lista_platform
        self.lista_enemigos = self.lista_info.lista_enemy
        self.time_juego = 60
        self.acumulador_time = 0
        self.time = Widget(self,600,0,200,50,None,None,"PIXEL ADVENTURE/Recursos/Menu/Buttons/fondo_botones.png",self.time_juego,"Arial",30,C_BLACK)
        self.score = Widget(self,1300,0,200,50,None,None,"PIXEL ADVENTURE/Recursos/Menu/Buttons/fondo_botones.png",self.lista_info.puntos,"Arial",30,C_BLACK)
        self.win = Widget(self,ANCHO_VENTANA / 2 - 450/2,150,500,300,None,None,"PIXEL ADVENTURE/Recursos/Menu/Buttons/you win.png",None,"Arial",30,C_BLACK)
        self.lose = Widget(self,ANCHO_VENTANA / 2 - 450/2,170,500,300,None,None,"PIXEL ADVENTURE/Recursos/Menu/Buttons/you lose.png",None,"Arial",30,C_BLACK)
        self.lista_widget = [self.time,self.score]
        self.tick_1s = pygame.USEREVENT+0
        pygame.time.set_timer(self.tick_1s,1000)
        #frutas
        self.fruits = self.lista_info.list_fruits
        
        self.lista_info.puntos = 0

    def update(self,delta_ms,lista_events):
        if(not self.lista_info.win and not self.player_dos.muerte and self.time_juego > 0):
            
            for aux_boton in self.lista_widget:    
                aux_boton.draw()
        
            self.lista_info.update(delta_ms,self.player_dos,self.master_form)

            self.time._text = self.time_juego
            self.score._text = self.lista_info.puntos

            self.time.update(lista_events)
            self.score.update(lista_events)

            #player_dos
            self.player_dos.update(delta_ms,self.lista_plataformas,self.lista_enemigos,lista_events,self.lista_info.list_trampas)
            self.player_dos.draw()

            self.barra_vida.update(lista_events,self.player_dos.hp)
            self.barra_vida.draw()

        if(self.lista_info.win):
            self.win_lvl2 = True
            self.win.update(lista_events)
            self.win.draw()
            self.display_finish_lvl(delta_ms)

        elif(self.player_dos.muerte or self.time_juego <= 0):
            self.lose.update(lista_events)
            self.lose.draw()
            self.display_finish_lvl(delta_ms)
        
        for event in lista_events:
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    self.set_active("pause")
            if (event.type == self.tick_1s):
                self.time_juego -= 1
       
    def display_finish_lvl(self,delta_ms):
        self.contador_puntos = self.lista_info.puntos
        self.acumulador_time += delta_ms
        if(self.acumulador_time >= 2000):
            self.set_active("name_player")
            self.forms_dict["name_player"].nivel_actual = "nivel_dos"
            self.resetear()
            self.acumulador_time = 0

        