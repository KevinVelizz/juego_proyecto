import pygame
from constantes import *
from cargar_json import *
from enemigo import *
from plataforma import *
from varios import *
from proyectil import *
from score import *
from trampas import *

class Datalevels:
    def __init__(self,screen,lvl) -> None:   
        self.lvl = lvl     
        self.lista_data = cargar_json_data("PIXEL ADVENTURE/levels.json")[0][self.lvl]
        self.screen = screen
        self.player = Player(100,540,10,10,50,10,15,10,screen)
        self.lista_enemy = []
        self.lista_platform = []
        self.list_fruits = []
        self.list_trampas = []
        self.create_ememies()
        self.create_trampas()
        self.create_platforms()
        self.create_fruits()
        self.win = False

    def create_ememies(self):
        '''
        El metodo crea la lista de enemigos para cada nivel desde la información exportada del json.
        '''
        for enemy in self.lista_data["enemys"]:
            if(self.lvl == "level_one"):
                if(enemy["name"] == "chanchito"):
                    for i in range(enemy["amount"]):
                        self.lista_enemy.append(EnemyGreen(enemy["position_x"][i],enemy["position_y"][i],enemy["speed"][i],50,50,self.screen))
                if(enemy["name"] == "planta"):
                    for i in range(enemy["amount"]):
                        self.lista_enemy.append(EnemyPlant(enemy["position_x"][i],enemy["position_y"][i],enemy["speed"][i],50,50,self.screen))

            elif(self.lvl == "level_two"):           
                if(enemy["name"] == "ghost"):
                    for i in range(enemy["amount"]):
                        self.lista_enemy.append(EnemyGhost(enemy["position_x"][i],enemy["position_y"][i],enemy["speed"][i],50,50,self.screen))
                if(enemy["name"] == "rino"):
                    for i in range(enemy["amount"]):
                        self.lista_enemy.append(EnemyRino(enemy["position_x"][i],enemy["position_y"][i],enemy["speed"][i],50,50,self.screen))

            elif(self.lvl == "level_three"):
                if(enemy["name"] == "ghost"):  
                    for i in range(enemy["amount"]):
                        self.lista_enemy.append(EnemyGhost(enemy["position_x"][i],enemy["position_y"][i],enemy["speed"][i],50,50,self.screen))
                if(enemy["name"] == "planta"):
                    for i in range(enemy["amount"]):
                        self.lista_enemy.append(EnemyPlant(enemy["position_x"][i],enemy["position_y"][i],enemy["speed"][i],50,50,self.screen))

    def create_platforms(self):
        '''
        El metodo crea la lista de plataformas para cada nivel desde la información exportada del json.
        '''
        for platform in self.lista_data["platforms"]:
            if(platform["name"] == "left_wall"):
                for i in range(platform["amount"]):
                    self.lista_platform.append(Platform(platform["position_x"],platform["position_y"][i],platform["width"],platform["speed"],platform["height"],50,0,0,0,4,0))
            
            if(platform["name"] == "right_wall"):
                for i in range(platform["amount"]):
                    self.lista_platform.append(Platform(platform["position_x"],platform["position_y"][i],platform["width"],platform["speed"],platform["height"],50,0,0,0,4,0))

            elif(platform["name"] == "flat"):
                for i in range(platform["amount"]):
                    self.lista_platform.append(Platform(platform["position_x"][i],platform["position_y"],platform["width"],platform["speed"],platform["height"],50,0,0,0,1,0))
            
            elif(platform["name"] == "some"):
                for i in range(platform["amount"]):
                    self.lista_platform.append(Platform(platform["position_x"][i],platform["position_y"][i],platform["width"],platform["speed"],platform["height"],50,0,0,0,platform["type"][i],0))
            
            elif(platform["name"] == "movable"):
                for i in range(platform["amount"]):
                    self.lista_platform.append(Platform(platform["position_x"][i],platform["position_y"][i],platform["width"],platform["speed"][i],platform["height"],50,platform["point_move_l"][i],platform["point_move_r"][i],platform["speed_up_down"],platform["type"][i],platform["punto_volver_plat_up"][i]))

    def create_fruits(self):
        '''
        El metodo crea la lista de frutas para cada nivel desde la información exportada del json.
        '''
        self.win = False
        for fruit in self.lista_data["fruits"]:
            if(fruit["name"] == "apple"):
                for i in range(fruit["amount"]):
                    self.list_fruits.append(Fruta(fruit["position_x"][i],fruit["position_y"][i],50,fruit["speed"]))
            if(fruit["name"] == "apple_movable"):
                for i in range(fruit["amount"]):
                    self.list_fruits.append(Fruta(fruit["position_x"][i],fruit["position_y"][i],50,fruit["speed"][i]))

    def create_trampas(self):
        '''
        El metodo crea la lista de trampas para cada nivel desde la información exportada del json.
        '''
        for trampa in self.lista_data["trampas"]:
            if(trampa["name"] == "cierra"):
                for i in range(trampa["amount"]):
                    self.list_trampas.append(Trampa(trampa["position_x"][i],trampa["position_y"][i],50,self.screen))

    def update(self,delta_ms,screen):
        '''
        Updatea y dibuja las trampas, plataformas,enemigos y frutas.
        Recibe por parametro el tiempo actual del juego y la pantalla.
        '''
        for trampa in self.list_trampas:
            trampa.update(delta_ms)
            trampa.draw()

        for platform in self.lista_platform:
            platform.update(delta_ms)
            platform.draw(self.screen)
        
        for enemy in self.lista_enemy:
            enemy.update(delta_ms,self.player)
            enemy.draw(self.screen)
            if(not enemy.live):
                self.lista_enemy.remove(enemy)
                self.player.puntos_player = self.player.puntos_player + 50

        for fruit in self.list_fruits:
            fruit.update(delta_ms,self.lista_platform,self.player.collition_rect)
            fruit.draw(screen)    
            if(fruit.collision):
                self.player.puntos_player = self.player.puntos_player + 50
                self.list_fruits.remove(fruit)

            if(len(self.list_fruits) <= 0):
                self.win = True 
        

        