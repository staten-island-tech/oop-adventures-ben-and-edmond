import pygame 
import random
import time 
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Click and drag to draw")
fruits= ["🍒", "🍊", "🍋", "🍎", "🍉"]
black= (0,0,0)
class slots:
    def starting():
        
    def roll():
        random.shuffle(fruits)

        
slots.starting()
slots.roll()
pygame.display.update()
pygame.quit() 