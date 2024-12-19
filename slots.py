import os
import pygame
import random
class Slots:
    pygame.init()

    black = (0, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    orange = (255, 165, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    screen = pygame.display.set_mode([600, 600])
    font = pygame.font.Font('freesansbold.ttf', 32)

    fruits = ["0", "1", "2", "3", "4"]
    color = [black, green, red, blue, orange]
    
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

    def calculate_money(self, x, y, z):
        if x == y == z:
            return self.bet * 2
        elif x == y or y == z or x == z:
            return self.bet * 0.5
        else:
            return -self.bet

    def game_loop(self):
        
        rolling = False
        roll_start_time = 0
        total_roll_time = 200
        roll_count = 0

        text, slot1, slot2, slot3, cashText, slot1Rect, slot2Rect, slot3Rect, textRect, cashTextRect = self.starting()

        while True:
            if self.money >= self.bet:
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
                        profit = self.calculate_money(x, y, z)
                        self.money += profit

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        if not rolling:
                            rolling = True
                            roll_start_time = pygame.time.get_ticks()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

            else:
                game_over_text = self.font.render("GAME OVER", True, self.red)
                game_over_rect = game_over_text.get_rect()
                game_over_rect.center = (300, 300)
                self.screen.fill(self.white)
                self.screen.blit(game_over_text, game_over_rect)
                pygame.display.update()
                pygame.time.wait(3000)
                pygame.quit()
                quit()

            pygame.display.update()


#Slots().game_loop()
