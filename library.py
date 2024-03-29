"""library.py
Morgan Bauer and John Cetinkaya
28 March 2024

A class representing a player's library in the game Dominion

"""
from card import Card
from random import shuffle

class Library:
    def __init__(self):
        self.__lib = []

    @property
    def lib(self) -> list:
        return self.__lib