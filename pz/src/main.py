import pygame, sys
from settings import *
from level import Level
from start import StartScreen
from Level2 import Level2


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))  
        pygame.display.set_caption('I wanna go home and sleep')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.level2=Level2()

    def run(self):
        while True:
            dt = self.clock.tick(120) / 1000
            if self.level.overl==False:
               self.level.run(dt)
            else:
                self.level2.run(dt)
            pygame.display.flip()


#进入游戏的开始界面
def run_game():  
    start_screen = StartScreen( "Start game")
    running = True  
    start_screen.draw() 
    while running:  
    # 处理事件  
        for event in pygame.event.get():  
           start_screen.update(event)  
           if start_screen.game_has_started():   
               return True  


if __name__ == '__main__':
    
    if run_game(): 
       game = Game()
       game.run()


  