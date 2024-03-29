"""card.py
Morgan Bauer and John Cetinkaya
27 March 2024

A class representing a generic card in the game Dominion. SupplyCard and
KingdomCard are child classes of Card

"""

class Card:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name