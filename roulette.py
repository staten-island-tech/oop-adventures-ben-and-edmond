import random

# Constants
RED_NUMBERS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
BLACK_NUMBERS = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}
FIRST_12 = set(range(1, 13))  # Numbers 1-12
SECOND_12 = set(range(13, 25))  # Numbers 13-24
THIRD_12 = set(range(25, 37))  # Numbers 25-36
GREEN_NUMBERS = {0}  # Green zero on the table

# Functions for the game

def spin_wheel():
    """Simulates a roulette wheel spin and returns the result."""
    wheel = list(range(37))  # Numbers 0-36
    result = random.choice(wheel)
    return result

def check_red_or_black(number):
    """Returns whether the number is red, black, or green."""
    if number == 0:
        return "green"
    elif number in RED_NUMBERS:
        return "red"
    elif number in BLACK_NUMBERS:
        return "black"

def check_12(number):
    """Returns which set of 12 the number belongs to."""
    if number in FIRST_12:
        return "first 12"
    elif number in SECOND_12:
        return "second 12"
    elif number in THIRD_12:
        return "third 12"
    else:
        return None

def payout(bet_type, bet_value, result):
    """Calculates the payout based on the bet type and result."""
    if bet_type == "color":
        if check_red_or_black(result) == bet_value:
            return 2  # 1:1 payout, so you win double
        else:
            return 0  # Lose the bet

    elif bet_type == "number":
        if result == bet_value:
            return 36  # 35:1 payout, so you win 35 times your bet
        else:
            return 0  # Lose the bet

    elif bet_type == "1st_12":
        if check_12(result) == bet_value:
            return 3  # 2:1 payout, so you win double the bet
        else:
            return 0  # Lose the bet


def main():
    print("Welcome to Roulette!")   
    # Prompt the player to choose a bet type
    while True:
        bet_type = input("Enter bet type (color, number, or 1st_12): ").lower()
        
        # Initialize bet_value based on bet_type
        if bet_type == "color":
            bet_value = input("Enter bet on red, black, or green: ").lower()
            if bet_value not in ["red", "black", "green"]:
                print("Invalid input, try again.")
                return
        elif bet_type == "number":
            bet_value = int(input("Enter a number to bet on (1-36): "))
            if bet_value < 1 or bet_value > 36:
                print("Invalid number, must be between 1 and 36.")
                return
        elif bet_type == "1st_12":
            bet_value = input("Enter bet on first 12, second 12, or third 12: ").lower()
            if bet_value not in ["first 12", "second 12", "third 12"]:
                print("Invalid input, try again.")
                return
        else:
            print("Invalid bet type. Please choose red_black, number, or 12.")
            return
        
        # Prompt the player to enter a bet amount
        bet_amount = int(input("Enter your bet amount: $"))
        
        # Spin the wheel and determine the result
        result = spin_wheel()
        print(f"The wheel spun: {result}")
        
        # Determine the payout and display the result
        winnings = payout(bet_type, bet_value, result)
        

        if winnings > 0:
            print(f"You win! You won ${winnings * bet_amount}.")
        else:
            print(f"You lose! You lost your bet of ${bet_amount}.")
        



if __name__ == "__main__":
    main()
