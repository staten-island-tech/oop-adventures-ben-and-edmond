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

    def prompt_bet(self):
        while True:
            try:
                bet_amount = int(input(f"Current balance: ${self.money}. Enter your bet amount: $"))
                if bet_amount > 0 and bet_amount <= self.money:
                    self.bet = bet_amount
                    break
                else:
                    print("Invalid bet amount. Please enter a valid bet.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def starting(self):
        text = self.font.render('SPACE TO ROLL', True, self.green)
        slots = [self.font.render('', True, self.black) for _ in range(3)]
        cashText = self.font.render(f"Money: ${self.money}", True, self.black)
        textRect = text.get_rect()
        slotsRect = [slot.get_rect() for slot in slots]
        cashTextRect = cashText.get_rect()
        
        textRect.center = (300, 500)
        for i, slotRect in enumerate(slotsRect):
            slotRect.center = (100 + i * 200, 300)
        cashTextRect.center = (100, 100)

        return text, slots, cashText, slotsRect, textRect, cashTextRect

    def roll(self):
        slots_result = [random.randint(0, 4) for _ in range(3)]
        slots_rendered = [self.font.render(self.fruits[x], True, self.color[x]) for x in slots_result]
        return slots_rendered, slots_result

    def calculate_money(self, x, y, z):
        if x == y == z:
            return self.bet * 2
        elif x == y or y == z or x == z:
            return self.bet * 0.5
        else:
            return -self.bet

    def game_loop(self):
        self.prompt_bet()
        rolling = False
        roll_start_time = 0
        total_roll_time = 200

        text, slots, cashText, slotsRect, textRect, cashTextRect = self.starting()

        while True:
            if self.money >= self.bet:
                self.screen.fill(self.white)
                self.screen.blit(text, textRect)
                for i, slot in enumerate(slots):
                    self.screen.blit(slot, slotsRect[i])
                cashText = self.font.render(f"Money: ${self.money}", True, self.black)
                self.screen.blit(cashText, cashTextRect)

                if rolling:
                    if pygame.time.get_ticks() - roll_start_time < total_roll_time:
                        slots_rendered, results = self.roll()
                    else:
                        rolling = False
                        profit = self.calculate_money(*results)
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
                        print(f"Your starting balance is ${self.balance}.\n")
                        pygame.quit()
                        quit()

            else:
                game_over_text = self.font.render("GAME OVER", True, self.red)
                game_over_rect = game_over_text.get_rect()
                game_over_rect.center = (300, 300)
                self.screen.fill(self.white)
                self.screen.blit(game_over_text, game_over_rect)
                pygame.display.update()
                pygame.time.wait(2000)
                pygame.quit()
                quit()

            pygame.display.update()

Slots().game_loop()