class Player:

    def __init__(self,name=None):
        self.hand=[]
        self.name=name

    def recv(self, card):
        self.hand.append(card)

    def choose(self):
        return input('select card: ')

    def play(self, choice):
        #return the choice of card from their hand
        #therefore removing it from the stack

        #after choosing a card game should check if its a valid move, if so pop it from the stack
        pass
