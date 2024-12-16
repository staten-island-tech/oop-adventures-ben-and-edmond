import pygame 
import random
import time 

pygame.init()
black = (0,0,0)
green = (0,255,0)  
blue = (0,0,255)    
orange = (255,165,0)
white = (255,255,255)
red = (255,0,0)
screen = pygame.display.set_mode([600, 600])
fruits = ["0", "1", "2", "3", "4"]
color = [black, green, red, blue, orange]
font = pygame.font.Font('freesansbold.ttf', 32)
money = 100


class Slots:
    def starting():

        text = font.render('SPACE TO ROLL', True, green)
        slot1 = font.render('', True, black)
        slot2 = font.render('', True, black)
        slot3 = font.render('', True, black)  
        cashText = font.render(f"Money: {money}", True, black)
        textRect = text.get_rect() 
        slot1Rect = slot1.get_rect()
        slot2Rect = slot2.get_rect()
        slot3Rect = slot3.get_rect()
        cashTextRect = cashText.get_rect()
        textRect.center = (300, 500)
        slot1Rect.center = (100, 300)
        slot2Rect.center = (300, 300)
        slot3Rect.center = (500, 300)
        cashTextRect.center = (100, 100)
        return text, slot1, slot2, slot3, cashText, slot1Rect, slot2Rect, slot3Rect, textRect, cashTextRect
    def roll():
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        z = random.randint(0, 4)
        slot1 = font.render(fruits[x], True, color[x])
        slot2 = font.render(fruits[y], True, color[y])
        slot3 = font.render(fruits[z], True, color[z])
        return slot1, slot2, slot3
        if x == y == z:  
            money += bet * 2  
        if x == y or y == z or x == z:
            money += bet * 1.5
        else:
            money -= bet
    def game_loop():
        text, slot1, slot2, slot3, cashText, slot1Rect, slot2Rect, slot3Rect, textRect, cashTextRect = Slots.starting()
        while True:
            screen.fill(white)
            screen.blit(text, textRect)
            screen.blit(slot1, slot1Rect)
            screen.blit(slot2, slot2Rect)
            screen.blit(slot3, slot3Rect)
            screen.blit(cashText, cashTextRect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    slot1, slot2, slot3 = Slots.roll()
            pygame.display.update()
Slots.game_loop()
