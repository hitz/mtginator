import pytest  # noqa

from mtginator import decks
data_dir = 'data/decks/'
test_decks = {
    'Bolt.dec': {'main': 60, 'side': 0, 'lands': 20},
    'Savannah_Lions.dec': {'main': 60, 'side': 0, 'lands': 18},
    'UR_five.txt': {'main': 60, 'side': 15, 'lands': 20},
    'Sultai_FKK_3-0.txt': {'main': 40, 'side': 11, 'lands': 18}
}


def test_deck_load():

    for deck_file in test_decks.keys():

        deck = decks.Deck()
        deck.load_deck(data_dir+deck_file)

        assert(len(deck.main) == test_decks[deck_file]['main'])
        assert(len(deck.side) == test_decks[deck_file]['side'])
        assert(len([l for l in deck.main if 'Land' in l.cardData['types']]) == test_decks[deck_file['lands']])


if __name__ == '__main__':
    test_deck_load()
