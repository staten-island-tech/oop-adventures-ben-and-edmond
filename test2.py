import random
import os

class Roulette:
    red_num = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    black_num = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    green_num = [37, 38]

    def __init__(self, money):
        self.money = money

    def diceroll(self):
        return random.choice(range(1, 39))

    def check_color(self, num):
        if num in self.red_num:
            return "red"
        if num in self.black_num:
            return "black"
        if num in self.green_num:
            return "green"

    def main(self):
        print("Welcome to Roulette!")
        while True:
            print(f"Balance: ${self.money}")
            try:
                bet = int(input("Enter your bet (or 0 to quit): "))
                if bet == 0:
                    return self.money
                if bet > self.money or bet <= 0:
                    print("Invalid bet amount!")
                    continue

                bet_type = input("Bet type (number/color): ").lower()
                result = self.diceroll()

                if bet_type == "number":
                    num = int(input("Choose a number (1-38): "))
                    if num == result:
                        print(f"You won! The number was {result}.")
                        self.money += bet * 9
                    else:
                        print(f"You lost! The number was {result}.")
                        self.money -= bet

                elif bet_type == "color":
                    color = input("Choose a color (red/black/green): ").lower()
                    if self.check_color(result) == color:
                        print(f"You won! The number was {result} ({color}).")
                        self.money += bet
                    else:
                        print(f"You lost! The number was {result} ({self.check_color(result)}).")
                        self.money -= bet

                else:
                    print("Invalid bet type!")

            except ValueError:
                print("Invalid input!")
Roulette.main()