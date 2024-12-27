import os
import random
import importlib

class Game:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.player_pos = [0, 0]
        self.slot_machine_locations = [[2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10]]
        self.blackjack_locations = [[2, 15], [3, 15], [4, 15]]
        self.roulette_locations = [[6, 12], [6, 13], [6, 14]]
        self.money = 100
        self.map = self.create_map()

    def create_map(self):
        map_layout = []
        for i in range(self.rows):
            row = [" - "] * self.cols
            map_layout.append(row)
        return map_layout

    def display_map(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        x, y = self.player_pos
        self.map[x][y] = " 😎"
        for machine_pos in self.slot_machine_locations:
            mx, my = machine_pos
            self.map[mx][my] = " 🎰"
        for bj_pos in self.blackjack_locations:
            bx, by = bj_pos
            self.map[bx][by] = " 🃏"
        for rl_pos in self.roulette_locations:
            rx, ry = rl_pos
            self.map[rx][ry] = " 🎡"

        for row in self.map:
            print("".join(row))

        self.map[x][y] = " - "

    def move_player(self, direction):
        x, y = self.player_pos

        if direction == "w" and x > 0:
            self.player_pos[0] -= 1
        elif direction == "a" and y > 0:
            self.player_pos[1] -= 1
        elif direction == "s" and x < self.rows - 1:
            self.player_pos[0] += 1
        elif direction == "d" and y < self.cols - 1:
            self.player_pos[1] += 1

    def check_position(self):
        if self.player_pos in self.slot_machine_locations:
            print("Starting Slots!\n")
            slots = importlib.import_module('slots')
            slots.Slots().game_loop()
        elif self.player_pos in self.blackjack_locations:
            print("Starting Blackjack!\n")
            blackjack_module = importlib.import_module('blackjack')
            blackjack_game = blackjack_module.Blackjack()
            blackjack_game.bj()
        elif self.player_pos in self.roulette_locations:
            print("Starting Roulette!\n")
            roulette_module = importlib.import_module('roulette')
            roulette_game = roulette_module.Roulette(self.money)
            self.money = roulette_game.main() 
    def play(self):
        while True:
            self.display_map()
            print(f"Current Money: ${self.money}")
            move = input("Move with WASD (or Q to quit): ").lower()

            if move == "q":
                break
            elif move in ["w", "a", "s", "d"]:
                self.move_player(move)
                self.check_position()