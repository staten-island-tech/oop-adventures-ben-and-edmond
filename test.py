import pygame
import random
import time

pygame.init()

black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)
white = (255, 255, 255)
red = (255, 0, 0)
screen = pygame.display.set_mode([600, 600])

fruits = ["0", "1", "2", "3", "4"]
color = [black, green, red, blue, orange]
font = pygame.font.Font('freesansbold.ttf', 32)

money = 100
bet = 0

class Slots:
    def starting():
        global bet
        text = font.render('SPACE TO ROLL', True, green)
        slot1 = font.render('', True, black)
        slot2 = font.render('', True, black)
        slot3 = font.render('', True, black)  
        cashText = font.render(f"Money: ${money}", True, black)
        betText = font.render(f"Bet: ${bet}", True, black)
        betInputText = font.render('Enter Bet:', True, black)
        textRect = text.get_rect() 
        slot1Rect = slot1.get_rect()
        slot2Rect = slot2.get_rect()
        slot3Rect = slot3.get_rect()
        cashTextRect = cashText.get_rect()
        betTextRect = betText.get_rect()
        betInputTextRect = betInputText.get_rect()
        textRect.center = (300, 500)
        slot1Rect.center = (100, 300)
        slot2Rect.center = (300, 300)
        slot3Rect.center = (500, 300)
        cashTextRect.center = (100, 100)
        betTextRect.center = (300, 100)
        betInputTextRect.center = (300, 150)
        return text, slot1, slot2, slot3, cashText, slot1Rect, slot2Rect, slot3Rect, textRect, cashTextRect, betText, betTextRect, betInputText, betInputTextRect

    def roll():
        global money, bet
        if bet > money:
            return None
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        z = random.randint(0, 4)
        slot1 = font.render(fruits[x], True, color[x])
        slot2 = font.render(fruits[y], True, color[y])
        slot3 = font.render(fruits[z], True, color[z])
        if x == y == z:  
            money += bet * 2  
        if x == y or y == z or x == z:
            money += bet * 1.5
        else:
            money -= bet
        bet = 0
        return slot1, slot2, slot3

    def game_loop():
        global bet
        user_input = ''
        input_rect = pygame.Rect(200, 150, 140, 32)
        color_active = pygame.Color('lightskyblue3')
        color_inactive = pygame.Color('chartreuse4')
        color = color_inactive
        active = False
        text, slot1, slot2, slot3, cashText, slot1Rect, slot2Rect, slot3Rect, textRect, cashTextRect, betText, betTextRect, betInputText, betInputTextRect = Slots.starting()
        while True:
            screen.fill(white)
            screen.blit(text, textRect)
            screen.blit(slot1, slot1Rect)
            screen.blit(slot2, slot2Rect)
            screen.blit(slot3, slot3Rect)
            screen.blit(cashText, cashTextRect)
            screen.blit(betText, betTextRect)
            screen.blit(betInputText, betInputTextRect)
            pygame.draw.rect(screen, color, input_rect, 2)
            bet_surface = font.render(user_input, True, black)
            screen.blit(bet_surface, (input_rect.x + 5, input_rect.y + 5))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                        color = color_active
                    else:
                        active = False
                        color = color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_BACKSPACE:
                            user_input = user_input[:-1]
                        elif event.key == pygame.K_RETURN:
                            if user_input.isdigit():
                                bet = int(user_input)
                                user_input = ''
                            else:
                                user_input = 'Invalid Bet'
                        else:
                            user_input += event.unicode
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if bet > 0:
                        slot1, slot2, slot3 = Slots.roll()
                    else:
                        bet = 0
            pygame.display.update()

Slots.game_loop()
