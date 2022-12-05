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
from gui_ranking import *
from gui_form_lvl3 import *
from gui_form_name import *
from controller import *
from gui_form_rankings import *

pygame.init()
pygame.mixer.music.load("PIXEL ADVENTURE/Recursos/music/musica_fondo.wav")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
clock = pygame.time.Clock()
imagen_fondo = pygame.image.load(PATH_IMAGE + "fondo/game_background_3. 2.png").convert()
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

level_uno = LevelUno("level_uno",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,C_BLACK,False,image_background=None,color_background=None)
menu = FormMenu("Menu",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,(0,0,0),True,image_background= "fondo/game_background_3. 2.png",color_background=None)
options = FormOptions("Options",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,(0,0,0),False,image_background="fondo/game_background_3. 2.png",color_background=None)
levels = FormLevels("levels",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,(0,0,0),False,image_background="fondo/game_background_3. 2.png",color_background=None)
level_dos = LevelDos("level_dos",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,(0,0,0),False,"fondo/game_background_3. 2.png",color_background=None)
juego_pause = FormPauseLvl("pause",screen,500,100,400,400,None,False,image_background="Menu/Buttons/bg.png",color_background=None)
ranking1 = FormRanking("nivel_uno",screen,550,100,400,600,None,False,"Menu/Buttons/table.png",None)
ranking2 = FormRanking("nivel_dos",screen,550,100,400,600,None,False,"Menu/Buttons/table.png",None)
ranking3 = FormRanking("nivel_tres",screen,550,100,400,600,None,False,"Menu/Buttons/table.png",None)
level_tres = LevelTres("level_tres",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,(0,0,0),False,"fondo/game_background_3. 2.png",None)
form_name_player = FormTextName("name_player",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,False,"fondo/game_background_3. 2.png",None)
form_clasifiaciones = FormClasificaciones("ranking",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,False,"fondo/game_background_3. 2.png",None)

while True:
    lista_events = pygame.event.get()   
    for event in lista_events:
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

    delta_ms = clock.tick(FPS)

    if(level_uno.active):
        level_uno.draw()
        level_uno.update(delta_ms,lista_events)
        
    elif(levels.active):
        levels.update(lista_events,(level_uno.win_lvl,level_dos.win_lvl2))
        levels.draw()

    elif(menu.active):        
        menu.update(lista_events)
        menu.draw()

    elif(options.active):
        options.update(lista_events)
        options.draw()
    
    elif(level_dos.active):
        level_dos.draw()
        level_dos.update(delta_ms,lista_events)

    elif(juego_pause.active):
        juego_pause.update(lista_events)
        juego_pause.draw()
    
    elif(level_tres.active):
        level_tres.draw()
        level_tres.update(delta_ms,lista_events)

    elif(form_name_player.active):
        form_name_player.update(lista_events)
        form_name_player.draw()
        puntos = level_uno.contador_puntos + level_dos.contador_puntos + level_tres.contador_puntos
        nombre = form_name_player.nombre_viajar

        if(nombre != ""):
            insertRow(nombre,puntos,form_name_player.nivel_actual)
            nombre = ""
            form_name_player.nombre_viajar = ""
            level_uno.contador_puntos = 0
            level_dos.contador_puntos = 0
            level_tres.contador_puntos = 0
            form_name_player.name_player._text = "Player"

    elif(form_clasifiaciones.active):
        form_clasifiaciones.update(lista_events)
        form_clasifiaciones.draw()

    elif(ranking1.active):
        ranking1.update(lista_events)
        ranking1.draw()

    elif(ranking2.active):
        ranking2.update(lista_events)
        ranking2.draw()

    elif(ranking3.active):
        ranking3.update(lista_events)
        ranking3.draw()

    pygame.display.flip()  