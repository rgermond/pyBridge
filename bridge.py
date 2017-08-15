from deck import Deck
from player import Player

def circleList(ls, start):
    return ls[start:] + ls[:start]

class Bridge:

    def __init__(self):


        #intialize the players
        self.players = [Player() for n in range(4)]

        #initialize the deck
        self.deck = Deck()

        #shuffle the deck
        self.deck.shuffle()

        #deal out the cards
        for rnd in range(13):
            for player in self.players:
                card = self.deck.deal()
                player.recv(card)

    def bid(self,trump):
        self.trump = trump

    def check_trick(self, trick):
        win = trick[0]
        lead_suit = trick[0].suit

        for card in trick[1:]:
            if card.suit == self.trump:
                if win.suit != self.trump:
                    win = card
                else:
                    if card.val > win.val:
                        win = card
            elif card.suit == lead_suit and win.suit == lead_suit:
                if card.val > win.val:
                    win = card

        return trick.index(win)

    def play(self):
        start = 0

        #go for 13 rounds of the game
        for rnd in range(13):

            #reset the suit that is in play
            suit = None

            #reset the pot of cards
            trick = []

            #go from the player who won the last round (start will be updated)
            for player in circleList(self.players, start):

                #player picks a card
                card = player.pick(suit)

                #it is added to the trick
                trick.append(card)

                #if its the first player
                if suit is None:
                    suit = card.suit     #update the suit

            #determine who won the trick
            win_idx = self.check_trick(start, trick)

            #update the start
            start = start+win_idx
            if start > 3:
                start = start - 4

            #increment the number of tricks the player has won
            self.players[start].tricks += 1

def main():
    bridge = Bridge()
    bridge.play()

if __name__=='__main__':
    main()



