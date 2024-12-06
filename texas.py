from random import shuffle

class TexasHoldem:
    #create deck
    def __init__(self):
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        suites = ['Heart', 'Spade', 'Club', 'Diamond']
        self.deck = [j + " " + i for j in values for i in suites]

    #shuffle deck
    def shuffle(self):
        shuffle(self.deck)

    #deal for players
    def deal(self, n_players):
        count = 0
        playercard1 = list()
        while count < n_players:
            card1 = self.deck[count]
            playercard1.append(card1)
            count += 1

        #remove cards from deck that were delt 
        for i in playercard1:
            self.deck.remove(i)

        count = 0
         #card 2 list 
        playercard2 = list() 
        while count < n_players:
            card2 = self.deck[count]
            playercard2.append(card2)
            count += 1

         #remove cards from deck delt for 2nd card
        for i in playercard2:
            self.deck.remove(i)

        #merge cards of playercard1 and playercard2 into set     
        self.playerhand = zip(playercard1, playercard2)

    #define the flop    
    def flop(self):
        #burn a card
        del self.deck[0]
        #lay down three
        self.flopcards = self.deck[0:3]
        #delete flop from deck
        for i in self.flopcards:
            self.deck.remove(i)

    #same as flop for turn and river        
    def turn(self):
        del self.deck[0]
        self.turncard = self.deck[0:1]

        for i in self.turncard:   
            self.deck.remove(i)

    def river(self):
        del self.deck[0]
        self.rivercard = self.deck[0:1]

        for i in self.rivercard:
            self.deck.remove(i)

#create instance of Cards class            
c = TexasHoldem()
#shuffle for this instance
c.shuffle()

#deal for n players
c.deal(9)

print ('Player Hands:')
for i in c.playerhand:
    print (i)

#flop
c.flop()
print ('Flop:')
print (c.flopcards)

#turn
c.turn()
print ('Turn:')
print (c.turncard)

#river
print ('River:')
c.river()
print (c.rivercard)