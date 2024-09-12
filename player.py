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
        self.__deck.deck = self.__discard_pile.graveyard
        self.__discard_pile.graveyard = []

        # Shuffle the deck
        self.__deck.shuffle()

    def draw_card(self) -> None:
        """Player draws one card to their hand from the top of their deck"""
        # If no cards remain in deck, reshuffle discard pile into deck
        if self.__deck.deck == []:
            self.refill_deck()

        # Draw a card
        self.__hand.hand.append(self.__deck.deck.pop())

    def __draw_new_hand(self) -> None:
        """Draw 5 (or more, dependent on the actions taken during the player's
        previous turn) new cards at the start of the player's turn

        """
        for i in range(5 + self.hand.num_addl_cards):
            self.draw_card()

    def __discard_hand(self):
        """Discard any cards remaining in the player's hand at the end of a
        turn

        """
        self.__discard_pile.graveyard = self.__discard_pile.graveyard + self.__hand.hand
        self.__hand.hand = []

    def take_turn(self, supply_dict) -> None:
        """Completes the sequential actions needed for a player to take a turn

        Input:
        supply_dict -- a dictionary containing the names of the cards being used
                       and their counts

        """
        # If the player has no hand, draw a new hand
        if self.__hand.hand == []:
            self.__draw_new_hand()

        # Action phase
        not_done = True

        while not_done:
            print(self.hand)
            play_something = "Not sure yet"

            while play_something not in "yn" or play_something == "yn" or\
                  play_something == "":
                play_something = input("Do you want to play a card? (y/n)").lower()

            if play_something == "y":
                card_to_play = "Get out of jail free"

                while card_to_play not in supply_dict.keys() or\
                      card_to_play not in self.__hand.hand:
                    card_to_play = input("What is the name of the card you want"\
                                         + "to play?").capitalize().strip()

                for card in self.__hand.hand:
                    if card.name == card_to_play:
                        card.play()
                        break

                play_more_stuff = "It's unknowable"
                while play_more_stuff not in "yn" or play_more_stuff == "yn" or\
                      play_more_stuff == "":
                      play_more_stuff = input("Would you like to play another"\
                                              + " card? (y/n)").lower()

                # If the user is done playing cards, move to the buy phase
                if play_more_stuff == "n":
                    for card in self.__hand.hand:

                        # Well this is confusing......
                        if type(card) == "SupplyCard":
                            if card.type == 0:
                                card.play()