import random
import os 

class Horse:

    @staticmethod
    def roll():
        result = random.randint(1, 5)
        return result

    def __init__(self, rows, cols, money):
        self.money = money
        self.cols = cols
        self.rows = rows
        self.map = self.create_track()
        self.horse1_pos = [0, 0]
        self.horse2_pos = [1, 0]
        self.horse3_pos = [2, 0]
        self.horse4_pos = [3, 0]
        self.horse5_pos = [4, 0]
        print(f"Your starting balance is ${self.money}.\n")
    
    @staticmethod
    def clear():
        if os.name == 'nt':
            os.system('CLS')
        else:
            os.system('clear')

    def create_track(self):
        track_layout = []
        for i in range(self.rows):
            row = ["-"] * self.cols
            track_layout.append(row)
        return track_layout
    
    def display_map(self):
        self.clear()  # Clear screen
        # Reset map with empty track
        self.map = self.create_track()
        
        # Place horses on the map
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
        
        # Print the track with horses
        for row in self.map:
            print("".join(row))

    def move_horses(self):
        # Roll the dice and move each horse accordingly
        if Horse.roll() == 1:
            self.horse1_pos[1] += 1
        if Horse.roll() == 2:
            self.horse2_pos[1] += 1
        if Horse.roll() == 3:
            self.horse3_pos[1] += 1
        if Horse.roll() == 4:
            self.horse4_pos[1] += 1
        if Horse.roll() == 5:
            self.horse5_pos[1] += 1

    def play(self):
        # Simulate the race for 15 moves
        for i in range(15):
            self.move_horses()  # Move the horses
            self.display_map()  # Display the current race track

# Create a Horse game with 5 rows, 75 columns, and an initial balance of $100
test = Horse(5, 75, 100)

# Start the game
test.play()
