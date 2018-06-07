#!/usr/bin/env python

import sys
import os
import mtginator.decks as decks
import mtginator.game as game

DECKS_DIR = 'data/decks/'


def run(turns, rounds, decks, goldfish=True):
    print("Running {} games for {} turns...".format(rounds, turns))
    if goldfish:
        print("In goldfish (single player) mode")
        nplayers = 1
    else:
        nplayers = 2
        print("Can only goldfish, sorry")
        sys.exit(1)

    ourplayers = []
    for n in range(0, nplayers):
        player = game.Player(name="Player%s" % n, deck=decks[n])
        ourplayers.append(player)

    for round in range(0, rounds):
        print("Round %s... FIGHT" % (round+1))
        for player in ourplayers:
            player.reset()
            print("%s has a %s card deck" % (player.name, len(player.deck.main)))
            player.mulligan(rules={})
            print("After mulligans player %s has %s cards." % (player.name, len(player.hand)))
            print("%s" % ([str(c) for c in player.hand]))
        game_state = game.Game(ourplayers, maxturns=turns)
        current_turn = 0
        (first_player, second_player) = game_state.play_or_draw()
        print("{} goes first".format(first_player.name))
        print("{} goes second".format(second_player.name))

        while(not game_state.is_over(turn=current_turn)):
            current_turn += 1
            print(game_state)
            first_player.take_turn()
            second_player.take_turn()


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Magic game sim')
    parser.add_argument('--turns', type=int, metavar='T', help="Number of turns each sim game runs", default=20)
    parser.add_argument('--rounds', type=int, metavar='N', help="Number of sim games", default=1)
    parser.add_argument('--decks', metavar='D', help='Decks to play', nargs='+', required=True)
    # parser.add_argument('updatefile', type=argparse.FileType('wb'))
    args = parser.parse_args()

    player_decks = []
    for deck_file in args.decks:
        d = decks.Deck()
        try:
            os.stat(deck_file)
            d.load_deck(deck_file)
        except OSError:
            try:
                os.stat(DECKS_DIR+deck_file)
                d.load_deck(DECKS_DIR+deck_file)
            except OSError:
                print("Could not find {} to load".format(deck_file))

        player_decks.append(d)

    if len(player_decks) < 1 or len(player_decks) > 2:
        print("Please supply 1 or 2 decks instead of {}".format(len(player_decks)))

    run(args.turns, args.rounds, player_decks)


if __name__ == '__main__':
    main()
else:
    pass
