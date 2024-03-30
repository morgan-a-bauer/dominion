"""trash.py
Morgan Bauer and John Cetinkaya
30 March 2024

A class representing the trash pile in the game Dominion

"""

class Trash:
    def __init__(self):
        self.__pile = []

    @property
    def pile(self) -> list:
        return self.__pile

    def trash_card(self, card) -> None:
        self.__pile.append(card)