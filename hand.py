"""hand.py
Morgan Bauer and John Cetinkaya
27 March 2024

A class representing a player's hand in the game Dominion

"""
from card import Card

class Hand:
    def __init__(self, num_addl_actions = 0, num_addl_buys = 0,
                 num_addl_treasure = 0, addl_cards = []):
        self.__actions = 1 + num_addl_actions
        self.__buys = 1 + num_addl_buys
        self.__treasure = num_addl_treasure
        self.__hand = addl_cards

    @property
    def actions(self) -> int:
        return self.__actions

    @property
    def buys(self) -> int:
        return self.__buys

    @property
    def treasure(self) -> int:
        return self.__treasure

    @property
    def hand(self) -> list:
        return self.__hand

    def draw_card(self) -> None:
