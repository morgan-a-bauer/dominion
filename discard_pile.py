"""discard_pile.py
Morgan Bauer and John Cetinkaya
28 March 2024

A class representing a player's discard pile in the game Dominion

"""
from card import Card
from random import shuffle

class DiscardPile:
    def __init__(self):
        self.__graveyard = []

    @property
    def graveyard(self) -> list:
        return self.__graveyard