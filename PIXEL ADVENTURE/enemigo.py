import pygame
from constantes import *
from auxiliar import *
from player import *

class Enemy:
    def __init__(self,x,y,speed,move_rate_ms,frame_rate_ms,screen) -> None:
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/AngryPig/Idle (36x30).png",9,1,False,1,2)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/AngryPig/Idle (36x30).png",9,1,True,1,2)
        self.hit = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/AngryPig/Hit 1 (36x30).png",5,1,False,1,2)
        self.frame = 0
        self.animation = self.stay_l
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_x = 0
        self.move_y = 0
        self.speed = speed
        self.direction = "R"
        self.live = True
        self.vida = 50
        self.impacto = False

        self.tiempo_colision = 0
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms
        self.tiempo_transcurrido_move = 0
        self.tiempo_spawn = 0
        self.tiempo_transcurrido_animation = 0
        self.tiempo_attack = 0
        self.damage_generate = 0
        self.colicion = False

        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_COLLIDE_H)
        self.rect_vision = pygame.Rect(self.rect.x - 100,self.rect.y,self.rect.w + 150,self.rect.h)
        self.rect_collition_bala_l = pygame.Rect(self.rect.x - 2,self.rect.y,self.rect.w - 70,self.rect.h)
        self.rect_collition_bala_r = pygame.Rect(self.rect.x + 20,self.rect.y,self.rect.w - 70,self.rect.h)

        self.tiempo_transcurrido = 0


    def spawn(self,direction):
        self.tiempo_spawn = pygame.time.get_ticks() 
        self.direction = direction
        if(direction == DIRECTION_R):
            self.animation = self.stay_r
        else:
            self.animation = self.stay_l
        self.frame = 0

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,255,255),rect=self.rect_vision)
            pygame.draw.rect(screen,color=(255,0,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(0,255,0),rect=self.rect_ground_collition)
            pygame.draw.rect(screen,color=(255,255,255),rect=self.rect_collition_bala_l)
            pygame.draw.rect(screen,color=(255,255,255),rect=self.rect_collition_bala_r)

        if(self.live):
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)
    
    def do_movement(self,delta_ms):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def update(self,delta_ms,player):
        self.do_movement(delta_ms)
        self.do_animation(delta_ms) 

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.rect_ground_collition.x += delta_x
        self.ground_collition_rect.x += delta_x
        self.rect_collition_bala_r.x += delta_x
        self.rect_collition_bala_l.x += delta_x 
 
    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.rect_ground_collition.y += delta_y
        self.ground_collition_rect.y += delta_y
        self.rect_collition_bala_r.y += delta_y
        self.rect_collition_bala_l.y += delta_y

    def animation_frame(self,animation):
        if(self.animation != animation):
            self.frame = 0
                

class EnemyGreen(Enemy):
    def __init__(self, x, y, speed, move_rate_ms, frame_rate_ms,screen) -> None:
        super().__init__(x, y, speed, move_rate_ms, frame_rate_ms,screen)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/AngryPig/Idle (36x30).png",9,1,False,1,2)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/AngryPig/Idle (36x30).png",9,1,True,1,2)
        self.move_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/AngryPig/Run (36x30).png",12,1,False,1,2)
        self.move_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/AngryPig/Run (36x30).png",12,1,True,1,2)
        self.hit = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/AngryPig/Hit 1 (36x30).png",5,1,False,1,2)
        self.spawn(DIRECTION_L)
        
        self.rect_vision = pygame.Rect(self.rect.x - 270,self.rect.y,self.rect.w + 200,self.rect.h)

    def x_move(self,delta_ms):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move > self.move_rate_ms ):
            self.animation_frame(self.move_l)
            self.animation = self.move_l
            self.move_x = -self.speed
            self.change_x(self.move_x)
            self.tiempo_transcurrido_move = 0
            self.tiempo_colision = 0

    def collition_vision(self,pos_xy,delta_ms):
        if(self.rect_vision.colliderect(pos_xy)):
            self.x_move(delta_ms)

    def is_collision_bala(self):
        if(self.impacto):
            self.vida -= self.damage_generate
            self.animation_frame(self.hit)
            self.animation = self.hit
            self.impacto = False
            if(self.vida <= 0):
                self.live = False
    
    def update(self,delta_ms,player):
        super().update(delta_ms,player)
        self.collition_vision(player.collition_rect,delta_ms)
                
