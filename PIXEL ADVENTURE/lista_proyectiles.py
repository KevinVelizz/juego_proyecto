import pygame 
from proyectil import *

class ListProyectil:
    def __init__(self,screen,pos_xy,path_image,creador) -> None:
        self.pos_xy = pos_xy
        self.surface = screen
        self.lista_balas = []
        self.tiempo_transcurrido = 0
        self.creador = creador
        self.path_image = path_image
 
    def generar_balas(self,velocidad,direction,x,y):
        '''
        El metodo genera las balas desde donde quiere salir.
        Recibe por parametro la velocidad de la bala y la direccion en la que se encuentra el enemigo o player y x e y la posición de salida.
        '''
        self.lista_balas.append(Proyectil(self.pos_xy.x + x,self.pos_xy.y + y,velocidad,direction,self.path_image,self.creador))
   
    def update(self,lista_objetivos):
        for proyectil in self.lista_balas:
            proyectil.update(lista_objetivos)
            proyectil.draw(self.surface)
            if(proyectil.impacto_objetivo):
                self.lista_balas.remove(proyectil)
            
            

