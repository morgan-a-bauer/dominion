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

    def refill_library(self) -> None:
        """Clears the player's discard pile into their library and shuffles the
        library

        """
        # Move discard pile to library
        self.__library = self.__discard_pile
        self.__discard_pile = []

        # Shuffle the library
        self.__library.shuffle()

    def draw_card(self) -> None:
        """Player draws one card to their hand from the top of their library"""
        # If no cards remain in library, reshuffle discard pile into library
        if self.__library == []:
            self.refill_library()

        # Draw a card
        self.__hand.append(self.__library.pop())

    def draw_new_hand(self, num_addl_cards = 0) -> None:
        """Draw 5 (or more, dependent on the actions taken during the player's
        previous turn) new cards at the start of the player's turn

        """
        for i in range(5 + num_addl_cards):
            self.draw_card()