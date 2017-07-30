from random import shuffle as std_shuffle
from card import Card

class Deck:

    def __init__(self, ace_high=True):
        self.cards = []
        for suit in ['heart','spade','diamond','club']:
                if ace_high:
                    for val in range(2,15):
                        self.cards.append(Card(val,suit))
                else:
                    for val in range(1,14):
                        self.cards.append(Card(val,suit))

    def shuffle(self):
        std_shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

