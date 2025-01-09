import random
import os 

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
        for row in self.map:
            print("".join(row))

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

    
    def move_horses(self):
        if horse.roll() == 1:
            self.horse1_pos[1] += 1
        if horse.roll() == 2:
            self.horse2_pos[1] += 1
        if horse.roll() == 3:
            self.horse3_pos[1] += 1
        if horse.roll() == 4:
            self.horse4_pos[1] += 1
        if horse.roll() == 5:
            self.horse5_pos[1] += 1

        
    def play(self):
        for i in range(375):
                horse.roll()
                self.move_horses()
                self.display_map()asdasd

test = horse(5,75,1000)

test.play()