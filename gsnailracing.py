import random
import os 
import time

class snail:
    @staticmethod
    def roll():
        result = random.randint(1,5)
        return result

    def __init__(self, rows, cols, money):
        self.money=money
        self.cols = cols
        self.rows = rows
        self.map = self.create_track()
        self.horse1_pos = [0,0]
        self.horse2_pos = [1,0]
        self.horse3_pos = [2,0]
        self.horse4_pos = [3,0]
        self.horse5_pos = [4,0]
        self.top_left = "┌"
        self.top_right = "┐"
        self.bottom_left = "└"
        self.bottom_right = "┘"
        self.horizontal_border = "-" * (self.cols + 5)
        print(f"Your starting balance is ${self.money}.\n")
    
    @staticmethod
    def clear():
        if os.name == 'nt':
            os.system('CLS')

    def create_track(self):
        track_layout = []
        for i in range(self.rows):
            row = ["-"] * self.cols
            track_layout.append(row)
        return track_layout
    
    def display_map(self):
        self.clear()
        self.map = self.create_track()
        x1, y1 = self.horse1_pos
        self.map[x1][y1] = "🔴🐌"
        x2, y2 = self.horse2_pos
        self.map[x2][y2] = "🔵🐌"
        x3, y3 = self.horse3_pos
        self.map[x3][y3] = "🟢🐌"
        x4, y4 = self.horse4_pos
        self.map[x4][y4] = "🟡🐌"
        x5, y5 = self.horse5_pos
        self.map[x5][y5] = "🟠🐌"
        print(self.top_left + self.horizontal_border + self.top_right)
        welcome_line = "Welcome to Snail Racing!"
        print("| " + welcome_line.ljust(self.cols + 4) + "|")
        money_line = f"You have $ {self.money}"
        print("| " + money_line.ljust(self.cols + 4) + "|")
        print("|" + " " * (self.cols + 5) + "|")
    
        for row in self.map:
            print("| " + "".join(row).ljust(self.cols) + " |")
    
        print("|" + " " * (self.cols + 5) + "|")
    
        print(self.bottom_left + self.horizontal_border + self.bottom_right)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def get_money(self):
        return self.money
    def continue_input(self):
        global again_input
        while True:
            if self.money == 0:
                print("Unable to continue, You have gone bankrupt.")
                time.sleep(1.5)
                return False
            self.clear()
            self.display_map()
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

    def bet_inputs(self):
        while True:
            try:
                self.display_map()
                print(f"Your current balance is $", self.money,"\n")
                global amount_input
                amount_input = int(input("How much $ would you like to bet?\n"))
                if amount_input > self.money:
                    print("Bet is larger than current balance, Try again.")
                    time.sleep(.75)
                    self.clear()
                elif amount_input <= 0:
                    print("Invalid bet Amount.")
                    time.sleep(.75)
                    self.clear()
                else:
                    self.clear()
                    break
            except:
                print("Invalid Bet.")
                time.sleep(.75)
            
        while True:
                self.display_map()
                global color_input
                color_input = input(f"Which snail would you like to bet on? ([r]ed, [b]lue, [g]reen, [y]ellow, [o]range)\n").lower()
                if color_input not in ["r","b","g","y","o"]:
                    print("Invalid bet type.")
                    time.sleep(1)
                elif color_input == "r":
                    print("You have bet on Red.")
                    time.sleep(1)
                    break
                elif color_input == "b":
                    print("You have bet on Blue.")
                    time.sleep(1)
                    break
                elif color_input == "g":
                    print("You have bet on Green.")
                    time.sleep(1)
                    break
                elif color_input == "y":
                    print("You have bet on Yellow.")
                    time.sleep(1)
                    break
                elif color_input == "o":
                    print("You have bet on Orange.")
                    time.sleep(1)
                    break

    def payout(self):

        if color_input == self.check_win():
            self.money = self.money + amount_input*1.5
            print(f"You won $",amount_input*1.5)
        else:
            self.money = self.money - amount_input
            print(f"You lost $",amount_input)
            


    def check_win(self):
        
        if self.horse1_pos[1] == 24:
            self.clear()
            self.display_map()
            print("The Red Snail has won the race!")
            return "r"
        if self.horse2_pos[1] == 24:
            print("The Blue Snail has won the race!")
            self.clear()
            self.display_map()
            return "b"
        if self.horse3_pos[1] == 24:
            self.clear()
            self.display_map()
            print("The Green Snail has won the race!")
            return "g"
        if self.horse4_pos[1] == 24:
            self.clear()
            self.display_map()
            print("The Yellow Snail has won the race!")
            return "y"
        if self.horse5_pos[1] == 24:
            self.clear()
            self.display_map()
            print("The Orange Snail has won the race!")
            return "o"
        else:
            return False
    
    def reset_positions(self):
        self.horse1_pos = [0, 0]
        self.horse2_pos = [1, 0]
        self.horse3_pos = [2, 0]
        self.horse4_pos = [3, 0]
        self.horse5_pos = [4, 0]

    
    def move_horses(self):
        roll_result = self.roll()
        if roll_result == 1:
            self.horse1_pos[1] += 1
        elif roll_result == 2:
            self.horse2_pos[1] += 1
        elif roll_result == 3:
            self.horse3_pos[1] += 1
        elif roll_result == 4:
            self.horse4_pos[1] += 1
        elif roll_result == 5:
            self.horse5_pos[1] += 1
            
    def start(self):
        
        while self.continue_input() == True:
            self.reset_positions()
            self.clear()
            self.bet_inputs()

            while self.check_win() == False:
                time.sleep(0.1)
                self.clear()
                self.display_map()
                self.move_horses()
                self.check_win()
                if self.check_win() != False:
                    time.sleep(1)
        
            self.payout()
            time.sleep(1)
            break