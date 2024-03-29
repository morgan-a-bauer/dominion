"""supply_card.py
Morgan Bauer and John Cetinkaya
28 March 2024

A class representing a supply card in the game Dominion

"""
from base_set import supply_cards as sc
from card import Card

class SupplyCard(Card):
    def __init__(self):
        Card.__init()
        self.__cost = int(sc[self.__name][1])
        self.__value = int(sc[self.__name][2:])

    @property
    def cost(self) -> int:
        return self.__cost

    @property
    def value(self) -> int:
        return self.__value