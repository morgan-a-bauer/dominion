"""deck.py
Morgan Bauer and John Cetinkaya
28 March 2024

A class representing a player's deck in the game Dominion

"""
from supply_card import SupplyCard
from math import ceil
from random import shuffle

class Deck:
    def __init__(self):
        self.__deck = []

        # Populate initial deck with 7 coppers and 3 estates
        for i in range(7):
            self.__deck.append(SupplyCard("Copper"))

        for i in range(3):
            self.__deck.append(SupplyCard("Estate"))

        shuffle(self.__deck)

    @property
    def deck(self) -> list:
        return self.__deck

    @deck.setter
    def deck(self, new_deck) -> None:
        self.__deck = new_deck

    def __str__(self) -> str:
        """Overloads print() to print a textual representation of all cards
        in a player's deck

        """
        # Get the number of rows in the str representation of a card
        num_rows = len(self.__deck[0].get_row_lyst())

        # Calculate the number of rows of cards to print (5 cards per row)
        num_card_rows = ceil(len(self.__deck) / 5)

        rows = [[[] for i in range(num_rows)] for j in range(num_card_rows)]

        # Assemble list of string parts to be joined and returned
        for i in range(num_card_rows):
            for j in range(num_rows):
                for card in self.__deck[i * 5: i * 5 + 5]:
                    rows[i][j].append(card.get_row_lyst()[j])

        # Freaking unreadable, but you've gotta admit this is slick
        # Seriously one of the most ridiculous lines of code though
        return "\n\n".join(["\n".join(["  ".join(row) for row in rows[i]]) for i in range(len(rows))])

if __name__ == "__main__":
    test_lib1 = Deck()
    print(test_lib1)