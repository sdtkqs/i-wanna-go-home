import pygame  
from settings import *
  
class StartScreen:  
    def __init__(self, caption): 
        pygame.init()  
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.font = pygame.font.Font(None, 50)  # 使用系统默认字体  
        self.caption=self.font.render(caption, True, (0, 0, 0))
        self.play_button_rect = self.caption.get_rect()# 假设的“开始游戏”按钮位置  
        self.play_button_rect.center=(600,600)
        self.rect_surface=pygame.Surface((400,100))
        self.rect_surface.fill((123,136,0))
        self.game_started = False  
        self.title=pygame.image.load(WORLD_PATH2).convert_alpha()
        self.background_image = pygame.image.load(WORLD_PATH1)
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
  
    def draw(self):  
        # 填充背景颜色  
        
        self.screen.blit(self.background_image, (0, 0)) 
        
  
        # 绘制标题或其他文本  
        self.screen.blit(self.title, (250, 100))
        self.screen.blit(self.rect_surface,(400,550))
        # 绘制“开始游戏”按钮（这里只是用矩形代替）  
        self.screen.blit(self.caption,self.play_button_rect)
  
        # 更新屏幕显示  
        pygame.display.flip()  
  
    def update(self, event):  
            if event.type == pygame.QUIT:  
                pygame.quit()  
                exit()  
            elif event.type == pygame.MOUSEBUTTONDOWN:  
                # 检查鼠标点击是否在“开始游戏”按钮内  
                if self.play_button_rect.collidepoint(pygame.mouse.get_pos()):  
                    self.game_started = True  
  
    def game_has_started(self):  
        return self.game_started  
  

  