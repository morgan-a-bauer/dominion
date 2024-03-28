"""player.py
Morgan Bauer and John Cetinkaya
28 March 2024

A class representing a player in the game Dominion

"""
from card import Card
from discard_pile import DiscardPile
from hand import Hand
from library import Library
from random import shuffle

class Player:
    def __init__(self):
        self.__library = Library()
        self.__discard_pile = DiscardPile()
        self.__hand = Hand()

    @property
    def library(self) -> list:
        return self.__library

    @property
    def discard_pile(self) -> list:
        return self.__discard_pile

    @property
    def hand(self) -> list:
        return self.__hand