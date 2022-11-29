import pygame
from gui_form import *
from pygame.locals import *
import sys
from constantes import *
from player import *
from plataforma import *
from score import *
from gui_barravida import *
from info_total_lvl2 import *

class LevelDos(Form):
    def __init__(self, name, master_form, x, y, w, h, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master_form, x, y, w, h, color_border, active, image_background, color_background)

        self.master_form = master_form
        self.lista_info = DataLevelDos(master_form)
        self.imagen_fondo = pygame.image.load(PATH_IMAGE + self.lista_info.lista_info ["background"]).convert()
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
        self.player_dos = PlayerDos(100,500,10,10,50,10,15,10,master_form)
        self.barra_vida = BarraVida(self,x=10,y=10,w=500,h=50,color_background=C_BLACK,color_border=C_BLUE,image_background=None,image_progress=None,value = self.player_dos.hp, value_max=self.player_dos.hp,color_vida=C_WHITE)
        self.lista_plataformas = self.lista_info.lista_platform
        self.contador_puntos = 0
        self.acumulador_time = 0
        
        #enemigos
        self.lista_enemigos = self.lista_info.lista_enemy

        #frutas
        self.fruits = self.lista_info.list_fruits

        #score
        self.text_score = Text(1300,30,"SCORE: ",(0,0,0),master_form)
        self.lose = pygame.image.load(PATH_IMAGE + "Menu/Buttons/you lose.png").convert()
        self.lose = pygame.transform.scale(self.lose,(300,400)) 
        self.win = pygame.image.load(PATH_IMAGE + "Menu/Buttons/you win.png").convert()
        self.win = pygame.transform.scale(self.win,(300,400))

    def draw(self):
        super().draw()
        self.surface.fill((0,0,0))
        self.surface.blit(self.imagen_fondo,(0,0))
    
    def resetear(self):
        self.lista_info = DataLevelDos(self.master_form)
        self.imagen_fondo = pygame.image.load(PATH_IMAGE + self.lista_info.lista_info ["background"]).convert()
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
        self.player_dos = PlayerDos(100,500,10,10,50,10,15,10,self.master_form)
        self.barra_vida = BarraVida(self,x=10,y=10,w=500,h=50,color_background=C_BLACK,color_border=C_BLUE,image_background=None,image_progress=None,value = self.player_dos.hp, value_max=self.player_dos.hp,color_vida=C_WHITE)
        self.lista_plataformas = self.lista_info.lista_platform
        self.contador_puntos = 0
        self.lista_enemigos = self.lista_info.lista_enemy
        #frutas
        self.fruits = self.lista_info.list_fruits
        self.lose = pygame.image.load(PATH_IMAGE + "Menu/Buttons/you lose.png").convert()
        self.lose = pygame.transform.scale(self.lose,(450,300)) 
        self.win = pygame.image.load(PATH_IMAGE + "Menu/Buttons/you win.png").convert()
        self.win = pygame.transform.scale(self.win,(450,300))

    def play_juego(self,delta_ms,lista_events):
        if(not self.lista_info.win and not self.player_dos.muerte):
            text_score2 = Text(1400,30,"{0}".format(self.lista_info.puntos),(0,0,0),self.master_form)

            self.lista_info.update(delta_ms,self.player_dos)

            #player_dos
            self.player_dos.update(delta_ms,self.lista_plataformas,self.lista_enemigos,lista_events,self.lista_info.list_trampas)
            self.player_dos.draw()

            self.text_score.draw()
            text_score2.draw()

            self.barra_vida.update(lista_events,self.player_dos.hp)
            self.barra_vida.draw()

        if(self.lista_info.win):
            self.contador_puntos = self.lista_info.puntos
            self.surface.blit(self.win,(ANCHO_VENTANA / 2 - 450/2,150))
            self.acumulador_time += delta_ms
            if(self.acumulador_time >= 2000):
                self.set_active("levels")
                self.resetear()
                self.acumulador_time = 0

        if(self.player_dos.muerte):
            self.contador_puntos = self.lista_info.puntos
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
       