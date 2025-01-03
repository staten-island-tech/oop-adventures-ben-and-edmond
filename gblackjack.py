import os 
import random
from map import money

import random
import os

class Blackjack:
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
    
    def __init__(self):
        self.money = money
        print(f"Your starting balance is ${self.money}.\n")
        
    def deal(self, deck):
        hand = []
        random.shuffle(deck)
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

    def print_results(self, dealer_hand, player_hand):  
        print("The dealer has a " + str(dealer_hand) + " for a total of " + str(self.total(dealer_hand)))
        print("You have a " + str(player_hand) + " for a total of " + str(self.total(player_hand)))

    def total(self, hand):
        total = 0
        ace_count = 0
        for card in hand:
            if card == "J" or card == "Q" or card == "K":
                total += 10
            elif card == "A":
                total += 11
                ace_count += 1
            else:
                total += card
        
        while total > 21 and ace_count > 0:
            total -= 10
            ace_count -= 1
        
        return total

    def hit(self, hand, deck):
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

    def blackjack(self, dealer_hand, player_hand):
        if self.total(player_hand) == 21:
            self.print_results(dealer_hand, player_hand)
            print("Congratulations! You got a Blackjack!\n")
            self.money += 1.5 * bet  
            print(f"Your balance is now ${self.money}.")
            self.play_again()
        elif self.total(dealer_hand) == 21:
            self.print_results(dealer_hand, player_hand)
            print("Sorry, you lose. The dealer got a blackjack.\n")
            self.money -= bet  
            print(f"Your balance is now ${self.money}.")
            self.play_again()

    def score(self, dealer_hand, player_hand):
        if self.total(player_hand) == 21:
            self.print_results(dealer_hand, player_hand)
            print("Congratulations! You got a Blackjack!\n")
            self.money += 1.5 * bet  
        elif self.total(dealer_hand) == 21:
            self.print_results(dealer_hand, player_hand)
            print("Sorry, you lose. The dealer got a blackjack.\n")
            self.money -= bet  
        elif self.total(player_hand) > 21:
            self.print_results(dealer_hand, player_hand)
            print("Sorry. You busted. You lose.\n")
            self.money -= bet  
        elif self.total(dealer_hand) > 21:
            self.print_results(dealer_hand, player_hand)
            print("Dealer busts. You win!\n")
            self.money += bet  
        elif self.total(player_hand) < self.total(dealer_hand):
            self.print_results(dealer_hand, player_hand)
            print("Sorry. Your score isn't higher than the dealer. You lose.\n")
            self.money -= bet  
        elif self.total(player_hand) > self.total(dealer_hand):
            self.print_results(dealer_hand, player_hand)
            print("Congratulations. Your score is higher than the dealer. You win\n")
            self.money += bet  

        print(f"Your balance is now ${self.money}.")
        self.play_again()

    def bj(self):  
        print("WELCOME TO BLACKJACK!\n")
        print(f"Your current balance is ${self.money}.")
        
        if self.money <= 0:
            print("You don't have enough money to play. Exiting the game.")
            exit()

        while True:
            try:
                global bet
                bet = int(input(f"Enter your bet (Current balance: ${self.money}): "))
                if bet > self.money:
                    print("You can't bet more than your current balance!")
                elif bet <= 0:
                    print("Bet must be greater than 0!")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        dealer_hand = self.deal(self.deck)
        player_hand = self.deal(self.deck)
        
        while True:
            print("The dealer is showing a " + str(dealer_hand[0]))
            print("You have a " + str(player_hand) + " for a total of " + str(self.total(player_hand)))
            self.blackjack(dealer_hand, player_hand)
            
            choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
  
            while choice == "h":
                self.hit(player_hand, self.deck)
                print("You have a " + str(player_hand) + " for a total of " + str(self.total(player_hand)))
                
                if self.total(player_hand) > 21:
                    print("You busted!")
                    self.print_results(dealer_hand, player_hand)
                    self.money -= bet  
                    print(f"Your balance is now ${self.money}.")
                    if self.money <= 0:
                        print("You have no money left. Exiting the game.")
                        exit()  
                    self.play_again()
                    return  
                
                choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
      
            if choice == "s":
                print("You chose to stand.")
                print("The dealer's hand is: " + str(dealer_hand) + " for a total of " + str(self.total(dealer_hand)))
                while self.total(dealer_hand) < 17:
                    print("The dealer is hitting...")
                    self.hit(dealer_hand, self.deck)
                    print("Dealer now has: " + str(dealer_hand) + " for a total of " + str(self.total(dealer_hand)))
                
                self.score(dealer_hand, player_hand)
                break

            elif choice == "q":
                print(f"Your balance is now ${self.money}.")
                print("Returning to map.")
                return  

    def play_again(self):
        if self.money <= 0:
            print("You don't have enough money to play again. Exiting the game.")
            exit()
        else:
            again = input("Do you want to play again? (Y/N): ").lower()
            if again == "y":
                self.game()
            else:
                print("Bye!")
                exit()

    def game(self):
        self.bj()


game = Blackjack()
game.game()
