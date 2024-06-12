import pygame
from settings import *




class Bandzi(pygame.sprite.Sprite):
    def __init__(self, ground_path,group,pos,type):  
        super().__init__(group)  # 调用父类（Sprite）的构造函数  
  
        # 加载图像并设置精灵的图像和矩形  
        self.image = pygame.image.load(ground_path).convert_alpha()  
        self.image=pygame.transform.scale(self.image, (38, 30))
        self.rect = self.image.get_rect(center=pos)  # 假设图像是一个正方形，其矩形将与其大小相同
        self.type=type
        self.direction = 1  # 1表示向右，-1表示向左，
        self.speed=1
        # 矩形边界  
        self.boundary_rect = pygame.Rect(100, 100, 200, 300)  
    
    def update(self):
        if self.type==1:
            self.rect.move_ip(self.speed * self.direction, 0)  
  
        # 如果碰到屏幕边缘，则反转方向  
            if self.rect.left < 100:  
                self.rect.left = 100  
                self.direction = 1  
            elif self.rect.right > 300:  
                self.rect.right = 300  
                self.direction = -1  
        if self.type==2:
            self.rect.move_ip(0, -self.speed)  
  
        # 如果碰到屏幕顶部或底部，则反转方向（但在这个例子中我们只需要检查顶部）  
            if self.rect.bottom <= 0:  
                self.rect.top = SCREEN_HEIGHT   # 回到屏幕底部
    
    def reset(self):
        pass


class OverSprite(pygame.sprite.Sprite):  
    def __init__(self,group,pos,player):  
        super().__init__(group)  
        self.images = [pygame.image.load(LAY_PATH).convert_alpha(),  
                       pygame.image.load(LAY_PATH2).convert_alpha()]  
        self.image = self.images[0]  # 初始化为第一张图片  
        self.rect = self.image.get_rect(center=pos)  # 精灵的矩形位置  
        self.index = 0  # 用来追踪当前显示的图片索引  
        self.frame_clock = 0  # 计时器，用于切换图片  
        self.frame_rate = 500  # 切换图片的频率，单位是毫秒  
        self.type=0
        self.frame_index = 0
        self.over=False
        self.player=player
  
    def update(self, dt):  
        # dt 是自上次调用 update 以来经过的时间（毫秒）  
        self.frame_index += 4 * dt
        if self.frame_index >= 2:
            self.frame_index = 0
        self.image=self.images[int(self.frame_index)]
        for play in self.player:
            if play.type==2:
                    if play.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height):
                        self.over=True
    
class cundang(pygame.sprite.Sprite):  
    position=(100,550)
    def __init__(self,group,pos,bullet):  
        super().__init__(group)  
        self.images = [pygame.image.load(CUN_PATH1).convert_alpha(),  
                       pygame.image.load(CUN_PATH2).convert_alpha()]  
        self.image = self.images[0]  # 初始化为第一张图片  
        self.image=pygame.transform.scale(self.image, (38, 40))
        self.rect = self.image.get_rect(center=pos)  # 精灵的矩形位置  
        self.type=10
        self.bullet=bullet
    
    def update(self):
        for bullet in self.bullet:
            if self.rect.colliderect(bullet):
                self.image=self.images[1]
                self.image=pygame.transform.scale(self.image, (38, 40))
                cundang.position=(self.rect.x,self.rect.y-50)
            else:
                self.image=self.images[0]
                self.image=pygame.transform.scale(self.image, (38, 40))
                
    def reset(self):
        pass