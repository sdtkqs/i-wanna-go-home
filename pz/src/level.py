import pygame 
from settings import *
from player import Player
from terrain import *
import sys
from play_die import *
from bandzi import *
#游戏的功能运行类
#————————————————————————————————————————————————————————————————————————————————
class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # 建立游戏中对象存储的精灵组
        self.all_sprites = pygame.sprite.Group()
        self.obs_sprites = pygame.sprite.Group()
        self.boom_sprite = pygame.sprite.Group()
        self.bullet_sprites=pygame.sprite.Group()

        
        #初始化，建立角色和地图对象
        self.draw_wall()
        self.setup()
        self.alive=True
        self.position=(0,0)
        self.overl=False
    
    #建立角色
    def setup(self):
        self.player = Player((100,550), self.all_sprites,self.obs_sprites)
        self.over=Over(self.boom_sprite)
        self.boom_sprite.add(self.over)
    
    
    #绘制地图
    #type==1为草块
    #type==2为刺
    def draw_wall(self):
        for y in range(len(SCREEN_MAP)):
            for x in range(len(SCREEN_MAP[y])):
                if SCREEN_MAP[y][x]==0:
                    continue
                
                
                
                #刺的生成，每个刺都有自己独特的行为模式
                if SCREEN_MAP[y][x]==2 or SCREEN_MAP[y][x]==12:
                    thorn=Thorn(THORN_PATH,self.obs_sprites,(x*38+19,y*30+15),self.all_sprites,[1,2])
                    self.obs_sprites.add(thorn)
                if SCREEN_MAP[y][x]==13:
                    thorn=Thorn(THORN_PATH,self.obs_sprites,(x*38+19,y*30+15),self.all_sprites,[1])
                    self.obs_sprites.add(thorn)
                if SCREEN_MAP[y][x]==4 :
                    thorn=Thorn(THORN_PATH,self.obs_sprites,(x*38+19,y*30+15),self.all_sprites,[])
                    self.obs_sprites.add(thorn)
                if SCREEN_MAP[y][x]==16:
                    thorn=Thorn(THORN_PATH2,self.obs_sprites,(x*38+19,y*30+15),self.all_sprites,[3])
                    self.obs_sprites.add(thorn)
                if SCREEN_MAP[y][x]==6:
                    thorn=Thorn(THORN_PATH2,self.obs_sprites,(x*38+19,y*30+15),self.all_sprites,[])
                    self.obs_sprites.add(thorn)
                if SCREEN_MAP[y][x]==8 :
                    thorn=Thorn(THORN_PATH3,self.obs_sprites,(x*38+19,y*30+15),self.all_sprites,[])
                    self.obs_sprites.add(thorn)
                if SCREEN_MAP[y][x]==9 :
                    thorn=Thorn(THORN_PATH4,self.obs_sprites,(x*38+19,y*30+15),self.all_sprites,[])
                    self.obs_sprites.add(thorn)
                    
                    
                    
                #地图的生成
                if SCREEN_MAP[y][x]==1 or SCREEN_MAP[y][x]==12 or SCREEN_MAP[y][x]==16 or SCREEN_MAP[y][x]==13:
                    wall=Ground(GROUND_PATH,self.obs_sprites,(x*38+19,y*30+15),1,self.all_sprites)
                    self.obs_sprites.add(wall)
                if SCREEN_MAP[y][x]==3:
                    wall=Ground(GROUND_PATH,self.obs_sprites,(x*38+19,y*30+15),3,self.all_sprites)
                    self.obs_sprites.add(wall)
                if SCREEN_MAP[y][x]==5 :
                    wall=Ground(GROUND_PATH3,self.obs_sprites,(x*38+19,y*30+15),1,self.all_sprites)
                    self.obs_sprites.add(wall)
                if SCREEN_MAP[y][x]==7:
                    wall=Ground(THORN_PATH,self.obs_sprites,(x*38+19,y*30+15),7,self.all_sprites)
                    self.obs_sprites.add(wall)
                if SCREEN_MAP[y][x]==10:
                    wall=Bandzi(BANDZI_PATH,self.obs_sprites,(x*38+19,y*30+15),1)
                    self.obs_sprites.add(wall)
                if SCREEN_MAP[y][x]==20:
                    wall=Bandzi(THORN_PATH,self.obs_sprites,(x*38+19,y*30+15),2)
                    self.obs_sprites.add(wall)
                if SCREEN_MAP[y][x]==30:
                    wall=OverSprite(self.all_sprites,(x*38+19,y*30+15),self.all_sprites)
                    self.all_sprites.add(wall)
                if SCREEN_MAP[y][x]==40:
                    wall=cundang(self.obs_sprites,(x*38+19,y*30+15),self.bullet_sprites)
                    self.obs_sprites.add(wall)

                    
    
    # 爆炸函数  
    def boom(self,alive, position):  
        if not alive and  len(self.boom_sprite)<2:   
            for _ in range(50):  # 例如，产生50个粒子  
                vx = random.randint(-10, 10)  
                vy = random.randint(-10, 10)  
                self.boom_sprite.add(Particle(position[0], position[1],(vx, vy),self.boom_sprite))  
            
                
                
                

    def run(self,dt):
        self.is_complete()
        if self.player.alive==False:
            self.alive=False
            self.position=(self.player.rect.x,self.player.rect.y)
            self.player.kill()
        self.boom(self.alive,self.position)
        #角色初始化设置
        self.player.dx=0
        self.player.dy=0
        #键盘事件获取
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if event.type ==pygame.KEYDOWN:
                #玩家行为的获取
                self.player.input_j(event)
                if event.key==pygame.K_LCTRL:
                    if self.player.status=='right' or self.player.status=='right_idle' or self.player.status=='right_up' or self.player.status=='right_updown':
                       bullet=Bullet(self.bullet_sprites,1,self.obs_sprites,(self.player.rect.x+40,self.player.rect.y+40))
                    else:
                        bullet=Bullet(self.bullet_sprites,-1,self.obs_sprites,(self.player.rect.x,self.player.rect.y+40))
                #重置游戏
                if event.key==pygame.K_SPACE:
                    if self.alive==True:
                        self.player.kill()
                    self.all_sprites.add(self.player)
                    
                    self.player.rect.x=cundang.position[0]
                    self.player.rect.y=cundang.position[1]
                    self.player.alive=True
                    self.alive=True
                    self.boom_sprite.empty()
                    self.boom_sprite.add(self.over)
                    for thorn in self.obs_sprites.sprites():
                        if thorn.type==2:
                            thorn.reset()
                        if thorn.type==3:
                            thorn.reset()

                    
                    
        #游戏绘制和更新
        self.display_surface.fill((173,216,230))
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
        self.obs_sprites.draw(self.display_surface)
        self.obs_sprites.update()
        self.bullet_sprites.draw(self.display_surface)
        self.bullet_sprites.update()
        if self.alive==False:
           self.boom_sprite.draw(self.display_surface)
           self.boom_sprite.update()
    
    def is_complete(self):
        for play in self.all_sprites.sprites():
            if play.type==0:
                if play.over==True:
                    self.overl=True
                    
