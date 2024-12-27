import os
import random
import importlib
money = 1000
class Game:
    def __init__(self, rows, cols, money):
        self.rows = rows
        self.cols = cols
        self.player_pos = [0, 0]
        self.money = money
        self.slot_machine_locations = [[2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10],
                                       [9, 5], [9, 6], [9, 7], [9, 8], [9, 9], [9, 10],
                                       [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10],
                                       [7, 5], [7, 6], [7, 7], [7, 8], [7, 9], [7, 10]]
        self.blackjack_locations = [[2, 15], [3, 15], [4, 15], [2, 13], [3, 13], [4, 13]]
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
            # Import and create a Slots instance, passing money
            slots = importlib.import_module('slots')
            slots.Slots(self.money).game_loop()  # Pass the money to the Slots class
        elif self.player_pos in self.blackjack_locations:
            print("Starting Blackjack!\n")
            blackjack_module = importlib.import_module('blackjack')
            blackjack_game = blackjack_module.Blackjack(self.money)  # Pass money to Blackjack class
            blackjack_game.bj()

    def play(self):
        while True:
            self.display_map()
            move = input("Move with WASD (or Q to quit): ").lower()

            if move == "q":
                break
            elif move in ["w", "a", "s", "d"]:
                self.move_player(move)
                self.check_position()

# Entry point of the program
if __name__ == "__main__":
    game = Game(12, 18, 1000)
    game.play()
