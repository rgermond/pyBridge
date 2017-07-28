from deck import Deck
from player import Player

class Bridge:

    def __init__(self):
        self.deck = Deck()
        self.players = [Player() for n in range(4)]

        #deal out the cards
        for rnd in range(13):
            for player in self.players:
                card = self.deck.deal()
                player.recv(card)

    def verify(self, player, choice):
        #verifies that the choice of card is a valid move
        #should return true or false
        pass

    def start(self):
        #goes through each round,
        #starts with whoever won the last hand
        #prompt each player for a choice, they'll make it
        #continue until game is done
        #keep score
        pass
