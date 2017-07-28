from deck import Deck

class Dealer:
	def __init__(self):
		self.deck=Deck()
		self.deck.shuffle()

	def deal(self):
		return self.deck.cards.pop()
