"""rules.py
Morgan Bauer and John Cetinkaya
30 March 2024

A dictionary containing the rules of Dominion.

"""
# maps the category of rules to a number
rule_nums = {"GOAL":             1,
             "PREPARATION":      2,
             "PLAYING THE GAME": 3,}

# rules is of the form <category>: <rules>
rules = {1: "This is a game of building a deck of cards. The deck is" +\
            " your Dominion.\nIt contains your resources, victory" +\
            " points, and the things you can do.\nIt starts out a small" +\
            " sad collection of Estates and Coppers, but you hope\nby" +\
            " the end of the game it will be brimming with Gold," +\
            " Provinces, and the\ninhabitants and structures of your" +\
            " castle and kingdom.\n\nThe player with the most victory" +\
            " points in his Deck at game end wins.\n",
         2: "Each player starts the game with the same cards: 7 coppers &" +\
            " 3 estates.\n\nIn addition to the Trash, Treasure, Victory," +\
            " and Curse cards that are used\nin every game, the players" +\
            " also select 10 Kingdom cards and place 10 of\neach in face-up" +\
            " piles on the table.\n\nException: Kingdom Victory card piles" +\
            " (e.g. Gardens) have the same number\nas the Victory card piles" +\
            " (12 for a 3 or 4 player game and 8 for a 2 player game).\n\n" +\
            "For the first game, we recommend using the following 10 Kingdom" +\
            " cards: Cellar,\nMarket, Militia, Mine, Moat, Remodel, Smithy," +\
            " Village, Woodcutter, and Workshop.\nAt the end of the rules," +\
            " we list more suggestions for sets of 10 Kingdom cards.\n\n" +\
            "In later games, players can choose the 10 Kingdom cards using" +\
            " any method they agree on.\n",
         3: "Starting Player:\nRandomly determine the starting player." +\
            " Players take turns in clockwise order.\n\nTurn Overview:\n" +\
            "Each turn has three phases (A, B, and C) in the order shown:\n" +\
            "A) Action phase - the player may play an Action.\nB) Buy phase" +\
            " - the player may buy a card.\nC) Clean-up phase - the player" +\
            " must discard both played and unplayed cards\nand draws five" +\
            " new cards. After a player completes all three phases,\nhis" +\
            " turn ends.\n\nAction Phase:\nIn the Action phase, the player" +\
            " may play one Action card. Action cards\nare the Kingdom cards" +\
            " that say “Action” at the bottom of the card.\nSince players do" +\
            " not start the game with any Action cards in their\ninitial" +\
            " Decks of 10 cards, a player will not have any Actions to play" +\
            "\nduring his first 2 turns. Normally, a player may play only" +\
            " one Action card,\nbut this number may be modified by the Action" +\
            " cards that the player plays.\n\nTo play an Action, the player" +\
            " takes an Action card from his hand and lays it\nface-up in his" +\
            " play area. He announces which card he is playing and follows\n" +\
            "the instructions written on that card from top to bottom. The" +\
            " player may\nstill play an Action card even if he is not able to" +\
            " do everything the\nAction card tells him to do; but the player" +\
            " must do as much as he can.\nFurthermore, the player must fully" +\
            " resolve an Action card before playing\nanother one (if he is" +\
            " able to play another Action card). Detailed information\nabout" +\
            " card abilities can be found in the card descriptions at the" +\
            " end of\nthese rules. Any Action cards played remain in the" +\
            " player’s play area until\nthe Clean-up phase of the turn unless" +\
            " otherwise indicated on the card.\n\nThe Action phase ends when" +\
            " the player cannot or chooses not to play any more\nAction" +\
            " cards. Generally, a player can only play Action cards during" +\
            " the\nAction phase of his turn. However, Reaction cards are an" +\
            " exception to this\nrule as they can be used at other times." +\
            '\n\nCommon Terms Used on the Action Cards:\n\n"+X Card(s)" –' +\
            " the player immediately draws X number of cards from his Deck.\n" +\
            "               If there are not enough cards in his Deck, he" +\
            " draws as many\n               as he can, shuffles the Discard " +\
            " pile to form a new Deck,\n               and then draws the" +\
            " rest. If he still does not have enough\n               cards" +\
            " left after forming a new Deck, he just draws as many\n       " +\
            "        as he can.\n"}
if __name__ == "__main__":
    for cat, num in rule_nums.items():
        print(cat)
        print()
        print(rules[num])