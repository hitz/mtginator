import pytest  # noqa

from mtginator import cards

data = [  # should be a pytest.fixture I guess
    {
        '{2}{G}': {
            'generic': 2,
            'G': 1
        }
    },
    {
        '{3}{B}{B}': {
            'generic': 3,
            'B': 2
        }
    },
    {
        '{U}': {
            'U': 1
        }
    },
    {
        '{G}{W}{R}': {
            'G': 1,
            'W': 1,
            'R': 1
        }
    },
    {
        '{4}': {
            'generic': 4,
        }
    },
    {
        '{U/R}': {
            'U/R': 1
        }
    },
    {
        '{U/W}{U/W}{2}': {
            'generic': 2,
            'U/W': 2
        }
    },
    {
        '{2}{G}{G}{W}{W}{U}{U}': {
            'generic': 2,
            'G': 2,
            'W': 2,
            'U': 2
        }
    },
    {
        '{G/P}': {
            'G/P': 1
        }
    },
    {
        '{C}4': {
            'C': 1,
            'generic': 4,
        }
    },
    {
        '{3}{R}{R/P}': {
            'generic': 3,
            'R': 1,
            'R/P': 1
        }
    }
]

bad_data = [
    '{H}',
]


@pytest.fixture
def basics():

    land_cards = [
        {
            'artist': 'John Avon',
            'cmc': 0,
            'colorIdentity': ['W'],
            'id': '501440ed1f0814e9ba812ad9f36ff69053fd0b42',
            'imageName': 'plains',
            'layout': 'normal',
            "multiverseid": 439601,
            "name": "Plains",
            "number": "212",
            "originalType": "Basic Land — Plains",
            'rarity': 'Basic Land',
            'subtypes': ['Plains'],
            'supertypes': ['Basic'],
            'type': 'Basic Land — Plains',
            'types': ['Land'],
            'watermark': 'White'
        },
        {
            'artist': 'John Avon',
            'cmc': 0,
            'colorIdentity': ['U'],
            'id': 'c745293c1f00ec9a2f78155322b74dc85ec4f3cb',
            'imageName': 'island',
            'layout': 'normal',
            'multiverseid': 439602,
            'name': 'Island',
            'number': '213',
            'originalType': 'Basic Land — Island',
            'rarity': 'Basic Land',
            'subtypes': ['Island'],
            'supertypes': ['Basic'],
            'type': 'Basic Land — Island',
            'types': ['Land'],
            'watermark': 'Blue'
        },
        {
            'artist': 'John Avon',
            'cmc': 0,
            'colorIdentity': ['B'],
            'id': '7210d09e2bd2613adb39795e0f216cc20c6dba0c',
            'imageName': 'swamp',
            'layout': 'normal',
            'multiverseid': 439603,
            'name': 'Swamp',
            'number': '214',
            'originalType': 'Basic Land — Swamp',
            'rarity': 'Basic Land',
            'subtypes': ['Swamp'],
            'supertypes': ['Basic'],
            'type': 'Basic Land — Swamp',
            'types': ['Land'],
            'watermark': 'Black'
        },
        {
            'artist': 'John Avon',
            'cmc': 0,
            'colorIdentity': ['R'],
            'id': '83345253cf2ac7c3ea2fce2fa186f7afd6a8447c',
            'imageName': 'mountain',
            'layout': 'normal',
            'multiverseid': 439604,
            'name': 'Mountain',
            'number': '215',
            'originalType': 'Basic Land — Mountain',
            'rarity': 'Basic Land',
            'subtypes': ['Mountain'],
            'supertypes': ['Basic'],
            'type': 'Basic Land — Mountain',
            'types': ['Land'],
            'watermark': 'Red'
        },
        {
            'artist': 'John Avon',
            'cmc': 0,
            'colorIdentity': ['G'],
            'id': '70523a1e8264d75a44d6d18af66f813dda4e7960',
            'imageName': 'forest',
            'layout': 'normal',
            'multiverseid': 439605,
            'name': 'Forest',
            'number': '216',
            'originalType': 'Basic Land — Forest',
            'rarity': 'Basic Land',
            'subtypes': ['Forest'],
            'supertypes': ['Basic'],
            'type': 'Basic Land — Forest',
            'types': ['Land'],
            'watermark': 'Green'
        },
        {
            "artist": "Jason Felix",
            "cmc": 0,
            "id": "68d4ca6db1b4f92aa306627cefa3d02137e4fa10",
            "imageName": "wastes2",
            "layout": "normal",
            "multiverseid": 407693,
            "name": "Wastes",
            "number": "183",
            "originalText": "C",
            "originalType": "Basic Land",
            "rarity": "Basic Land",
            "supertypes": [
                "Basic"
            ],
            "text": "{T}: Add {C}.",
            "type": "Basic Land",
            "types": [
                "Land"
            ],
            "variations": [
                407694,
                407695,
                407696
            ],
            "watermark": "Colorless"
        },
    ]
    return {x['name']: cards.Card(card_data=x) for x in land_cards}