class EnemyPlant(Enemy):
    def __init__(self, x, y, speed, move_rate_ms, frame_rate_ms,screen) -> None:
        super().__init__(x, y, speed, move_rate_ms, frame_rate_ms,screen)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/Plant/Idle (44x42).png",11,1,False,1,1.5)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/Plant/Idle (44x42).png",11,1,True,1,1.5)
        self.attack_planta_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/Plant/Attack (44x42).png",8,1,False,1,1.5)
        self.spawn(DIRECTION_L)
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y + 20, self.rect.w / 3, GROUD_RECT_H_PLANTA)
        self.rect_vision = pygame.Rect(self.rect.x - 300,self.rect.y,self.rect.w + 400,self.rect.h + 20)
        self.tiempo_transcurrido_attack = 0
        self.direction = "L"
        self.spawn(DIRECTION_L)
        self.lista_proyectiles = ListProyectil(screen,self.rect,"Enemies/Plant/Bullet.png",self)
        self.tiempo_attack = 0 
    
    def is_collision_bala(self):
        if(self.impacto):
            self.vida -= self.damage_generate
            self.impacto = False
            if(self.vida <= 0):
                self.live = False

    def disparar(self,delta_ms):
        self.tiempo_attack += delta_ms
        if(self.animation == self.attack_planta_l and self.tiempo_attack >= self.frame_rate_ms + 1450):
            self.tiempo_attack = 0
            self.lista_proyectiles.generar_balas(4,self.direction,-30,10)

    def attack(self,pos_xy):  
        if self.rect_vision.colliderect(pos_xy):
            self.animation_frame(self.attack_planta_l)
            self.animation = self.attack_planta_l 
        else:
            self.animation_frame(self.stay_l)
            self.animation = self.stay_l
            
    def update(self,delta_ms,player):
        super().update(delta_ms,player)
        self.attack(player.collition_rect) 
        self.lista_proyectiles.update([player])
        self.disparar(delta_ms)
    
        
class EnemyGhost(Enemy):
    def __init__(self, x, y, speed, move_rate_ms, frame_rate_ms, screen) -> None:
        super().__init__(x, y, speed, move_rate_ms, frame_rate_ms, screen)

        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/Ghost/Desappear (44x30).png",4,1,False,1,1.5)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/Ghost/Desappear (44x30).png",4,1,True,1,1.5)
        self.spawn(DIRECTION_R)
        self.hit = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/Ghost/Hit (44x30).png",5,1,True,1,1.5)
        self.attack_ghost = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/Ghost/Idle (44x30).png",10,1,True,1,1.5)
        self.rect_collition_bala_l = pygame.Rect(self.rect.x - 2,self.rect.y,self.rect.w - 65,self.rect.h)

        self.rect_vision = pygame.Rect(self.rect.x + 50,self.rect.y,self.rect.w + 300,self.rect.h + 20)
        self.lista_proyectiles = ListProyectil(screen,self.rect,"Enemies/Plant/Bullet.png",self)

    def is_collision_bala(self):
        if(self.impacto):
            self.vida -= self.damage_generate
            self.animation_frame(self.hit)
            self.animation = self.hit
            self.impacto = False
            if(self.vida <= 0):
                self.live = False

    def disparar(self,delta_ms):
        self.tiempo_attack += delta_ms
        if(self.animation == self.attack_ghost and self.tiempo_attack >= self.frame_rate_ms + 1450):
            self.tiempo_attack = 0
            self.lista_proyectiles.generar_balas(4,self.direction,10,10)

    def attack(self,pos_xy):  
        if self.rect_vision.colliderect(pos_xy):
            self.animation_frame(self.attack_ghost)
            self.animation = self.attack_ghost 
        else:
            self.animation_frame(self.stay_r)
            self.animation = self.stay_r
        
    def update(self, delta_ms,player):
        super().update(delta_ms,player)
        self.lista_proyectiles.update([player])
        self.attack(player.collition_rect)
        self.disparar(delta_ms)

class EnemyRino(Enemy):
    def __init__(self, x, y, speed, move_rate_ms, frame_rate_ms, screen) -> None:
        super().__init__(x, y, speed, move_rate_ms, frame_rate_ms, screen)

        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/Rino/Idle (52x34).png",11,1,False,1,1.5)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/Rino/Idle (52x34).png",11,1,True,1,1.5)  
        self.spawn(DIRECTION_L)
        self.move_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/Rino/Run (52x34).png",6,1,False,1,1.5)
        self.move_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/Rino/Run (52x34).png",6,1,True,1,1.5)
        
        self.hit = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies/Rino/Hit (52x34).png",5,1,False,1,1.5)
        self.rect_vision = pygame.Rect(self.rect.x - 150,self.rect.y,self.rect.w + 400,self.rect.h)

    def is_collision_bala(self):
        if(self.impacto):
            self.vida -= self.damage_generate
            self.animation_frame(self.hit)
            self.animation = self.hit
            self.impacto = False
            if(self.vida <= 0):
                self.live = False

    def x_move(self,delta_ms):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move > self.move_rate_ms):
            self.animation_frame(self.move_l)
            self.animation = self.move_l
            self.move_x = -self.speed
            self.change_x(self.move_x)
            self.tiempo_transcurrido_move = 0
            self.tiempo_colision = 0
    
    def collition_vision(self,pos_xy,delta_ms):
        if(self.rect_vision.colliderect(pos_xy)):
            self.x_move(delta_ms)

    def update(self, delta_ms,player):
        super().update(delta_ms,player)
        self.collition_vision(player,delta_ms)
        