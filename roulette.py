import random

red_num = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
black_num = [2.4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
green_num = [37,38]
first_twelve = [1,2,3,4,5,6,7,8,9,10,11,12]
second_twelve = [13,14,15,16,17,18,19,20,21,22,23,24]
third_twelve = [25,26,27,28,29,30,31,32,33,34,35,36]


class roulette:

    def diceroll():
        roll = random.randint(1,38)
        return roll

    def check_color(num):
        if num in red_num:
            return "red"
        if num in black_num:
            return "black"
        if num in green_num:
            return "green"

    def check_twelve(num):
        if num in first_twelve:
            return "first_twelve"
        if num in second_twelve:
            return "second_twelve"
        if num in third_twelve:
            return "third_twelve"

    
    
    def main():
        print("Welcome to addiction!")
        while True:
            bet_input = input("What type of bet would you like to place? (number, color, twelves)\n").lower()
            roulette.diceroll()
            if bet_input == "number":
                roulette.diceroll()                
            elif bet_input == "color":
                while True:
                    color_input = input("Which color would you like to bet on? (green, red, or black)\n").lower()
                    if color_input not in ["red","black","green"]:
                        print("Invalid Color.")
                        continue
                    roulette.check_color()
            elif bet_input == "twelves":
                while True:
                    twelve_input = input("Which twelve would you like to bet on (first, second, third)")
                    if twelve_input not in ["first","second","third"]:
                        print("Invalid Twelve.")
                        continue
            else:
                print ("Invalid bet type entered, Try again.")
                return

roulette.main()
