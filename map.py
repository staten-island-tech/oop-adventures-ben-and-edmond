import os
import pygame
import random
import time
import slots
import blackjack
"""         self.black_jack = [,]
        self.roulette = [,]
        self.texas = [,]
        self.slot_machine = [,] """
class Game:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.player_pos = [0, 0] 
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
        self.map[x][y] = "😎 "
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

    def play(self):
        while True:
            self.display_map() 
            move = input("Move with WASD (or Q to quit): ").lower()

            if move == "q": 
                break
            elif move in ["w", "a", "s", "d"]: 
                self.move_player(move)

game = Game(12, 18)
game.play()
