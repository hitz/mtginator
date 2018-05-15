import re
#from enum import Enum
#zones = Enum('hand', 'library', 'graveyard', 'battlefield', 'exile')
#permanents = Enum('land', 'creature', 'enchantment', 'artifact', 'planeswalker')
## below should be enums I guess but never bothered to load module
zones = ['hand', 'library', 'graveyard', 'battlefield', 'exile']
permanents = ['Land', 'Creature', 'Enchantment', 'Artifact', 'Planeswalker']
base_symbols = ['B', 'G', 'R', 'U', 'W']

# mana costs from MTGJson are {Z} where Z is int or symbol
# hybrid is {S/T}
# X is {X}
# Phyrexian is {Z/P}
allowed_symbols = base_symbols+['X']
for a in base_symbols:
    allowed_symbols.append(a+'/P')
    for b in base_symbols[1:]:
        if a==b:
            continue
        else:
            allowed_symbols.append(a+'/'+b)
            allowed_symbols.append(b+'/'+a)

manas = '\{\d+\}'
for s in allowed_symbols:
    manas += '\{'+s+'\}+'

keywords = [
    'flash',
    'haste',
    'flying',
    'first strike',
    'lifelink',
    'deathtouch',
    'indestructable',
    'reach',
    'trample',
    'double strike',
    'hexproof',
    'vigilance'
    ]
# currently just evergreen keywords
kwre = [ re.compile(k+'(?i)') for k in keywords ]

templates = {
    'triggered': re.compile('(when |whenever)(?i)'),
    'conditional': re.compile('if (?i)'),
    'activated': re.compile('('+manas+'|sacrifice \S+|pay \S+):(?i)'),
    'mana_ability': re.compile('^(B|G|R|W|U)$|\{T\}: Add ('+manas+') (.*) to your mana pool')
}

class Cost(object):
    # does not handle alt casting costs

    def __init__(self, fromString="", B=0, G=0, R=0, U=0, W=0, c=0, X=False):
        self.mana = {}
        if fromString:
            bracks = re.compile('[\{\}]')
            syms = bracks.split(fromString)
            for symbol in syms:
                if not symbol:
                    continue
                    # split leaves ""s
                try:
                    colorless = int(symbol)
                    self.mana['colorless'] = colorless
                except ValueError:
                    if symbol == 'X':
                        self.mana['X'] = True
                    elif symbol in self.allowed_symbols:
                        self.mana[symbol] = self.mana.get(symbol,0) + 1
                    else:
                        print("Unknown mana symbol: %s" % (symbol))
                        raise

        else:
            ## warning does not handle hybrid/phyrexian use fromString!!!
            self.mana['colorless'] = int(c)
            self.mana['B'] = int(B)
            self.mana['G'] = int(G)
            self.mana['R'] = int(R)
            self.mana['U'] = int(U)
            self.mana['W'] = int(W)
            self.mana['X'] = X

    def cmc(self):
        return self.cardData.get('cmc',0)

class Card(object):

    def __init__(self, name='', cost='', spells=[], cardData={}):
        if cardData:
            self.name = cardData['name']
            self.mana_cost = Cost(fromString=cardData.get('manaCost',''))
            self.cardData = cardData

            self.keywords = []
            self.spells = []
            self.targets = []
            self._parse_text()
        else:
            self.name = name
            self.mana_cost = Cost(fromString=cost)
            self.spells = spells  # array of functions
        self.zone = 'library'
        self.untaps_normally = True
        self.summoning_sick = False
        self.tapped = None #

    def _parse_text(self):
        ''' parse text or originalText for important abilities'''
        text = self.cardData.get("text","")
        if not text:
            # note basic lands
            text = self.cardData.get("originalText", "")

        # find if cipt
        self.cipt = False
        if text.find('enters the battlefield tapped'):
            self.cipt = True

        # find key_words and mana abilities
        for line in text.split("\n"):
            templated = False
            for template in templates.keys():
                tokens = templates[template].search(line)
                if tokens:
                    templated = True
                    if template == 'mana_ability':
                        if len(tokens.group) == 2:
                            # basic land?
                            pass
                        elif len(tokens.group) == 3:
                            # single type
                            pass
                        elif len(tokens.group) >= 4:
                            # multi type
                            pass
            if templated:
                break
            if self.isCreature:
                self.keywords = [ k.lower().strip() for k in kwre.findall(line) ]
            elif re.search('flash(?i)'):
                self.keywords = [ 'flash']
        # find mana abilities

    def isLand(self):
        return 'Land' in self.cardData['types']

    def isPermanent(self):
        [ ty for ty in self.cardData['types'] if ty in permanents ]

    def isCreature(self):
        return 'Creature' in self.cardData['types']

    def isEnchantment(self):
        return 'Enchantment' in self.cardData['types']

    def isPlaneswalker(self):
        return 'Planeswalker' in self.cardData['types']

    def isArtifact(self):
        return 'Artifact' in self.cardData['types']

    def isInstant(self):
        return 'Instant' in self.cardData['types']

    def isSorcery(self):
        return 'Sorcery' in self.cardData['types']

    def isInstantSpeed(self):
        return self.isInstant or 'flash' in self.keywords

    def draw(self):
        self.zone = 'hand'

    def destroy(self):
        self.zone = 'graveyard'

    def exile(self):
        self.zone = 'exile'

    def tap(self):
        if not self.tapped:
            self.tapped = True

    def untap(self):
        if self.tapped:
            self.tapped = False

    def play(self, context):

        self.pay_cost(context)  # need some sort of game context object
        self.zone = 'battlefield'
        self.tapped = False
        if self.cipt:
            self.tapped = True

    def __str__(self):
        return "[ %s (%s) ]" % (self.name, self.cardData.get('manaCost', '0'))



