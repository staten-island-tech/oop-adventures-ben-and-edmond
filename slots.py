import pygame
import random
import time

class Slots:
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
    bet = 10

    def starting(self):
        text = self.font.render('SPACE TO ROLL', True, self.green)
        slot1 = self.font.render('', True, self.black)
        slot2 = self.font.render('', True, self.black)
        slot3 = self.font.render('', True, self.black)  
        cashText = self.font.render(f"Money: ${self.money}", True, self.black)
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
    
    def roll(self):
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        z = random.randint(0, 4)
        slot1 = self.font.render(self.fruits[x], True, self.color[x])
        slot2 = self.font.render(self.fruits[y], True, self.color[y])
        slot3 = self.font.render(self.fruits[z], True, self.color[z])
        return slot1, slot2, slot3, x, y, z

    def game_loop(self):
        rolling = False
        roll_start_time = 0
        total_roll_time = 300
        roll_count = 0
    def no_money(self):

        text, slot1, slot2, slot3, cashText, slot1Rect, slot2Rect, slot3Rect, textRect, cashTextRect = self.starting()

        while True:
            if self.money>=self.bet:
                self.screen.fill(self.white)
                self.screen.blit(text, textRect)
                self.screen.blit(slot1, slot1Rect)
                self.screen.blit(slot2, slot2Rect)
                self.screen.blit(slot3, slot3Rect)
                cashText = self.font.render(f"Money: ${self.money}", True, self.black)
                self.screen.blit(cashText, cashTextRect)

                if rolling:
                    if pygame.time.get_ticks() - roll_start_time < total_roll_time:
                        slot1, slot2, slot3, x, y, z = self.roll()
                    else:
                        rolling = False
                        if x == y == z:  
                            self.money += self.bet * 2  
                        elif x == y or y == z or x == z:
                            self.money += self.bet * 0.5
                        else:
                            self.money -= self.bet
                        roll_count += 1
                        if roll_count >= 10:
                            rolling = False
                            roll_count = 0

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        if not rolling:
                            rolling = True
                            roll_start_time = pygame.time.get_ticks()
            else: 
            pygame.display.update()

game = Slots()
game.game_loop()
