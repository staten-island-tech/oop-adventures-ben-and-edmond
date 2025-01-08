import random
import os
class roulette:
    red_num = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
    black_num = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
    green_num = [37,38]
    first_twelve = [1,2,3,4,5,6,7,8,9,10,11,12]
    second_twelve = [13,14,15,16,17,18,19,20,21,22,23,24]
    third_twelve = [25,26,27,28,29,30,31,32,33,34,35,36]
    def __init__(self, money):
        self.money=money
        print(f"Your starting balance is ${self.money}.\n")

    def get_money(self):
        return self.money
    
    def diceroll():
        roll=list(range(1,39))
        result=random.choice(roll)
        return result


    def check_color(num):
        if num in roulette.red_num:
            return "red"
        if num in roulette.black_num:
            return "black"
        if num in roulette.green_num:
            return "green"


    def check_twelve(num):
        if num in roulette.first_twelve:
            return "first_twelve"
        if num in roulette.second_twelve:
            return "second_twelve"
        if num in roulette.third_twelve:
            return "third_twelve"


    def clear():
        if os.name == 'nt':
            os.system('CLS')  

    def start(self):
        print("Welcome to addiction (roulette).")
        while True:
            result = roulette.diceroll()
            if self.money == 0:
                print("You are bankrupt.")
                break
            print(f"Balance: $",self.money)
            try:
                exit_input = input("Would you like to continue? (y)\n").lower()
                if exit_input == "y":
                    print("Continuing.")
                else:
                    print("Exiting.")
                    break
            except ValueError:
                print("Invalid")
            while True:
                    try:
                        roulette.clear()
                        print(f"Balance: $",self.money)
                        bet_amount_input = int(input("How much $ would you like to bet?\n"))
                   
                        if bet_amount_input <= self.money:
                           break
                        elif bet_amount_input > self.money:
                            print("You do not have enough $")
                        else:
                            print("Invalid Bet.")
                    except:
                        print("Invalid input. Please enter a valid number.")


            roulette.clear()
            print(f"Balance: $",self.money)
            bet_type_input = input("What type of bet would you like to place? (number, color, twelves)\n").lower()
            if bet_type_input == "number":
                while True:
                    roulette.clear()
                    print(f"Balance: $",self.money)
                    num_input = int(input("Which number would you like to bet on? (1-38)\n"))
                    if num_input not in list(range(1,39)):
                        roulette.clear()
                        print(f"Balance: $",self.money)
                        print("Invalid Number.")
                    elif num_input == result:
                        roulette.clear()
                        print(f"Balance: $",self.money)
                        self.money = self.money+bet_amount_input*9
                        print(f"The wheel rolled",result)
                        print(f"You won $",bet_amount_input*9)
                        break
                    else:
                        roulette.clear()
                        print(f"Balance: $",self.money)
                        self.money = self.money-bet_amount_input
                        print(f"The wheel rolled",result)
                        print(f"You lost $",bet_amount_input)
                        break
            elif bet_type_input == "color":
                while True:
                    roulette.clear()
                    print(f"Balance: $",self.money)
                    color_input = input("Which color would you like to bet on? (green, red, or black)\n").lower()
                    if color_input not in ["red","black","green"]:
                        roulette.clear()
                        print(f"Balance: $",self.money)
                        print("Invalid Color.")
                    elif roulette.check_color(result) == color_input:
                        if color_input == "green":
                            roulette.clear()
                            print(f"Balance: $",self.money)
                            self.money = self.money+bet_amount_input*5
                            print(f"The wheel rolled",result)
                            print(f"You won $",bet_amount_input*5)
                            break
                        else:
                            roulette.clear()
                            print(f"Balance: $",self.money)
                            self.money = self.money+bet_amount_input
                            print(f"The wheel rolled",result)
                            print(f"You won $",bet_amount_input)
                            break
                    else:
                        roulette.clear()
                        print(f"Balance: $",self.money)
                        self.money = self.money-bet_amount_input
                        print(f"The wheel rolled",result)
                        print(f"You lost $",bet_amount_input)
                        break
            elif bet_type_input == "twelves":
                while True:
                    roulette.clear()
                    print(f"Balance: $",self.money)
                    twelve_input = input("Which twelve would you like to bet on (first, second, third)\n")
                    if twelve_input not in ["first","second","third"]:
                        roulette.clear()
                        print(f"Balance: $",self.money)
                        print("Invalid Twelve.")
                    if roulette.check_twelve(result) == twelve_input:
                        roulette.clear()
                        print(f"Balance: $",self.money)
                        self.money = self.money+bet_amount_input*2
                        print(f"The wheel rolled",result)
                        print(f"You won $",bet_amount_input*2)
                        break
                    else:
                        roulette.clear()
                        print(f"Balance: $",self.money)
                        self.money = self.money-bet_amount_input
                        print(f"The wheel rolled",result)
                        print(f"You lost $",bet_amount_input)
                        break
            else:
                roulette.clear()
                print(f"Balance: $",self.money)
                print ("Invalid bet.")
                return