@pytest.fixture
def dual_land():
    ''' Comes into play tapped and makes 2 manas '''
    gate = {
        "artist": "John Avon",
        "cmc": 0,
        "colorIdentity": [
          "W",
          "B"
        ],
        "flavor": "Enter to find wealth, security, and eternal life . . . for just a small price up front.",

        "id": "10c55a7849426eb6a1bddb183b34d638814fcc65",
        "imageName": "orzhov guildgate",
        "layout": "normal",
        "mciNumber": "299",
        "multiverseid": 405331,
        "name": "Orzhov Guildgate",
        "number": "299",
        "originalText": "Orzhov Guildgate enters the battlefield tapped.{T}: Add {W} or {B} to your mana pool.",
        "originalType": "Land — Gate",
        "rarity": "Common",
        "subtypes": [
          "Gate"
        ],
        "text": "Orzhov Guildgate enters the battlefield tapped.\n{T}: Add {W} or {B}.",
        "type": "Land — Gate",
        "types": [
          "Land"
        ]
    }
    return cards.Card(card_data=gate)


@pytest.fixture
def creature():
    baneslayer = {
        "artist": "Greg Staples",
        "cmc": 5,
        "colorIdentity": [
          "W"
        ],
        "colors": [
          "White"
        ],
        "flavor": "Some angels protect the meek and innocent. Others seek out and smite evil wherever it lurks.",
        "id": "c7416f618d15b5067b2020814108622e3161caf0",
        "imageName": "baneslayer angel",
        "layout": "normal",
        "manaCost": "{3}{W}{W}",
        "mciNumber": "6",
        "multiverseid": 401633,
        "name": "Baneslayer Angel",
        "number": "6",
        "originalText": "Flying, first strike, lifelink, protection from Demons and from Dragons",
        "originalType": "Creature — Angel",
        "power": "5",
        "rarity": "Mythic Rare",
        "subtypes": [
          "Angel"
        ],
        "text": "Flying, first strike, lifelink, protection from Demons and from Dragons",
        "toughness": "5",
        "type": "Creature — Angel",
        "types": [
          "Creature"
        ]
    }
    return cards.Card(card_data=baneslayer)


@pytest.fixture
def broken_creature():
    busted = {
        "id": "89028c1a74afa4a6228f53a9f5c9ddd343fdc004",
        "artist": "Seb McKinnon",
        "cmc": 6,
        "colorIdentity": [
          "B"
        ],
        "colors": [
          "Black"
        ],
        "imageName": "soulflayer",
        "layout": "normal",
        "manaCost": "{4}{B}{B}",
        "mciNumber": "151",
        "name": "Soulflayer",
        "number": "151",
        "power": "4",
        "printings": [
          "pPRE",
          "FRF"
        ],
        "rarity": "Special",
        "releaseDate": "2015-01-17",
        "source": "Fate Reforged Sultai Prerelease participation bonus",
        "subtypes": [
          "Demon"
        ],
        "text": "Delve (Each card you exile from your graveyard while casting this spell pays for {1}.)\nIf a creature card with flying was exiled with Soulflayer's delve ability, Soulflayer has flying. The same is true for first strike, double strike, deathtouch, haste, hexproof, indestructible, lifelink, reach, trample, and vigilance.",
        "toughness": "4",
        "type": "Creature — Demon",
        "types": [
          "Creature"
        ]
    }
    return cards.Card(card_data=busted)


