"""player.py
Morgan Bauer and John Cetinkaya
28 March 2024

A class representing a player in the game Dominion

"""
from card import Card
from discard_pile import DiscardPile
from hand import Hand
from deck import Deck
from random import shuffle

class Player:
    def __init__(self, name):
        self.__name = name
        self.__deck = Deck()
        self.__discard_pile = DiscardPile()
        self.__hand = Hand()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def deck(self) -> list:
        return self.__deck

    @property
    def discard_pile(self) -> list:
        return self.__discard_pile

    @property
    def hand(self) -> list:
        return self.__hand

    def refill_deck(self) -> None:
        """Clears the player's discard pile into their deck and shuffles the
        deck

        """
        # Move discard pile to deck
        self.__deck = self.__discard_pile
        self.__discard_pile = []

        # Shuffle the deck
        self.__deck.shuffle()

    def draw_card(self) -> None:
        """Player draws one card to their hand from the top of their deck"""
        # If no cards remain in deck, reshuffle discard pile into deck
        if self.__deck == []:
            self.refill_deck()

        # Draw a card
        self.__hand.append(self.__deck.pop())

    def draw_new_hand(self, num_addl_cards = 0) -> None:
        """Draw 5 (or more, dependent on the actions taken during the player's
        previous turn) new cards at the start of the player's turn

        """
        for i in range(5 + num_addl_cards):
            self.draw_card()