"""kingdom_card.py
Morgan Bauer and John Cetinkaya
28 March 2024

A class representing a kingdom card in the game Dominion

"""
from base_set import kingdom_cards as kc
from card import Card

class KingdomCard(Card):
    def __init__(self):
        Card.__init__()
        self.__type = int(kc[self.__name][0])
        self.__cost = int(kc[self.__name][1])
        self.__actions = int(kc[self.__name][2])
        self.__buys = int(kc[self.__name][3])
        self.__cards = int(kc[self.__name][4])
        self.__treasure = int(kc[self.__name][5])

    @property
    def type(self) -> int:
        return self.__type

    @property
    def cost(self) -> int:
        return self.__cost

    @property
    def actions(self) -> int:
        return self.__actions

    @property
    def buys(self) -> int:
        return self.__buys

    @property
    def cards(self) -> int:
        return self.__cards

    @property
    def treasure(self) -> int:
        return self.__treasure