@pytest.fixture
def legend():
    jodah = {
        "artist": "Yongjae Choi",
        "cmc": 4,
        "colorIdentity": [
          "W",
          "U",
          "R",
          "B",
          "G"
        ],
        "colors": [
          "White",
          "Blue",
          "Red"
        ],
        "flavor": "\"Chronicles across the ages describe Jodah. They likely refer not to one mage, but to a family or an arcane title.\"\n—Arkol, Argivian scholar",
        "id": "09bf8437ee518d775f5574f1c3d9077569239cac",
        "imageName": "jodah, archmage eternal",
        "layout": "normal",
        "manaCost": "{1}{U}{R}{W}",
        "multiverseid": 443086,
        "name": "Jodah, Archmage Eternal",
        "number": "198",
        "originalText": "Flying\nYou may pay {W}{U}{B}{R}{G} rather than pay the mana cost for spells that you cast.",
        "originalType": "Legendary Creature — Human Wizard",
        "power": "4",
        "printings": [
          "DOM"
        ],
        "rarity": "Rare",
        "subtypes": [
          "Human",
          "Wizard"
        ],
        "supertypes": [
          "Legendary"
        ],
        "text": "Flying\nYou may pay {W}{U}{B}{R}{G} rather than pay the mana cost for spells that you cast.",
        "toughness": "3",
        "type": "Legendary Creature — Human Wizard",
        "types": [
          "Creature"
        ]
    }
    return cards.Card(card_data=jodah)


@pytest.fixture
def instant():
    opt = {
        "artist": "Craig J Spearing",
        "cmc": 1,
        "colorIdentity": [
          "U"
        ],
        "colors": [
          "Blue"
        ],
        "flavor": "\"It's easy to anticipate Captain Storm's orders: take the more dangerous route.\"",
        "id": "bd9e59dedab85afcdbb6a36f0bb8923f3fd7c822",
        "imageName": "opt",
        "layout": "normal",
        "manaCost": "{U}",
        "mciNumber": "65",
        "multiverseid": 435217,
        "name": "Opt",
        "number": "65",
        "originalText": "Scry 1. (Look at the top card of your library. You may put that card on the bottom of your library.)\nDraw a card.",
        "originalType": "Instant",
        "rarity": "Common",
        "text": "Scry 1. (Look at the top card of your library. You may put that card on the bottom of your library.)\nDraw a card.",
        "type": "Instant",
        "types": [
          "Instant"
        ]
    }
    return cards.Card(card_data=opt)


@pytest.fixture
def sorcery():
    ''' something with hybrid mana '''
    skybreaker = {
        "artist": "Randy Gallegos",
        "cmc": 7,
        "colorIdentity": [
          "U",
          "R"
        ],
        "colors": [
          "Blue",
          "Red"
        ],
        "flavor": "It hears and answers every orison across Shadowmoor.",
        "id": "41fba89f1d092e02d09ef196b066bd4c4e75f04e",
        "imageName": "call the skybreaker",
        "layout": "normal",
        "manaCost": "{5}{U/R}{U/R}",
        "mciNumber": "214",
        "multiverseid": 413756,
        "name": "Call the Skybreaker",
        "number": "214",
        "originalText": "Put a 5/5 blue and red Elemental creature token with flying onto the battlefield.\nRetrace (You may cast this card from your graveyard by discarding a land card in addition to paying its other costs.)",
        "originalType": "Sorcery",
        "rarity": "Rare",
        "text": "Create a 5/5 blue and red Elemental creature token with flying.\nRetrace (You may cast this card from your graveyard by discarding a land card in addition to paying its other costs.)",
        "type": "Sorcery",
        "types": [
          "Sorcery"
        ]
    }
    return cards.Card(card_data=skybreaker)


