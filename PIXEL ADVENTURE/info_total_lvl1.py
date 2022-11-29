import pygame
from constantes import *
from cargar_json import *
from enemigo import *
from plataforma import *
from varios import *
from proyectil import *
from score import *
from trampas import *

class CargarData:
    def __init__(self,screen) -> None:        
        self.lista_data = cargar_json_data("PIXEL ADVENTURE/levels.json")[0]["level_one"]
        self.screen = screen
        self.lista_enemy = []
        self.lista_platform = []
        self.list_fruits = []
        self.list_trampas = []
        self.create_trampas()
        self.create_ememies()
        self.create_platforms()
        self.create_fruits()
        
        self.puntos = 0
    
    def create_ememies(self):
        for enemy in self.lista_data["enemys"]:
            if(enemy["name"] == "chanchito"):
                self.lista_enemy.append(EnemyGreen(enemy["position_x"],enemy["position_y"],enemy["speed"],50,50,self.screen))
            if(enemy["name"] == "planta"):
                self.lista_enemy.append(EnemyPlant(enemy["position_x"],enemy["position_y"],enemy["speed"],50,50,self.screen))

    def create_platforms(self):
        for platform in self.lista_data["platforms"]:
            if(platform["name"] == "left_wall"):
                for i in range(platform["amount"]):
                    self.lista_platform.append(Platform(platform["position_x"],platform["position_y"][i],platform["width"],platform["speed"],platform["height"],50,0,0,0,4))
            
            if(platform["name"] == "right_wall"):
                for i in range(platform["amount"]):
                    self.lista_platform.append(Platform(platform["position_x"],platform["position_y"][i],platform["width"],platform["speed"],platform["height"],50,0,0,0,4))

            elif(platform["name"] == "flat"):
                for i in range(platform["amount"]):
                    self.lista_platform.append(Platform(platform["position_x"][i],platform["position_y"],platform["width"],platform["speed"],platform["height"],50,0,0,0,1))
            
            elif(platform["name"] == "some"):
                for i in range(platform["amount"]):
                    self.lista_platform.append(Platform(platform["position_x"][i],platform["position_y"][i],platform["width"],platform["speed"],platform["height"],50,0,0,0,platform["type"][i]))
            
            elif(platform["name"] == "movable"):
                for i in range(platform["amount"]):
                    self.lista_platform.append(Platform(platform["position_x"][i],platform["position_y"][i],platform["width"],platform["speed"],platform["height"],50,platform["point_move_l"][i],platform["point_move_r"][i],platform["speed_up_down"],platform["type"][i]))

    def create_fruits(self):
        
        self.win = False
        for fruit in self.lista_data["fruits"]:
            if(fruit["name"] == "apple"):
                for i in range(fruit["amount"]):
                    self.list_fruits.append(Fruta(fruit["position_x"][i],fruit["position_y"][i],50,fruit["speed"]))
            if(fruit["name"] == "apple_movable"):
                for i in range(fruit["amount"]):
                    self.list_fruits.append(Fruta(fruit["position_x"][i],fruit["position_y"][i],50,fruit["speed"]))

    def create_trampas(self):
        for trampa in self.lista_data["trampas"]:
            if(trampa["name"] == "cierra"):
                for i in range(trampa["amount"]):
                    self.list_trampas.append(Trampa(trampa["position_x"][i],trampa["position_y"][i],50,self.screen))

    def update(self,delta_ms,player,screen):
        for trampa in self.list_trampas:
            trampa.update(delta_ms)
            trampa.draw()

        for platform in self.lista_platform:
            platform.update(delta_ms)
            platform.draw(self.screen)
        
        for enemy in self.lista_enemy:
            enemy.update(delta_ms,player)
            enemy.draw(self.screen)
            if(not enemy.live):
                self.lista_enemy.remove(enemy)
                self.puntos = self.puntos + 50

        for fruit in self.list_fruits:
            fruit.update(delta_ms,self.lista_platform,player.collition_rect)
            fruit.draw(screen)    
            if(fruit.collision):
                self.puntos = self.puntos + 50
                self.list_fruits.remove(fruit)

            if(len(self.list_fruits) <= 0):
                self.win = True 
        
        