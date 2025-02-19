import os
import gslots
import groulette
import gblackjack
import gsnailracing
import time
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
class grandma(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

    def scream(self):
        print(self.firstname, self.lastname,":" "\nGET AWAY FROM ME")
    def scream_machine(self):
        print(self.firstname, self.lastname,":" "\nGET AWAY FROM MY MACHINE")
class Game:
    def __init__(self, rows, cols, money):
        self.rows = rows
        self.cols = cols
        self.player_pos = [5, 8]
        self.money = money
        self.slot_machine_locations = [[2, 6], [2, 7], [2, 8], [2, 9], [2, 10],
                                       [9, 6], [9, 7], [9, 8], [9, 9], [9, 10], 
                                       [4, 7], [4, 8], [4, 9], [4, 10],
                                       [7, 6], [7, 7], [7, 8], [7, 9], [7, 10]]
        self.blackjack_locations = [ [2, 15], [3, 15], [4, 15], [2, 13], [3, 13], [4, 13], [7,15] , [8,15] , [9,15] , [7,13] , [8,13] , [9,13] ]
        self.roulette_locations = [[2, 1], [3, 1], [4, 1], [2, 3], [3, 3], [4, 3], [7,1] , [8,1] , [9,1] , [7,3] , [8,3] , [9,3]]
        self.snail_locations = [[0,0],[11,0],[11,17],[0,17],[2,4],[2,5],[2,11],[2,12]]
        self.grammy_locations = [[5,6]]
        self.grammy_machine_locations = [[4,6]]
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
        for roul_pos in self.roulette_locations:
            rx, ry = roul_pos
            self.map[rx][ry] = " 🎡"
        for snail_pos in self.snail_locations:
            sx, sy = snail_pos
            self.map[sx][sy] = " 🐌"
        for grammy_pos in self.grammy_locations:
            gx, gy = grammy_pos
            self.map[gx][gy] = " 👵"
        for grammy_machine_pos in self.grammy_machine_locations:
            gmx, gmy = grammy_machine_pos
            self.map[gmx][gmy] = " 🎰"

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
        game = None
        if self.money > 0:
            if self.player_pos in self.slot_machine_locations:
                print("Starting Slots!\n")
                game = gslots.Slots(self.money)
            elif self.player_pos in self.blackjack_locations:
                print("Starting Blackjack!\n")
                game = gblackjack.Blackjack(self.money)
            elif self.player_pos in self.roulette_locations:
                print("Starting Roulette!\n")
                game = groulette.roulette(self.money)
            elif self.player_pos in self.snail_locations:
                print("Starting Snail Racing\n")
                game = gsnailracing.snail(5, 25, self.money)
            elif self.player_pos in self.grammy_locations:
                grammy_anger = grandma("Linda", "Smith")
                grammy_anger.scream()
                time.sleep(1)
            elif self.player_pos in self.grammy_machine_locations:
                grammy_anger = grandma("Linda", "Smith")
                grammy_anger.scream_machine()
                time.sleep(1)

        if game:
            game.start()
            self.money = game.get_money()

    def play(self):
        while True:
            self.display_map()
            move = input("Move with WASD (or Q to quit): ").lower()

            if move == "q":
                return
            elif move in ["w", "a", "s", "d"]:
                self.move_player(move)
                self.check_position()