@pytest.fixture
def xspell():
    ''' fireball perhaps '''
    fireball = {
        "artist": "Dave Dorman",
        "cmc": 1,
        "colorIdentity": [
          "R"
        ],
        "colors": [
          "Red"
        ],
        "flavor": "The spell fell upon the crowd like a dragon, ancient and full of death.",
        "id": "cc2a2fb5ba26d8db0db8ff8421fc5d566f68f6bf",
        "imageName": "fireball",
        "layout": "normal",
        "manaCost": "{X}{R}",
        "mciNumber": "56",
        "multiverseid": 393831,
        "name": "Fireball",
        "number": "56",
        "originalText": "Fireball deals X damage divided evenly, rounded down, among any number of target creatures and/or players.\nFireball costs {1} more to cast for each target beyond the first.",
        "originalType": "Sorcery",
        "rarity": "Uncommon",
        "text": "This spell costs {1} more to cast for each target beyond the first.\nFireball deals X damage divided evenly, rounded down, among any number of targets.",
        "type": "Sorcery",
        "types": [
          "Sorcery"
        ]
    }
    return cards.Card(card_data=fireball)


@pytest.fixture
def artifact():
    post = {
        "artist": "Adam Paquette",
        "cmc": 4,
        "id": "03b03295b5d8acdf7a719a71e7aed9b4bff33ab3",
        "imageName": "trading post",
        "layout": "normal",
        "manaCost": "{4}",
        "mciNumber": "278",
        "multiverseid": 420895,
        "name": "Trading Post",
        "number": "278",
        "originalText": "{1}, {T}, Discard a card: You gain 4 life.\n{1}, {T}, Pay 1 life: Create a 0/1 white Goat creature token.\n{1}, {T}, Sacrifice a creature: Return target artifact card from your graveyard to your hand.\n{1}, {T}, Sacrifice an artifact: Draw a card.",
        "originalType": "Artifact",
        "rarity": "Rare",
        "text": "{1}, {T}, Discard a card: You gain 4 life.\n{1}, {T}, Pay 1 life: Create a 0/1 white Goat creature token.\n{1}, {T}, Sacrifice a creature: Return target artifact card from your graveyard to your hand.\n{1}, {T}, Sacrifice an artifact: Draw a card.",
        "type": "Artifact",
        "types": [
          "Artifact"
        ]
    }
    return cards.Card(card_data=post)


@pytest.fixture
def aura():
    owtw = {
        "artist": "Naomi Baker",
        "cmc": 2,
        "colorIdentity": [
          "U"
        ],
        "colors": [
          "Blue"
        ],
        "flavor": "\"River and sea, jungle and sky. Water flows freely between the two halves of the world. We are creatures of the water.\"\n—Shaper Tuvasa",
        "id": "d09f596ba35de4276e85abea5eb6f41bb462d677",
        "imageName": "one with the wind",
        "layout": "normal",
        "manaCost": "{1}{U}",
        "mciNumber": "64",
        "multiverseid": 435216,
        "name": "One With the Wind",
        "number": "64",
        "originalText": "Enchant creature\nEnchanted creature gets +2/+2 and has flying.",
        "originalType": "Enchantment — Aura",
        "printings": [
          "XLN"
        ],
        "rarity": "Common",
        "subtypes": [
          "Aura"
        ],
        "text": "Enchant creature\nEnchanted creature gets +2/+2 and has flying.",
        "type": "Enchantment — Aura",
        "types": [
          "Enchantment"
        ],
    }
    return cards.Card(card_data=owtw)


