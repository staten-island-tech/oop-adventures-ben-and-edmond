import pygame 
import random
import time 

pygame.init()
black = (0,0,0)
green = (0,255,0)  
white = (255,255,255)
red = (255,0,0)
screen = pygame.display.set_mode([600, 600])
fruits = ["0", "1", "2", "3", "4"]
color = 
font = pygame.font.Font('freesansbold.ttf', 32)


class Slots:
    def starting():  
        text = font.render('SPACE TO ROLL', True, green)
        slot1 = font.render('', True, green)
        slot2 = font.render('', True, green)
        slot3 = font.render('', True, green)  
        textRect = text.get_rect() 
        slot1Rect = slot1.get_rect()
        slot2Rect = slot2.get_rect()
        slot3Rect = slot3.get_rect()
        textRect.center = (300, 500)
        slot1Rect.center = (100, 300)
        slot2Rect.center = (300, 300)
        slot3Rect.center = (500, 300)
        return text, slot1, slot2, slot3, slot1Rect, slot2Rect, slot3Rect, textRect
    def roll():
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        z = random.randint(0, 4)
        slot1 = font.render(fruits[x], True, green)
        slot2 = font.render(fruits[y], True, green)
        slot3 = font.render(fruits[z], True, green)
        return slot1, slot2, slot3
    def game_loop():
        text, slot1, slot2, slot3, slot1Rect, slot2Rect, slot3Rect, textRect = Slots.starting()
        while True:
            screen.fill(white)
            screen.blit(text, textRect)
            screen.blit(slot1, slot1Rect)
            screen.blit(slot2, slot2Rect)
            screen.blit(slot3, slot3Rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    slot1, slot2, slot3 = Slots.roll()
            pygame.display.update()
Slots.game_loop()
