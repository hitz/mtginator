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


def test_basics(basics):
    for (land_type, mana) in cards.land_mana.items():
        land = basics[land_type]
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