@pytest.fixture
def enchantment():
    ''' something with an activated ability '''
    agg_assault = {
        "artist": "Greg Staples",
        "cmc": 3,
        "colorIdentity": [
          "R"
        ],
        "colors": [
          "Red"
        ],
        "id": "d425390b0a2b7af340767b18207c6242353f167e",
        "imageName": "aggravated assault",
        "layout": "normal",
        "manaCost": "{2}{R}",
        "mciNumber": "185",
        "multiverseid": 40195,
        "name": "Aggravated Assault",
        "number": "185",
        "originalText": "{3}{R}{R}: Untap all creatures you control. After this phase, there is an additional combat phase followed by an additional main phase. Play this ability only any time you could play a sorcery.",
        "originalType": "Enchantment",
        "rarity": "Rare",
        "text": "{3}{R}{R}: Untap all creatures you control. After this main phase, there is an additional combat phase followed by an additional main phase. Activate this ability only any time you could cast a sorcery.",
        "type": "Enchantment",
        "types": [
          "Enchantment"
        ]
    }
    return cards.Card(card_data=agg_assault)


@pytest.fixture
def planeswalker():
    tibalt = {
        "artist": "Chase Stone",
        "cmc": 2,
        "colorIdentity": [
          "R"
        ],
        "colors": [
          "Red"
        ],
        "id": "e191ef6de0af169cf10e069fd55e3d579f05537d",
        "imageName": "tibalt, the fiend-blooded",
        "layout": "normal",
        "loyalty": 2,
        "manaCost": "{R}{R}",
        "mciNumber": "41",
        "multiverseid": 368531,
        "name": "Tibalt, the Fiend-Blooded",
        "number": "41",
        "originalText": "+1: Draw a card, then discard a card at random.\n-4: Tibalt, the Fiend-Blooded deals damage equal to the number of cards in target player's hand to that player.\n-6: Gain control of all creatures until end of turn. Untap them. They gain haste until end of turn.",
        "originalType": "Planeswalker — Tibalt",
        "printings": [
          "AVR",
          "DDK"
        ],
        "rarity": "Mythic Rare",
        "rulings": [
          {
            "date": "2012-05-01",
            "text": "The number of cards in the target player's hand is determined when Tibalt's second ability resolves."
          },
          {
            "date": "2012-05-01",
            "text": "When Tibalt's third ability resolves, all creatures will become untapped and gain haste, including ones you controlled before the ability resolved."
          }
        ],
        "subtypes": [
          "Tibalt"
        ],
        "supertypes": [
          "Legendary"
        ],
        "text": "+1: Draw a card, then discard a card at random.\n−4: Tibalt, the Fiend-Blooded deals damage equal to the number of cards in target player's hand to that player.\n−6: Gain control of all creatures until end of turn. Untap them. They gain haste until end of turn.",
        "type": "Legendary Planeswalker — Tibalt",
        "types": [
          "Planeswalker"
        ]
    }
    return cards.Card(card_data=tibalt)


@pytest.fixture
def artifact_creature():
    metamorph = {
        "artist": "Jung Park",
        "cmc": 4,
        "colorIdentity": [
          "U"
        ],
        "colors": [
          "Blue"
        ],
        "id": "7e2ca176e9c8b43903dc8de0109e995a5ff95a4f",
        "imageName": "phyrexian metamorph",
        "layout": "normal",
        "manaCost": "{3}{U/P}",
        "mciNumber": "14",
        "name": "Phyrexian Metamorph",
        "number": "14",
        "power": "0",
        "printings": [
          "pLPA",
          "NPH"
        ],
        "rarity": "Special",
        "releaseDate": "2011-05-13",
        "source": "New Phyrexia Launch Party participation bonus",
        "subtypes": [
          "Shapeshifter"
        ],
        "text": "({U/P} can be paid with either {U} or 2 life.)\nYou may have Phyrexian Metamorph enter the battlefield as a copy of any artifact or creature on the battlefield, except it's an artifact in addition to its other types.",
        "toughness": "0",
        "type": "Artifact Creature — Shapeshifter",
        "types": [
          "Artifact",
          "Creature"
        ]
    }
    return cards.Card(card_data=metamorph)


