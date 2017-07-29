from deck import Deck
from player import Player

def circleList(ls, start):
    return ls[start:] + ls[:start]

class Bridge:

    def __init__(self):

        #initialize the deck and the players
        self.deck = Deck()
        self.players = [Player() for n in range(4)]

        #attribute to hold which suit is being played
        self.suit = None

        #deal out the cards
        for rnd in range(13):
            for player in self.players:
                card = self.deck.deal()
                player.recv(card)

    def start(self):
        start = 0

        #go for 13 rounds of the game
        for rnd in range(13):

            #go from the player who won the last round (start will be updated)
            for player in circleList(self.players, start):
                #let the player choose a card to play, if its a valid move play it

                #if its the first player
                if self.suit is None:
                    #let them pick a card and play
                    card = player.pick(self.suit)

                    #update the suit
                    self.suit = card.suit

                else:
                    card = player.pick(self.suit)

            #reset the suit that is in play
            self.suit = None

            #reset the pot of cards


