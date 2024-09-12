"""rules.py
Morgan Bauer and John Cetinkaya
30 March 2024

A dictionary containing the rules of Dominion.

"""
# maps the category of rules to a number
rule_nums = {"GOAL":             1,
             "PREPARATION":      2,
             "PLAYING THE GAME": 3,
             "GAME END": 4,
             "ADDITIONAL RULES": 5,
             "PLAY": 6}

# rules is of the form <category>: <rules>
rule_dict = {1: "This is a game of building a deck of cards. The deck is" +\
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
                '\n\nCommon Terms Used on the Action Cards:\n\"+X Card(s)"   –' +\
                " the player immediately draws X number of cards from his Deck.\n" +\
                "                 If there are not enough cards in his Deck, he" +\
                " draws as many\n                 as he can, shuffles the Discard " +\
                " pile to form a new Deck,\n                 and then draws the" +\
                " rest. If he still does not have enough\n                 cards" +\
                " left after forming a new Deck, he just draws as many\n       " +\
                '          as he can.\n"+X Action(s)" – the player may play X' +\
                " number of additional Actions this turn.\n                " +\
                " +X Action(s) adds to the number of Actions that can be played" +\
                "\n                 in the Action phase. It does not mean play" +\
                " another Action\n                 immediately. The instructions" +\
                " on the current Action card must\n                 be completed" +\
                " before playing any additional Actions. The player\n           " +\
                "      must complete all of his Actions before he moves on to the" +\
                " Buy\n                 phase of his turn. If a card gives the" +\
                " player more than one\n                 additional Action, he" +\
                " may keep track of the number of Actions\n                 " +\
                'he has remaining out loud.\n"+(X)"         – the player has X' +\
                " number of additional coins to spend in the Buy\n              " +\
                "   phase. The player does not take additional Treasure cards" +\
                ' for\n                 these coins\n"+1 Buy"       – the player' +\
                " may buy an additional card from the Supply during\n           " +\
                "      the Buy phase of his turn. +1 Buy adds to a player’s" +\
                " potential\n                 Buys, it does not allow the player" +\
                " to buy a card during the\n                 Action phase.\n" +\
                '"Discard"      – unless otherwise specified, discarded cards' +\
                " are from the\n                 player’s hand. When a player" +\
                " discards a card, he places\n                 the discarded" +\
                " card face-up onto his Discard pile. When\n                " +\
                " discarding several cards at once, the player need not show all" +\
                "\n                 cards he is discarding to his opponents, but" +\
                " player may need to\n                 show how many cards he is" +\
                " discarding (for example, when playing\n                 the" +\
                " Cellar). The top card of a player’s Discard pile is always" +\
                '\n                 visible.\n"Trash”        – when a player' +\
                " trashes a card, he places it in the Trash pile,\n             " +\
                "    not his Discard pile. Trashed cards are not returned to the" +\
                "\n                 Supply and are not available for purchase." +\
                '\n"Gain”         – when a player gains a card, he takes the' +\
                " gained card (usually\n                 from the Supply) and" +\
                " puts it onto his Discard pile (unless the\n                 " +\
                "card says to put it elsewhere). The player does not get to use" +\
                "\n                 the card when he gains it." +\
                '\n“Reveal”       – when a player reveals a card, he shows a card' +\
                " to all players and\n                 then returns it to" +\
                " wherever it came from (unless instructed\n                 " +\
                "specifically to put it elsewhere). If the player is required to" +\
                "\n                 reveal cards from the top of his Deck, and" +\
                " he does not have enough\n                 cards, he shuffles" +\
                " in order to reveal the required number of cards.\n" +\
                '“Set Aside”    – when a player sets aside a card, he' +\
                " places it face-up on the table\n                 (unless" +\
                " otherwise indicated) without following any instructions on" +\
                "\n                 the card. An Action that requires a player to" +\
                " set aside cards will\n                 instruct him on what to" +\
                " do with these cards.\n\nBuy Phase:\nIn the Buy phase, the" +\
                " player can gain one card from the Supply by paying its" +\
                " cost.\nAny card that is in the Supply may be purchased" +\
                " (Treasure, Victory, Kingdom, and\neven Curse cards). The" +\
                " player may not purchase cards from the Trash pile. Normally," +\
                "\na player may buy only one card, but he may buy more if he" +\
                " played certain cards\nearlier in his Action phase.\n\n" +\
                "The cost of a card is in its lower left corner. The player may" +\
                " play some or all of\nthe Treasure cards from his hand to his" +\
                " play area and add to their value the coins \nprovided by" +\
                " Action cards played this turn. The player may then gain any" +\
                " card in the\nSupply of equal or lesser value. He takes the" +\
                " purchased card from its Supply pile\nand places it face-up on" +\
                " his Discard pile. He my not use the ability of the card" +\
                "\nwhen it is gained.\n\nIf the player has multiple Buys, he" +\
                " combines Treasure cards and any coins available\nfrom Action" +\
                " cards to pay for all of the purchases. For example, if Tyler" +\
                " has +1 Buy\nand 6 coins provided by two Gold cards, he can buy" +\
                " a Cellar costing 2, placing it\nface-up in his Discard pile." +\
                " Then, he can buy a Smithy with the remaining 4 coins\nand" +\
                " place that face-up in his Discard pile. If he wants to use all" +\
                " 6 coins to buy one\ncard, he can buy a Copper (for free) with" +\
                " his second Buy or not buy a second card." +\
                "\nPlayers do not have to use any or all of their Buys.\n\n" +\
                "The Treasure cards remain in the play area until the Clean-up" +\
                " phase. Treasure cards\nwill be used multiple times during the" +\
                " game. Although they are discarded during the\nClean-up phase," +\
                " the player will draw them again as his Discard pile is" +\
                " shuffled into\na new Deck. Thus, Treasure cards are a source" +\
                " of income, not a resource that is used\nup when played." +\
                " When played, Coppers are worth 1 coin, Silvers are worth 2" +\
                " coins,\nand Golds are worth 3 coins.\n\nClean-up Phase:\nAll" +\
                " cards gained this turn should already be in the player’s" +\
                " Discard pile. The player\nplaces any cards that are in his" +\
                " play area (Action cards that have been played in the\nAction" +\
                " phase as well as Treasure cards that have been played in the" +\
                " Buy phase) and any\ncards remaining in his hand onto his" +\
                " Discard pile. Although the player need not show\nthe cards" +\
                " remaining in his hand to his opponents, since he places the" +\
                " cards in the\nDiscard pile face-up, his opponents will always" +\
                " be able to see the top-most card of\nhis Discard pile." +\
                "\n\nThen, the player draws a new hand of 5 cards from his Deck." +\
                " If there are not enough\ncards in his Deck, he draws as many" +\
                " as he can, shuffles his Discard pile to form a\nnew face-down" +\
                " Deck, and then draws the rest of his new hand.\n\n" +\
                "Once the player has drawn a new hand of 5 cards, the next" +\
                " player starts his turn.\nTo speed play, players may begin" +\
                " their turns while previous players are completing\ntheir" +\
                " Clean-up phases. When someone plays an Attack card, the" +\
                " players must complete\ntheir Clean-up phases in order to" +\
                " properly resolve the Attack.\n",
            4: "The game ends at the end of any player’s turn when either:\n" +\
                "1) the Supply pile of Province cards is empty or\n" +\
                "2) any 3 Supply piles are empty.\n\nEach player puts all of his" +\
                " cards into his Deck and counts the victory points on all\nthe" +\
                " cards he has.\n\nThe player with the most victory points wins." +\
                " If the highest scores are tied at the\nend of the game, the" +\
                " tied player who has had the fewest turns wins the game. If the" +\
                "\ntied players have had the same number of turns, they rejoice" +\
                " in their shared victory.\n",
            5: "Each player has his own Dominion, which he builds from cards in" +\
                " the supply. During the\ngame, a player’s cards are usually in" +\
                " three parts: his Deck (which he draws cards from),\nhis hand," +\
                " and his Discard pile. The player draws cards from his own Deck" +\
                " and discards\ncards to his own Discard pile. When his Deck" +\
                " is exhausted and the player needs to draw\nor reveal cards" +\
                " from his Deck, he shuffles his Discard pile to reform his" +\
                " Deck. He does\nnot shuffle his Discard pile until he needs" +\
                " to reveal or draw a card from his Deck and\ncannot. At any" +\
                " point in the game, if a player has to draw or reveal more" +\
                " cards than are\nremaining in his Deck, he must draw or reveal" +\
                " as many as he can and then shuffle his\nface-up Discard pile" +\
                " to form a new face-down Deck. Then, he draws or reveals the" +\
                " remaining\nnumber of cards from his newly shuffled Deck.\n\n" +\
                "A player places cards he Buys or otherwise acquires during the" +\
                " game on his Discard pile\nunless he is specifically directed" +\
                " to place them elsewhere.\n\nAt the end of a player’s turn," +\
                " he places all the cards he played and those still in his\n" +\
                "hand on his Discard pile.\n\nA player is allowed to count how" +\
                " many cards are left in his Deck, but not in his Discard\npile." +\
                " A player may not look through his Deck or his Discard pile." +\
                " A player may look\nthrough the Trash pile, and players may" +\
                " count the number of cards left in any pile in\nthe Supply.\n\n" +\
                "If an ability of a card affects multiple players, and the order" +\
                " matters, resolve that\nability for each affected player in" +\
                " turn order, starting with the player whose turn it is.\n\n" +\
                "During each turn, a player is allowed 1 Action and 1 Buy," +\
                " but may be entitled to more based\non Action cards played." +\
                " The instructions written on all the action cards alter the" +\
                " rules of\nthe game by, for example, allowing the player to draw" +\
                " more cards from his Deck, play more\nAction cards in the Action" +\
                " phase, use more coins for the Buy phase, Buy extra cards in" +\
                " the\nBuy phase and so on.\n\nWhen an Action card allows a player" +\
                " to gain a card costing up to a certain value, he may not\nadd" +\
                " from his hand or other action cards to gain a higher-valued card"}

if __name__ == "__main__":
    for cat, num in rule_nums.items():
        print(cat)
        print()
        print(rule_dict[num])