@pytest.fixture
def enchantment_creature():
    ''' flash  + bestow '''
    boon_satyr = {
        "artist": "Wesley Burt",
        "cmc": 3,
        "colorIdentity": [
          "G"
        ],
        "colors": [
          "Green"
        ],
        "id": "72e0b7a24aac0b2c6ca40010f323f57c858b8c6a",
        "imageName": "boon satyr",
        "layout": "normal",
        "manaCost": "{1}{G}{G}",
        "mciNumber": "152",
        "multiverseid": 373509,
        "name": "Boon Satyr",
        "number": "152",
        "originalText": "Flash\nBestow {3}{G}{G} (If you cast this card for its bestow cost, it's an Aura spell with enchant creature. It becomes a creature again if it's not attached to a creature.)\nEnchanted creature gets +4/+2.",
        "originalType": "Enchantment Creature — Satyr",
        "power": "4",
        "printings": [
          "THS"
        ],
        "rarity": "Rare",
        "subtypes": [
          "Satyr"
        ],
        "text": "Flash\nBestow {3}{G}{G} (If you cast this card for its bestow cost, it's an Aura spell with enchant creature. It becomes a creature again if it's not attached to a creature.)\nEnchanted creature gets +4/+2.",
        "toughness": "2",
        "type": "Enchantment Creature — Satyr",
        "types": [
          "Enchantment",
          "Creature"
        ]
    }
    return cards.Card(card_data=boon_satyr)


@pytest.fixture
def legendary_sorcery():
    urb = {
        "artist": "Noah Bradley",
        "cmc": 5,
        "colorIdentity": [
          "W"
        ],
        "colors": [
          "White"
        ],
        "flavor": "Centuries ago, one man's vengeance plunged the world into ice and darkness.",
        "id": "a2deafcef6967cba4268fb0ac203f54c3ae34f28",
        "imageName": "urza's ruinous blast",
        "layout": "normal",
        "manaCost": "{4}{W}",
        "multiverseid": 442927,
        "name": "Urza's Ruinous Blast",
        "number": "39",
        "originalText": "(You may cast a legendary sorcery only if you control a legendary creature or planeswalker.)\nExile all nonland permanents that aren't legendary.",
        "originalType": "Legendary Sorcery",
        "printings": [
          "DOM"
        ],
        "rarity": "Rare",
        "rulings": [
          {
            "date": "2018-04-27",
            "text": "You can't cast a legendary sorcery unless you control a legendary creature or a legendary planeswalker. Once you begin to cast a legendary sorcery, losing control of your legendary creatures and planeswalkers won't affect that spell."
          },
          {
            "date": "2018-04-27",
            "text": "Other than the casting restriction, the legendary supertype on a sorcery carries no additional rules. You may cast any number of legendary sorceries in a turn, and your deck may contain any number of legendary cards (but no more than four of any with the same name)."
          }
        ],
        "supertypes": [
          "Legendary"
        ],
        "text": "(You may cast a legendary sorcery only if you control a legendary creature or planeswalker.)\nExile all nonland permanents that aren't legendary.",
        "type": "Legendary Sorcery",
        "types": [
          "Sorcery"
        ]
      }
    return cards.Card(card_data=urb)


def test_creature(creature):
    assert creature.is_creature()
    assert creature.is_permanent()
    assert not creature.cipt
    assert 'flying' in creature.keywords
    assert 'first strike' in creature.keywords
    assert 'lifelink' in creature.keywords
    assert creature.cmc() == 5
    assert creature.mana_cost.mana['W'] == 2
    assert creature.mana_cost.mana['generic'] == 3


@pytest.mark.xfail
def test_bad_creature(broken_creature):
    ''' note this is an xfail because "parser" such as it is, thinks soulflayer always has all keywords'''
    assert broken_creature.is_creature()
    assert broken_creature.is_permanent()
    everything = {
        'flying',
        'first strike',
        'double strike',
        'deathtouch',
        'haste',
        'hexproof',
        'indestructible',
        'lifelink',
        'reach',
        'trample',
        'vigilance'
    }
    assert not everything & broken_creature.keywords
    # something something delve


def test_legend(legend):
    assert legend.is_legendary()
    assert legend.is_permanent()
    assert legend.is_creature()
    for cost in ('generic', 'R', 'W', 'U'):
        assert legend.mana_cost.mana[cost] == 1
    assert set('WUBRG') == set(legend.card_data['colorIdentity'])


