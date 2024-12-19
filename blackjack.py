import os 
import random

class Blackjack:
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
    def deal(deck):
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

    def play_again():
        again = input("Do you want to play again? (Y/N) : ").lower()
        if again == "y":
            Blackjack.game()
        else:
            print("Bye!")
            exit()

    def total(hand):
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
        Blackjack.clear()
        print("The dealer has a " + str(dealer_hand) + " for a total of " + str(Blackjack.total(dealer_hand)))
        print("You have a " + str(player_hand) + " for a total of " + str(Blackjack.total(player_hand)))

    def blackjack(dealer_hand, player_hand):
        if Blackjack.total(player_hand) == 21:
            Blackjack.print_results(dealer_hand, player_hand)
            print("Congratulations! You got a Blackjack!\n")
            Blackjack.play_again()
        elif Blackjack.total(dealer_hand) == 21:
            Blackjack.print_results(dealer_hand, player_hand)
            print("Sorry, you lose. The dealer got a blackjack.\n")
            Blackjack.play_again()

    def score(dealer_hand, player_hand):
        if Blackjack.total(player_hand) == 21:
            Blackjack.print_results(dealer_hand, player_hand)
            print("Congratulations! You got a Blackjack!\n")
        elif Blackjack.total(dealer_hand) == 21:
            Blackjack.print_results(dealer_hand, player_hand)
            print("Sorry, you lose. The dealer got a blackjack.\n")
        elif Blackjack.total(player_hand) > 21:
            Blackjack.print_results(dealer_hand, player_hand)
            print("Sorry. You busted. You lose.\n")
        elif Blackjack.total(dealer_hand) > 21:
            Blackjack.print_results(dealer_hand, player_hand)
            print("Dealer busts. You win!\n")
        elif Blackjack.total(player_hand) < Blackjack.total(dealer_hand):
            Blackjack.print_results(dealer_hand, player_hand)
            print("Sorry. Your score isn't higher than the dealer. You lose.\n")
        elif Blackjack.total(player_hand) > Blackjack.total(dealer_hand):
            Blackjack.print_results(dealer_hand, player_hand)
            print("Congratulations. Your score is higher than the dealer. You win\n")

    def bj():
        Blackjack.clear()
        print("WELCOME TO BLACKJACK!\n")
        dealer_hand = Blackjack.deal(deck)
        player_hand = Blackjack.deal(deck)
        
        while True:
            print("The dealer is showing a " + str(dealer_hand[0]))
            print("You have a " + str(player_hand) + " for a total of " + str(Blackjack.total(player_hand)))
            Blackjack.blackjack(dealer_hand, player_hand)
            
            choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
            Blackjack.clear()
            
            while choice == "h":
                Blackjack.hit(player_hand, deck)
                print("You have a " + str(player_hand) + " for a total of " + str(Blackjack.total(player_hand)))
                
                if Blackjack.total(player_hand) > 21:
                    print("You busted!")
                    Blackjack.print_results(dealer_hand, player_hand)
                    Blackjack.play_again()
                    return  
                
                choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
                Blackjack.clear()
            
            if choice == "s":
                while Blackjack.total(dealer_hand) < 17:
                    Blackjack.hit(dealer_hand, deck)
                Blackjack.score(dealer_hand, player_hand)
                Blackjack.play_again()
            
            elif choice == "q":
                print("Bye!")
                exit()

#Blackjack.bj()