import pygame 
from settings import *
from player import Player
from terrain import *
import sys

class Level2:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # 建立游戏中对象存储的精灵组
        self.all_sprites = pygame.sprite.Group()
        self.obs_sprites = pygame.sprite.Group()

        
        #初始化，建立角色和地图对象
        self.draw_wall()
        self.setup()
        self.background_image = pygame.image.load(WORLD_PATH3)
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #建立角色
    def setup(self):
        self.player = Player((100,550), self.all_sprites,self.obs_sprites)


    def draw_wall(self):
        for y in range(len(SCREEN_MAP2)):
            for x in range(len(SCREEN_MAP2[y])):
                if SCREEN_MAP2[y][x]==0:
                    continue
                #地图的生成
                if SCREEN_MAP2[y][x]==1 :
                    wall=Ground(GROUND_PATH,self.obs_sprites,(x*38+19,y*30+15),1,self.all_sprites)
                    self.obs_sprites.add(wall)
                if SCREEN_MAP2[y][x]==5 :
                    wall=Ground(GROUND_PATH3,self.obs_sprites,(x*38+19,y*30+15),1,self.all_sprites)
                    self.obs_sprites.add(wall)
    
    def run(self,dt):
        self.player.dx=0
        self.player.dy=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type ==pygame.KEYDOWN:
                #玩家行为的获取
                self.player.input_j(event)
        self.display_surface.blit(self.background_image, (0, 0)) 
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
        self.obs_sprites.draw(self.display_surface)
        self.obs_sprites.update()