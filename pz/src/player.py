import pygame
import sys
from settings import *
from support import *

#角色类
#——————————————————————————————————————————————————————————————————

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group,obs):
        super().__init__(group)
        self.animations=import_assets()#获取图片路径
        self.status = 'right'#玩家状态
        self.frame_index = 0#玩家同一状态的不同图片
        # 获取kid的图片和矩形
        self.image= self.animations[self.status][self.frame_index]
        self.mask = pygame.mask.from_surface(self.image)
        #self.image=pygame.transform.scale(self.image, (48, 64))
        self.rect = self.image.get_rect(center = pos)
        
        self.type=2
        self.obs=obs#碰撞组

        # 玩家移动参数
        self.direction=0#判断左右移动
        self.speed = LR_SPEED
        self.on_ground=False #检测玩家是否在地上
        self.diff=0  #y方向速度，正数为下
        self.jumps_left = JUMP_COUNT  # 剩余的跳跃次数（默认有两次跳跃）
        self.gravity=GRAVITY  #重力加速度
        
        self.alive=True
        self.display_surface = pygame.display.get_surface()
        
        self.dy=0
        self.dx=0
    
    #跳跃
    def jump(self):  
        if self.jumps_left > 0:  # 确保玩家在地面上且还有剩余跳跃次数  
            self.diff = -JUMP_SPEED  
            self.jumps_left -= 1  # 使用一次跳跃后减少剩余次数  
    
    #重力逻辑
    def use_gravity(self):  
        self.diff += self.gravity
        if self.diff>10:
            self.diff=10
        if self.on_ground==True and self.diff>0:
            pass
        else:
            self.dy+=self.diff
        
        
        
    #角色动态效果
    def animate(self,dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]
    
    #键盘事件
    def input_j(self,event):
        if event.key==pygame.K_LSHIFT:
            self.jump()

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction = 1
            self.dx+=self.speed
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction = -1
            self.dx+=self.speed
            self.status = 'left'
        else:
            self.direction = 0
    
    #当人物站立不动时，应该为待机状态
    def get_status(self):
        
        if self.direction == 0:
            self.status = self.status.split('_')[0] + '_idle'
        if not self.on_ground:
            if self.dy<0:
               self.status = self.status.split('_')[0] + '_up'
            else:
               self.status = self.status.split('_')[0] + '_updown'

    
    #移动
    def move(self):
        self.rect.x += self.direction *self.dx
        self.rect.y += self.dy
    
    #角色碰撞机制
    def obs_f(self):
        self.on_ground=False
        for ground in self.obs:
            if ground.type==1:
               if ground.rect.colliderect(self.rect.x + self.direction * self.speed+10, self.rect.y+21, self.rect.width-20, self.rect.height-21):
                   self.dx=0
               if ground.rect.colliderect(self.rect.x+13, self.rect.y+21 + self.dy, self.rect.width-26, self.rect.height-21):
                    if self.dy < 0:
                        self.dy = ground.rect.bottom - (self.rect.top+21)
                        self.diff = 0
                    elif self.dy > 0:
                        self.dy = ground.rect.top - self.rect.bottom
                        self.diff= 0
                        self.on_ground=True
                        self.jumps_left=JUMP_COUNT
               if ground.rect.colliderect(self.rect.x+13, self.rect.y+21+1, self.rect.width-26, self.rect.height-21):
                  self.on_ground=True
            if ground.type==2:
               obs_sprites = pygame.sprite.Group()
               obs_sprites.add(ground)
               if pygame.sprite.spritecollideany(self, obs_sprites, collided=pygame.sprite.collide_mask):  
                  self.alive=False
                
        if self.rect.top>SCREEN_HEIGHT:
            self.alive=False
                  
    


    #角色运行和更新
    def update(self, dt):
        #self.dy=0
        #self.dx=0
        self.use_gravity()
        self.input()
        self.get_status()
        self.obs_f()
        self.move()
        self.animate(dt)