def test_instant(instant):
    assert instant.is_instant()
    assert instant.is_instant_speed()
    assert not instant.is_sorcery()
    assert not instant.is_permanent()
    assert instant.cmc() == 1


def test_sorcery(sorcery):
    assert sorcery.is_sorcery()
    assert not sorcery.is_instant()
    assert not sorcery.is_instant_speed()
    assert not sorcery.is_permanent()
    assert sorcery.mana_cost.mana['generic'] == 5
    assert sorcery.mana_cost.mana['U/R'] == 2
    # note this doesn't actually help you figure out the "OR" to cast it


def test_xspell(xspell):
    assert xspell.is_sorcery()
    assert not xspell.is_permanent()
    assert xspell.cmc() == 1
    assert xspell.mana_cost.mana['X']
    assert xspell.mana_cost.mana['R'] == 1


def test_artifact(artifact):
    assert artifact.is_artifact()
    assert artifact.is_permanent()
    assert not artifact.is_creature()
    assert artifact.cmc() == 4
    # something something multiple activated tap abilitioes.


def test_aura(aura):
    assert aura.is_enchantment()
    assert aura.is_permanent()
    # something something needs a creature to target


def test_enchantment(enchantment):
    assert enchantment.is_enchantment()
    assert enchantment.is_permanent()
    # something something activated ability


def test_planeswalker(planeswalker):
    assert planeswalker.is_planeswalker()
    assert planeswalker.is_permanent()
    assert planeswalker.is_legendary()
    assert planeswalker.cmc() == 2
    assert planeswalker.mana_cost.mana['R'] == 2
    assert planeswalker.loyalty == 2
    # something something loyalty abilities.


def test_legendary_sorcery(legendary_sorcery):
    assert legendary_sorcery.is_legendary()
    assert legendary_sorcery.is_sorcery()
    assert not legendary_sorcery.is_permanent()
    assert legendary_sorcery.cmc() == 5


def test_boon_satyr(enchantment_creature):
    assert enchantment_creature.is_creature()
    assert enchantment_creature.is_enchantment()
    assert enchantment_creature.is_permanent()
    assert enchantment_creature.is_instant_speed()
    assert enchantment_creature.cmc() == 3

    # something something bestow.


def test_phyrexia_creature(artifact_creature):
    assert artifact_creature.is_creature()
    assert artifact_creature.is_artifact()
    assert artifact_creature.cmc() == 4
    assert artifact_creature.mana_cost.mana['generic'] == 3
    assert artifact_creature.mana_cost.mana['U/P'] == 1


def test_cost_good():

    for sample in data:
        for cost_str in sample.keys():
            cost = cards.Cost(fromString=cost_str)
            assert cost.mana == sample[cost_str]


def test_cost_bad():
    for bad in bad_data:
        try:
            cards.Cost(fromString=bad)
            assert(False)
        except Exception:
            assert(True)


@pytest.mark.xfail
def test_dual(dual_land):
    ''' text parsing not up to snuff here, hence xfail'''
    assert dual_land.cipt
    assert isinstance(dual_land, object)
    assert dual_land.cmc() == 0
    assert dual_land.is_land()
    assert dual_land.is_permanent()
    assert not dual_land.is_instant()
    assert not dual_land.is_sorcery()
    assert not dual_land.is_creature()
    assert not dual_land.is_enchantment()
    assert not dual_land.is_planeswalker()
    assert not dual_land.is_artifact()
    assert not dual_land.is_instant_speed()
    assert set(dual_land.is_mana_source()) == set('BW')


def test_basics(basics):
    for (land_type, mana) in cards.land_mana.items():
        land = basics[land_type]
        assert not land.cipt
        assert isinstance(land, object)
        assert land_type == land.name
        assert land.cmc() == 0
        assert land.is_land()
        assert land.is_permanent()
        assert not land.is_instant()
        assert not land.is_sorcery()
        assert not land.is_creature()
        assert not land.is_enchantment()
        assert not land.is_planeswalker()
        assert not land.is_artifact()
        assert not land.is_instant_speed()
        assert land.is_mana_source() == [mana]
