"""hand.py
Morgan Bauer and John Cetinkaya
27 March 2024

A class representing a player's hand in the game Dominion

"""
from kingdom_card import KingdomCard

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

    def __str__(self) -> str:
        """Overloads print() to print a textual representation of all cards
        in a player's hand

        """
        # TODO Modify this to work for more than six cards
        # Get the number of rows in the str representation of a card
        num_rows = len(self.__hand[0].get_row_lyst())
        rows = [[] for i in range(num_rows)]
        for i in range(num_rows):
            for card in self.__hand:
                rows[i].append(card.get_row_lyst()[i])

        # Freaking unreadable, but you've gotta admit this is slick
        return "\n".join(["  ".join(row) for row in rows])

if __name__ == "__main__":
    test_cards = []
    for card_name in ["Moneylender", "Village", "Spy", "Militia", "Moat",
                      "Market"]:
        test_card = KingdomCard(card_name)
        test_cards.append(test_card)
    test_hand = Hand(addl_cards = test_cards)
    print(test_hand)