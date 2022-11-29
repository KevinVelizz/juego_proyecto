import pygame
from gui_form import *
from pygame.locals import *
import sys
from constantes import *
from player import *
from plataforma import *
from score import *
from gui_barravida import *
from info_total_lvl1 import *
from gui_textbox import *
from gui_widget import *
from gui_time import *

class LevelUno(Form):
    def __init__(self, name, master_form, x, y, w, h, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master_form, x, y, w, h, color_border, active, image_background, color_background)

        self.master_form = master_form
        self.lista_data = CargarData(master_form)
        self.imagen_fondo = pygame.image.load(PATH_IMAGE + "Background/Blue.png").convert()
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
        self.player = Player(100,500,10,10,50,10,15,10,master_form)
        self.barra_vida = BarraVida(self,x=10,y=10,w=500,h=50,color_background=C_BLACK,color_border=C_BLUE,image_background=None,image_progress=None,value = self.player.hp, value_max=self.player.hp,color_vida=C_WHITE)
        self.lista_plataformas = self.lista_data.lista_platform
        self.contador_puntos = 0
        self.acumulador_time = 0
        self.text_score = 0
        self.time_acumulador = 0
        self.time = FormTime("time",self.master_form,600,20,200,100,(0,0,0),True,None,None)

        self.lista_widget = [self.time]
        #enemigos
        self.lista_enemigos = self.lista_data.lista_enemy

        #frutas
        self.fruits = self.lista_data.list_fruits

        #score
        self.text_score = Text(1300,30,"SCORE: ",(0,0,0),master_form)
        self.lose = pygame.image.load(PATH_IMAGE + "Menu/Buttons/you lose.png").convert()
        self.lose = pygame.transform.scale(self.lose,(450,300)) 
        self.win = pygame.image.load(PATH_IMAGE + "Menu/Buttons/you win.png").convert()
        self.win = pygame.transform.scale(self.win,(450,300)) 

    def draw(self):
        super().draw()
        self.surface.blit(self.imagen_fondo,(0,0))
        # for aux_boton in self.lista_widget:
        #     aux_boton.draw()

    def resetear(self):
        self.lista_data = CargarData(self.master_form)
        self.imagen_fondo = pygame.image.load(PATH_IMAGE + "Background/Blue.png").convert()
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
        self.player = Player(100,500,10,10,50,10,15,10,self.master_form)
        self.barra_vida = BarraVida(self,x=10,y=10,w=500,h=50,color_background=C_BLACK,color_border=C_BLUE,image_background=None,image_progress=None,value = self.player.hp, value_max=self.player.hp,color_vida=C_WHITE)
        self.lista_plataformas = self.lista_data.lista_platform
        self.lista_data.puntos = 0
        #enemigos
        self.lista_enemigos = self.lista_data.lista_enemy

        #frutas
        self.fruits = self.lista_data.list_fruits
        self.lose = pygame.image.load(PATH_IMAGE + "Menu/Buttons/you lose.png").convert()
        self.lose = pygame.transform.scale(self.lose,(450,300)) 
        self.win = pygame.image.load(PATH_IMAGE + "Menu/Buttons/you win.png").convert()
        self.win = pygame.transform.scale(self.win,(450,300)) 

    def play_juego(self,delta_ms,lista_events):
        if(not self.lista_data.win and not self.player.muerte):
            
            self.time.active = True
            self.time.puntos(lista_events,self.time_acumulador)

            text_score2 = Text(1400,30,"{0}".format(self.lista_data.puntos),(0,0,0),self.master_form)

            self.lista_data.update(delta_ms,self.player,self.master_form)
            #player
            self.player.update(delta_ms,self.lista_plataformas,self.lista_enemigos,lista_events,self.lista_data.list_trampas)
            self.player.draw()

            self.barra_vida.update(lista_events,self.player.hp)
            self.barra_vida.draw()

            self.text_score.draw()
            text_score2.draw()

        if(self.lista_data.win):
            self.contador_puntos = self.lista_data.puntos
            print(self.contador_puntos)
            self.surface.blit(self.win,(ANCHO_VENTANA / 2 - 450/2,150))
            self.acumulador_time += delta_ms
            if(self.acumulador_time >= 2000):
                self.set_active("levels")
                self.resetear()
                self.acumulador_time = 0

        if(self.player.muerte):
            self.contador_puntos = self.lista_data.puntos
            self.surface.blit(self.lose,(ANCHO_VENTANA / 2 - 450/2,150))
            self.acumulador_time += delta_ms
            if(self.acumulador_time >= 2000):
                self.set_active("levels")
                self.resetear()
                self.acumulador_time = 0

        for event in lista_events:
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    self.set_active("pause")
            

       