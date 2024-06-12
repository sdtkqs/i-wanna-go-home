import pygame  
import random
from settings import *
#角色死亡特效
#————————————————————————————————————————————————————————————————————
# 粒子类  
class Particle(pygame.sprite.Sprite):  
    def __init__(self, x, y, velocity,group):  
        super().__init__(group)
        self.velocity = velocity  
        self.image=pygame.image.load(BLOOD_PATH)
        self.rect=self.image.get_rect(center=(x,y))
        self.rect.x=x
        self.rect.y=y
  
    def update(self):  
        self.rect.x += self.velocity[0]  
        self.rect.y += self.velocity[1]  
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH or self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT:    
            self.kill()

class Over(pygame.sprite.Sprite):
    def __init__(self,group):
        super().__init__(group)
        self.image=pygame.image.load(OVER_PATH).convert_alpha()
        self.rect=self.image.get_rect(center=(602,300))
  



