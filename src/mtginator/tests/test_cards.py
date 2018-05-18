import pytest  # noqa

from mtginator import cards

data = [
    {
        '{2}{G}': {
            'colorless': 2,
            'G': 1
        }
    },
    {
        '{3}{B}{B}': {
            'colorless': 3,
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
            'colorless': 4,
        }
    },
    {
        '{U/R}': {
            'U/R': 1
        }
    },
    {
        '{U/W}{U/W}{2}': {
            'colorless': 2,
            'U/W': 2
        }
    },
    { 
        '{2}{G}{G}{W}{W}{U}{U}': {
            'colorless': 2,
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
        '{3}{R}{R/P}': {
            'colorless': 3,
            'R': 1,
            'R/P': 1
        }
    }
]

bad_data = [
    '{H}',
]


def test_cards():

    for sample in data:
        for cost_str in sample.keys():
            cost = cards.Cost(fromString=cost_str)
            assert cost.mana == sample[cost_str]

    print("%s good data tests passed" % len(data))

    for bad in bad_data:
        try:
            cost = cards.Cost(fromString=bad)
            assert(False)
        except Exception:
            assert(True)

    print("%s bad data tests passed" % len(bad_data))


if __name__ == '__main__':
    test_cards()
