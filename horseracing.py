import random
import os 
from map import money

class horse:

    def roll():
        result = random.randint(1,4)
        return result

    def __init__(self):
        self.money=money
        print(f"Your starting balance is ${self.money}.\n")
    
    def clear():
        if os.name == 'nt':
            os.system('CLS')

    def create_track(self):
        


    # def create_map(self):
    #     map_layout = []
    #     for i in range(self.rows):
    #         row = [" - "] * self.cols
    #         map_layout.append(row)
    #     return map_layout

    # def display_map(self):
    #     os.system('cls' if os.name == 'nt' else 'clear')

    #     x, y = self.player_pos
    #     self.map[x][y] = " 😎"
    #     for machine_pos in self.slot_machine_locations:
    #         mx, my = machine_pos
    #         self.map[mx][my] = " 🎰"
    #     for bj_pos in self.blackjack_locations:
    #         bx, by = bj_pos
    #         self.map[bx][by] = " 🃏"
    #     for roul_pos in self.roulette_locations:
    #         rx, ry = roul_pos
    #         self.map[rx][ry] = " 🎡"

    #     for row in self.map:
    #         print("".join(row))

    #     self.map[x][y] = " - "

horse.roll()