import random
import os
import time

class roulette:
    red_num = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
    black_num = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
    green_num = [37,38]
    first_twelve = [1,2,3,4,5,6,7,8,9,10,11,12]
    second_twelve = [13,14,15,16,17,18,19,20,21,22,23,24]
    third_twelve = [25,26,27,28,29,30,31,32,33,34,35,36]

    def __init__(self, money):
        self.money = money
        print(f"Your starting balance is ${self.money}.\n")
    def get_money(self):
        return self.money

    @staticmethod
    def diceroll():
        return random.choice(range(1, 39))

    @staticmethod
    def check_color(num):
        if num in roulette.red_num:
            return "red"
        if num in roulette.black_num:
            return "black"
        if num in roulette.green_num:
            return "green"

    @staticmethod
    def check_twelve(num):
        if num in roulette.first_twelve:
            return "first"
        if num in roulette.second_twelve:
            return "second"
        if num in roulette.third_twelve:
            return "third"

    @staticmethod
    def clear():
        if os.name == 'nt':
            os.system('CLS')
        else:
            os.system('clear')

    def continue_input(self):
        global again_input
        while True:
            if self.money == 0:
                print("Unable to continue, You have gone bankrupt.")
                time.sleep(1.5)
                return False
            self.clear()
            again_input = input("Would you like to continue? (y/n)\n").lower()
            if again_input == "y" or again_input == "n":
                break
            else:
                print("Invalid input.")
                time.sleep(.5)
                
        if again_input == "y":
            print("Continuing")
            time.sleep(.5)
            return True
        elif again_input == "n":
            print("Exiting.")
            time.sleep(.5)
            return False

    def get_bet_amount(self):
        while True:
            try:
                print("Welcome to addiction (roulette).\n")
                roulette.clear()
                print(f"Balance: ${self.money}")
                bet_amount = int(input("How much $ would you like to bet?\n"))
                if 0 < bet_amount <= self.money:
                    return bet_amount
                print("Invalid amount. Please enter a value within your balance.")
                time.sleep(1)
                
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                time.sleep(1)

    def get_bet_type(self):
        roulette.clear()
        print(f"Balance: ${self.money}")
        return input("What type of bet would you like to place? (number, color, twelves)\n").lower()

    def process_number_bet(self, result, bet_amount):
        while True:
            try:
                roulette.clear()
                print(f"Balance: ${self.money}")
                num_input = int(input("Which number would you like to bet on? (1-38)\n"))
                if 1 <= num_input <= 38:
                    if num_input == result:
                        self.money += bet_amount * 9
                        print(f"The wheel rolled {result}. You won ${bet_amount * 9}!")
                    else:
                        self.money -= bet_amount
                        print(f"The wheel rolled {result}. You lost ${bet_amount}.")
                    return
                print("Invalid number. Please choose a number between 1 and 38.")
                time.sleep(1)
            except ValueError:
                print("Invalid input. Please enter a number.")
                time.sleep(1)

    def process_color_bet(self, result, bet_amount):
        while True:
            roulette.clear()
            print(f"Balance: ${self.money}")
            color_input = input("Which color would you like to bet on? (green, red, or black)\n").lower()
            if color_input in ["red", "black", "green"]:
                if roulette.check_color(result) == color_input:
                    if color_input == "green":
                        self.money += bet_amount * 5
                        print(f"The wheel rolled {result}. You won ${bet_amount * 5}!")
                    else:
                        self.money += bet_amount
                        print(f"The wheel rolled {result}. You won ${bet_amount}!")
                else:
                    self.money -= bet_amount
                    print(f"The wheel rolled {result}. You lost ${bet_amount}.")
                return
            print("Invalid color. Please choose red, black, or green.")
            time.sleep(1)

    def process_twelve_bet(self, result, bet_amount):
        while True:
            roulette.clear()
            print(f"Balance: ${self.money}")
            twelve_input = input("Which twelve would you like to bet on? (first, second, third)\n").lower()
            if twelve_input in ["first", "second", "third"]:
                if roulette.check_twelve(result) == twelve_input:
                    self.money += bet_amount * 2
                    print(f"The wheel rolled {result}. You won ${bet_amount * 2}!")
                else:
                    self.money -= bet_amount
                    print(f"The wheel rolled {result}. You lost ${bet_amount}.")
                return
            print("Invalid input. Please choose first, second, or third.")
            time.sleep(1)

    def start(self):
        print("Welcome to addiction (roulette).")
        time.sleep(1)
        while self.continue_input() == True:

            result = roulette.diceroll()
            bet_amount = self.get_bet_amount()
            bet_type = self.get_bet_type()

            if bet_type == "number":
                self.process_number_bet(result, bet_amount)
                time.sleep(1)
            elif bet_type == "color":
                self.process_color_bet(result, bet_amount)
                time.sleep(1)
            elif bet_type == "twelves":
                self.process_twelve_bet(result, bet_amount)
                time.sleep(1)
            else:
                print("Invalid bet type. Try again.")
                time.sleep(1)