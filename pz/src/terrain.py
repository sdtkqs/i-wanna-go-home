from typing import Any
import pygame
from settings import *
#游戏内障碍物的类
#——————————————————————————————————————————————————————————————————————————————————
#草块
class Ground(pygame.sprite.Sprite):  
    def __init__(self, ground_path,group,pos,type,player):  
        super().__init__(group)  # 调用父类（Sprite）的构造函数  
  
        # 加载图像并设置精灵的图像和矩形  
        self.image = pygame.image.load(ground_path).convert_alpha()  
        self.image=pygame.transform.scale(self.image, (38, 30))
        self.rect = self.image.get_rect(center=pos)  # 假设图像是一个正方形，其矩形将与其大小相同  
        self.type=type
        self.player=player
    def update(self):
        if self.type==3:
            for play in self.player:
                    if play.rect.colliderect(self.rect.x+10, self.rect.y, self.rect.width-20, self.rect.height):
                       self.image=pygame.image.load(GROUND_PATH2).convert_alpha()
                       
    def reset(self):
        self.image=pygame.image.load(GROUND_PATH).convert_alpha()

#刺
class Thorn(pygame.sprite.Sprite):
    def __init__(self, ground_path,group,pos,player,mode_list):  
        super().__init__(group)  # 调用父类（Sprite）的构造函数  
  
        # 加载图像并设置精灵的图像和矩形  
        self.image = pygame.image.load(ground_path).convert_alpha()  
        self.image=pygame.transform.scale(self.image, (38, 30))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=pos)  # 假设图像是一个正方形，其矩形将与其大小相同
        self.type=2
        self.mode=mode_list
        self.player=player
        self.re_mode=[]
    
    def update(self):
        if len(self.mode)>0:
            if self.mode[0]==1:
                for play in self.player:
                    if play.rect.colliderect(self.rect.x+5, self.rect.y-50, self.rect.width-10, self.rect.height):
                       self.rect.y-=30
                       self.re_mode.append(self.mode[0])
                       self.mode.remove(self.mode[0])
        if len(self.mode)>0:
            if self.mode[0]==2:
                for play in self.player:
                    if play.rect.colliderect(self.rect.x+10, self.rect.y-240, self.rect.width-20, self.rect.height+30):
                       i=270
                       self.image=pygame.transform.scale(self.image, (38,i ))
                       self.rect.y-=240
                       self.mask=pygame.mask.from_surface(self.image)
                       self.re_mode.append(self.mode[0])
                       self.mode.remove(self.mode[0])
        if len(self.mode)>0:
            if self.mode[0]==3:
                for play in self.player:
                    if play.rect.colliderect(self.rect.x+10, self.rect.y+20, self.rect.width-20, self.rect.height):
                       self.rect.y+=30
                       self.re_mode.append(self.mode[0])
                       self.mode.remove(self.mode[0])
    
    def reset(self):
        self.re_mode.reverse()
        for mode in self.re_mode:
            if mode==1:
                self.rect.y+=30
                #self.re_mode.remove(mode)
                self.mode.insert(0,mode)
            if mode==2:
                self.image=pygame.transform.scale(self.image, (38, 30))
                self.rect.y+=240
                self.mask=pygame.mask.from_surface(self.image)
                #self.re_mode.remove(mode)
                self.mode.insert(0,mode)
            if mode==3:
                self.rect.y-=30
                #self.re_mode.remove(mode)
                self.mode.insert(0,mode)
        self.re_mode.clear()
        

class Bullet(pygame.sprite.Sprite):
    def __init__(self,group,type,obs,pos):
        super().__init__(group)
        self.image=pygame.image.load(BULLET_PATH)
        self.rect=self.image.get_rect(center=pos)
        self.obs=obs
        self.type=type
    
    def update(self):

        if self.type==1:
            self.rect.x+=5
        else:
            self.rect.x-=5
        for obs in self.obs:
            if obs.rect.colliderect(self):
                self.kill()
        if self.rect.x<0 or self.rect.x>SCREEN_WIDTH:
            self.kill()
                
        
        
        
                  
                  
                
            
    
  
 
    
    
    
    