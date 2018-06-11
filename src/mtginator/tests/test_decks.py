import pytest  # noqa

from mtginator import decks
DATA_DIR = 'data/decks/'
TEST_DECKS = {
    'Bolt.dec': {'main': 60, 'side': 0, 'lands': 20},
    'Savannah_Lions.dec': {'main': 60, 'side': 0, 'lands': 18},
    'UR_five.txt': {'main': 60, 'side': 15, 'lands': 24},
    'Sultai_FKK_3-0.txt': {'main': 40, 'side': 11, 'lands': 18}
}


def test_deck_load():
    ''' test loading decks '''
    for deck_file in TEST_DECKS.keys():

        deck = decks.Deck()
        deck.load_deck(DATA_DIR+deck_file)

        assert len(deck.main) == TEST_DECKS[deck_file]['main']
        assert len(deck.side) == TEST_DECKS[deck_file]['side']
        lands = [cc for cc in deck.main if 'Land' in cc.card_data['types']]
        assert len(lands) == TEST_DECKS[deck_file]['lands']


if __name__ == '__main__':
    test_deck_load()
