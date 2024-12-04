import os
import random

# Initialize deck once at the start of the game
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def deal(deck):
    hand = []
    random.shuffle(deck)  # Shuffle deck once at the beginning
    for i in range(2):
        card = deck.pop()
        if card == 11:
            card = "J"
        elif card == 12:
            card = "Q"
        elif card == 13:
            card = "K"
        elif card == 14:
            card = "A"
        hand.append(card)
    return hand

def play_again():
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
        game()
    else:
        print("Bye!")
        exit()

def total(hand):
    total = 0
    ace_count = 0  # Track number of Aces
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            total += 11
            ace_count += 1
        else:
            total += card
    
    # Adjust for Aces if total exceeds 21
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    
    return total

def hit(hand, deck):
    card = deck.pop()
    if card == 11:
        card = "J"
    elif card == 12:
        card = "Q"
    elif card == 13:
        card = "K"
    elif card == 14:
        card = "A"
    hand.append(card)
    return hand

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealer_hand, player_hand):
    clear()
    print("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
    print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You got a Blackjack!\n")
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
        play_again()

def score(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You got a Blackjack!\n")
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Sorry. You busted. You lose.\n")
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Dealer busts. You win!\n")
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Sorry. Your score isn't higher than the dealer. You lose.\n")
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Congratulations. Your score is higher than the dealer. You win\n")

def game():
    clear()
    print("WELCOME TO BLACKJACK!\n")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    
    while True:
        print("The dealer is showing a " + str(dealer_hand[0]))
        print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
        blackjack(dealer_hand, player_hand)
        
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        clear()
        
        while choice == "h":
            hit(player_hand, deck)
            print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
            
            if total(player_hand) > 21:
                print("You busted!")
                print_results(dealer_hand, player_hand)
                play_again()
                return  
            
            choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
            clear()
        
        if choice == "s":
            while total(dealer_hand) < 17:
                hit(dealer_hand, deck)
            score(dealer_hand, player_hand)
            play_again()
        
        elif choice == "q":
            print("Bye!")
            exit()

if __name__ == "__main__":
    game()
