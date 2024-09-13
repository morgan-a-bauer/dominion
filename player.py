"""player.py
Morgan Bauer and John Cetinkaya
28 March 2024

A class representing a player in the game Dominion

"""
from base_set import kingdom_cards, supply_cards
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

    def __print_current_totals_action(self):
        """Prints the current numbers of available actions, buys, and treasure
        for the player's action phase

        """
        actions = self.__hand.actions
        buys = self.__hand.buys
        treasure = self.__hand.treasure
        for cat_name, cat_value in zip(("Actions", "Buys", "Treasure"),
                                       (actions, buys, treasure)):
            print(f"{cat_name:<10}{cat_value:>3}")

    def __print_current_totals_buy(self):
        """Prints the current numbers of available buys and treasure
        for the player's buy phase

        """
        buys = self.__hand.buys
        treasure = self.__hand.treasure
        for cat_name, cat_value in zip(("Buys", "Treasure"),
                                       (buys, treasure)):
            print(f"{cat_name:<10}{cat_value:>3}")

    def __action_phase(self, supply_dict: dict) -> None:
        """Completes the necessary steps for a player's action phase

        Input:
        supply_dict -- a dictionary containing the names of the cards being used
                       and their counts

        """
        not_done = True

        while not_done:
            # Print current counts of available actions, buys, and treasure
            self.__print_current_totals_action()
            print()

            # Print the player's hand
            print(self.hand)
            print()

            play_something = "Not sure yet"

            while play_something not in "yn" or play_something == "yn" or\
                  play_something == "":
                play_something = input("Do you want to play a card? (y/n): ").lower().strip()

            if play_something == "y":
                card_to_play = "Get out of jail free"

                cards_in_hand = [card.name for card in self.__hand.hand]

                while card_to_play not in supply_dict.keys() or\
                      card_to_play not in cards_in_hand:
                    card_to_play = input("What is the name of the card you want"\
                                         + " to play?: ").capitalize().strip()

                self.__hand.play_card(card_to_play, self)

                # Print current counts of available actions, buys, and treasure
                print()
                self.__print_current_totals_action()
                print()

                # Print the player's hand
                print(self.hand)
                print()

                play_more_stuff = "It's unknowable"
                while play_more_stuff not in "yn" or play_more_stuff == "yn" or\
                      play_more_stuff == "":
                      play_more_stuff = input("Would you like to play another"\
                                              + " card? (y/n): ").lower().strip()

                # If the user is done playing cards, move to the buy phase
                if play_more_stuff == "n" or self.__hand.actions == 0 or\
                    len(self.__hand.hand) == 0:
                    not_done = False

            else:
                not_done = False

        # Count any remaining treasure
        for card in self.__hand.hand:

            # Well this is confusing...type(card) and card.type
            if type(card) == "SupplyCard":
                if card.type == 0:
                    self.__hand.play_card(card.name, self)

        return


    def __buy_phase(self, supply_dict: dict) -> None:
        """Completes the necessary steps for a player's action phase

        Input:
        supply_dict -- a dictionary containing the names of the cards being used
                       and their counts

        """
        # Print current counts of buys and treasure
        self.__print_current_totals_buy()
        print()

        print(f"{'Card name':^15}|{'Cost':^5}|{'Quantity':^5}")
        for card_name, card_count in supply_dict.items():
            if card_name in supply_cards.keys():
                cost = supply_cards[card_name][1]
            else:
                cost = kingdom_cards[card_name][1]

            print(f"{card_name:^15}|{cost:^5}|{card_count:^5}")

        card_to_buy = "Ace of spades"
        cost = float("inf")
        while card_to_buy not in supply_dict or supply_dict[card_to_buy] == 0 or\
              cost > self.__hand.treasure:
            card_to_buy = input("Which card would you like to buy? ").strip()

            try:
                if card_to_buy in supply_cards.keys():
                    cost = supply_cards[card_to_buy][1]
                else:
                    cost = kingdom_cards[card_to_buy][1]

            except Exception as e:
                pass

    def take_turn(self, supply_dict: dict) -> None:
        """Completes the sequential actions needed for a player to take a turn

        Input:
        supply_dict -- a dictionary containing the names of the cards being used
                       and their counts

        """
        # If the player has no hand, draw a new hand
        if self.__hand.hand == []:
            self.__draw_new_hand()

        # Action phase
        self.__action_phase(supply_dict)

        #Buy phase
        self.__buy_phase(supply_dict)