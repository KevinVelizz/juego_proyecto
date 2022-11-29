#json se llama nivel, en ese nivel el player,enemigo,posicion,obstaculos.
import pygame
from pygame.locals import *
import sys
from constantes import *
from cargar_json import *
from gui_form_level1 import *
from gui_form_menu import *
from gui_menu_options import *
from gui_form_lvls import *
from gui_form_lvl2 import *
from gui_from_pause import *
from gui_puntos import *
from gui_form_lvl3 import *

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()
imagen_fondo = pygame.image.load(PATH_IMAGE + "fondo/game_background_3. 2.png").convert()
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

level_uno = LevelUno("level_uno",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,C_BLACK,False,image_background=None,color_background=None)
menu = FormMenu("Menu",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,(0,0,0),True,image_background= "fondo/game_background_3. 2.png",color_background=None)
options = FormOptions("Options",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,(0,0,0),False,image_background="fondo/game_background_3. 2.png",color_background=None)
levels = FormLevels("levels",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,(0,0,0),False,image_background="fondo/game_background_3. 2.png",color_background=None)
level_dos = LevelDos("level_dos",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,(0,0,0),False,"fondo/game_background_3. 2.png",color_background=None)
juego_pause = FormPauseLvl("pause",screen,500,100,400,400,(0,0,0),False,image_background="Menu/Buttons/bg.png",color_background=None)
ranking = FormRanking("ranking",screen,500,250,500,300,(0,0,0),False,"Menu/Buttons/table.png",None)
level_tres = LevelTres("level_tres",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,(0,0,0),False,"fondo/game_background_3. 2.png",None)
    
while True:
    lista_events = pygame.event.get()   
    for event in lista_events:
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
    delta_ms = clock.tick(FPS)

    if(level_uno.active):
        level_uno.draw()
        level_uno.play_juego(delta_ms,lista_events)
        
    elif(levels.active):
        levels.update(lista_events)
        levels.draw()

    elif(menu.active):
        menu.update(lista_events)
        menu.draw()

    elif(options.active):
        options.update(lista_events)
        options.draw()

    elif(level_dos.active):
        level_dos.update(lista_events)
        level_dos.draw()
        level_dos.play_juego(delta_ms,lista_events)

    elif(juego_pause.active):
        juego_pause.update(lista_events)
        juego_pause.draw()
    
    elif(level_tres.active):
        level_tres.update(lista_events)
        level_tres.draw()
        level_tres.play_juego(delta_ms,lista_events)

    if(ranking.active):
        screen.blit(imagen_fondo,(0,0))
        ranking.puntos(lista_events,(level_uno.contador_puntos + level_dos.contador_puntos))
        ranking.draw()

    pygame.display.flip()  