class Player:

    #class dictionaries to map the user input to the card associated
    suit_map = {'d':'diamonds', 'c':'clubs','h':'hearts','s':'spades'}
    value_map = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'j':11,'q':12,'k':13,'a':14}

    def __init__(self):
        self.hand=[]
        self.tricks = 0

        #organizer dictionary for quick look up if the card is there
        self.org = {'diamonds':[],'hearts':[],'spades':[],'clubs':[]}


    def recv(self, card):
        self.hand.append(card)
        self.org[key]

    def pick(self, first_suit):

        while True:
            print('Selection must be of form: <value><suit>')
            print('Valid values: 2-10, j (jack), q (queen), k (king), a (ace)')
            print('Valid suits: s (spades), h (hearts), c (clubs), d (diamonds)')
            choice = input('Select card: ')

            #if the suit is not in the dictionary repeat the selection
            if choice[-1] not in self.suit_map:
                print('Invalid suit')
                continue
            else:
                suit = self.suit_map[choice[-1]]

            #if the value is not in the dictionary repeat the selection

            if choice[:-1] not in self.value_map:
                print('Invalid value')
                continue
            else:
                value = self.value_map[choice[:-1]]

            #check if the player actually has that card
            if value not in self.org[suit]:
                print('You do not have that card')
                continue

            #now verify the card can be played
            if first_suit is None:
                #let them play because they have the card
                break

            #if the chosen card doesn't match the first suit played
            #but they dont have cards in that suit (a void)
            elif first_suit != suit and not self.org[first_suit]:
                #let them play because they have a void
                break
            elif first_suit == suit:
                #let them play because they are following suit
                break
            else:
                print('Must play a card from the suit: ', first_suit)
                continue

        #select the card object from the hand
        card = list(filter(lambda c: c.suit==suit and c.val==value), self.hand)[0]
        #remove the card from the hand
        self.hand.remove(card)
        #remove the card from the organizer
        self.org[suit].remove(value)
        return card

