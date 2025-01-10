import random
import os 
import time

class horse:
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
        print("+" + "-" * 31 + "+")
        welcome_line = "Welcome to Snail Racing!"
        print("| "+ " " + welcome_line.ljust(29) + "|")
        money_line = f"You have $ {self.money}"
        print("| "+ " " + money_line.ljust(29) + "|")
        print("|" + " " * 29 + " ","|")
        for row in self.map:
            print("|" + " " + "".join(row).ljust(28) + "|")
        print("|" + " " * 29 + " ","|")
        print("+" + "-" * 31 + "+")

        # self.map[x1][y1] = "-"

    # def check_win()
    #     if self.horse1_pos[1] == 75
    #     print("")
    #     if self.horse2_pos[1] == 75
    #     print("")
    #     if self.horse3_pos[1] == 75
    #     print("")
    #     if self.horse4_pos[1] == 75
    #     print("")
    #     if self.horse5_pos[1] == 75
    #     print("")sdfsdf



    def bet_inputs(self):
        while True:
            try:
                amount_input = int(input("How much $ would you like to bet?"))
                if amount_input > self.money:
                    print("Bet is larger than current balance, Try again.")
                elif amount_input == 0:
                    print("Invalid bet Amount")
                else:
                    break
            except:
                print("Invalid Bet.")
        while True:
                cash_input = input(f"Which snail would you like to bet on? ([r]ed, [b]lue, [g]reen, [y]ellow, [o]range)\n").lower()
                if cash_input not in ["r","b","g","y","o"]:
                    print("Invalid bet type.")
                # elif cash_input == "r":
                    
                # elif cash_input == "b":

                # elif cash_input == "g":

                # elif cash_input == "y":

                # elif cash_input == "o":

    def check_win(self):
        if self.horse1_pos[1] == 24:
            print("The Red Snail has won the race!")
            time.sleep(999999999)
            return 
        if self.horse2_pos[1] == 24:
            print("The Blue Snail has won the race!")
            time.sleep(999999999)
            return
        if self.horse3_pos[1] == 24:
            print("The Green Snail has won the race!")
            time.sleep(999999999)
            return
        if self.horse4_pos[1] == 24:
            print("The Yellow Snail has won the race!")
            time.sleep(999999999)
            return
        if self.horse5_pos[1] == 24:
            print("The Orange Snail has won the race!")
            time.sleep(999999999)
            return
    
    
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


        
    def play(self):
        while True:
            for i in range(125):
                time.sleep(0.1)
                self.clear()
                self.display_map()
                self.check_win()
                self.display_map()
                self.move_horses()


test = horse(5,25,1000)

test.play()