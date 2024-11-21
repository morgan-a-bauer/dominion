"""hand.py
Morgan Bauer and John Cetinkaya
27 March 2024

A class representing a player's hand in the game Dominion

"""
from kingdom_card import KingdomCard
from math import ceil

class Hand:
    def __init__(self, num_addl_actions = 0, num_addl_buys = 0,
                 num_addl_treasure = 0, num_addl_cards = 0):
        self.__actions = 1 + num_addl_actions
        self.__buys = 1 + num_addl_buys
        self.__treasure = num_addl_treasure
        self.__num_addl_cards = num_addl_cards
        self.__hand = []

    @property
    def actions(self) -> int:
        return self.__actions

    @actions.setter
    def actions(self, new_actions) -> None:
        self.__actions = new_actions

    @property
    def buys(self) -> int:
        return self.__buys

    @buys.setter
    def buys(self, new_buys) -> None:
        self.__buys = new_buys

    @property
    def treasure(self) -> int:
        return self.__treasure

    @treasure.setter
    def treasure(self, new_treasure) -> None:
        self.__treasure = new_treasure

    @property
    def num_addl_cards(self) -> int:
        return self.__num_addl_cards

    @num_addl_cards.setter
    def num_addl_cards(self, new_addl_cards) -> None:
        self.__num_addl_cards = new_addl_cards

    @property
    def hand(self) -> list:
        return self.__hand

    @hand.setter
    def hand(self, new_hand) -> None:
        self.__hand = new_hand

    def play_card(self, card_name: str, player):
        """Lets the player play a card from the hand

        Input:
        card_name -- the name of the card to play
        player -- the player object that played the card

        """
        for card in self.__hand:
            if card.name == card_name:
                card.play(player)
                break

    def __str__(self) -> str:
        """Overloads print() to print a textual representation of all cards
        in a player's hand

        """
        # Get the number of rows in the str representation of a card
        num_rows = len(self.__hand[0].get_row_lyst())

        # Calculate the number of rows of cards to print (5 cards per row)
        num_card_rows = ceil(len(self.__hand) / 5)

        # I know you love this nonsense
        rows = [[[] for i in range(num_rows)] for j in range(num_card_rows)]

        # Assemble list of string parts to be joined and returned
        for i in range(num_card_rows):
            for j in range(num_rows):
                for card in self.__hand[i * 5: i * 5 + 5]:
                    rows[i][j].append(card.get_row_lyst()[j])

        # Freaking unreadable, but you've gotta admit this is slick
        # Seriously one of the most ridiculous lines of code though
        return "\n\n".join(["\n".join(["  ".join(row) for row in rows[i]]) for i in range(len(rows))])

if __name__ == "__main__":
    test_cards = []
    for card_name in ["Moneylender", "Village", "Spy", "Militia", "Moat",
                      "Market", "Gardens"]:
        test_card = KingdomCard(card_name)
        test_cards.append(test_card)
    test_hand = Hand(addl_cards = test_cards)
    print(test_hand)