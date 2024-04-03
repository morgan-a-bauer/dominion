"""discard_pile.py
Morgan Bauer and John Cetinkaya
28 March 2024

A class representing a player's discard pile in the game Dominion

"""
from math import ceil
from random import shuffle

class DiscardPile:
    def __init__(self):
        self.__graveyard = []

    @property
    def graveyard(self) -> list:
        return self.__graveyard

    def __str__(self) -> str:
        """Overloads print() to print a textual representation of all cards
        in a player's deck

        """
        # Get the number of rows in the str representation of a card
        num_rows = len(self.__graveyard[0].get_row_lyst())

        # Calculate the number of rows of cards to print (5 cards per row)
        num_card_rows = ceil(len(self.__graveyard) / 5)

        rows = [[[] for i in range(num_rows)] for j in range(num_card_rows)]

        # Assemble list of string parts to be joined and returned
        for i in range(num_card_rows):
            for j in range(num_rows):
                for card in self.__graveyard[i * 5: i * 5 + 5]:
                    rows[i][j].append(card.get_row_lyst()[j])

        # Freaking unreadable, but you've gotta admit this is slick
        # Seriously one of the most ridiculous lines of code though
        return "\n\n".join(["\n".join(["  ".join(row) for row in rows[i]]) for i in range(len(rows))])