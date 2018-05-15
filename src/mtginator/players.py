import random

class Player(object):

    def __init__(self, name='Default1', deck=None, life=20, poison=10):
        self.name = name
        self.deck = deck
        self.life = life
        self.poison = poison
        self.hand = []
        self.graveyard = []
        self.exile = []

        self.battlefield = []


    def _satisfied(self, rules, n):
        if not rules:
            if len(self.hand) and len(self.hand) < 5:
                # keep all 4s
                return True
            elif len([ c for c in self.hand if c.isLand() ]) and len([ c for c in self.hand if not c.isLand() ]):
                    return True
            else:
                return False

    def available_mana(self):


    def reset(self):
        self.deck.main = self.deck.main + self.hand + self.graveyard + self.exile + self.battlefield
        self.hand = self.graveyard = self.exile = self.battlefield = []
        self.deck.shuffle()
        assert(len(self.deck.main) == self.deck.total_cards)


    def mulligan(self, rules={}, n=7, verbose=True):
        ''' draw an initial hand and paris mulligan until acceptable by rules
            default rules are mulligan 0 land and 0 non-land hands until 4, then keep '''

        self.deck.main += self.hand
        self.deck.shuffle()
        self.hand = []
        if verbose:
            if n==7:
                print("Drawing initial 7...")
            else:
                print("Mulling to %s...") % (n)
        for i in range(0,n):
            self.hand.append(self.deck.drawCard())

        while(not self._satisfied(rules, n)):
            self.mulligan(rules,n-1, verbose=verbose)

        if verbose:
            print("Final hand %s" % ([ str(c) for c in self.hand ]))

    def enumerate_plays(self):
        ''' For a given hand (or metahand) and available mana, what plays are available to Player'''
        if not self.hand:
            return []

        for card in self.hand:
