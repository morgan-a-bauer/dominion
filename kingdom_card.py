"""kingdom_card.py
Morgan Bauer and John Cetinkaya
28 March 2024

A class representing a kingdom card in the game Dominion

"""
from base_set import kingdom_cards as kc
from card import Card

class KingdomCard(Card):
    def __init__(self, name):
        Card.__init__(self, name)
        self.__type = int(kc[self.name][0])
        self.__cost = int(kc[self.name][1])
        self.__actions = int(kc[self.name][2])
        self.__buys = int(kc[self.name][3])
        self.__cards = int(kc[self.name][4])
        self.__treasure = int(kc[self.name][5])

    @property
    def type(self) -> int:
        return self.__type

    @property
    def cost(self) -> int:
        return self.__cost

    @property
    def actions(self) -> int:
        return self.__actions

    @property
    def buys(self) -> int:
        return self.__buys

    @property
    def cards(self) -> int:
        return self.__cards

    @property
    def treasure(self) -> int:
        return self.__treasure

    def get_row_lyst(self) -> list:
        """Builds a list of the rows in the textual representation of a card.
        This is primarily helpful when printing all cards in a player's hand

        """
        # Ensures proper use of singular/plural; uses empty string if NA
        # Number of additional actions the player gets for the current turn
        actions = "+" + str(self.__actions)
        if self.__actions == 0:
            actions = ""
        elif self.__actions == 1:
            actions += " Action"
        else:
            actions += " Actions"

        # Number of additional buys the player gets for the current turn
        buys = "+" + str(self.__buys)
        if self.__buys == 0:
            buys = ""
        elif self.__actions == 1:
            buys += " Buy"
        else:
            buys += " Buys"

        # Number of additional cards the player draws for the current turn
        cards = "+" + str(self.__cards)
        if self.__cards == 0:
            cards = ""
        elif self.__cards == 1:
            cards += " Card"
        else:
            cards += " Cards"

        # Number of additional treasure the player recieves for the current turn
        treasure = "+(" + str(self.__treasure) + ")"
        if self.__treasure == 0:
            treasure = ""

        type = "Action"
        if self.__type == 1:
            type += " - Attack"
        elif self.__type == 2:
            type += " - Reaction"
        elif self.__type == 3:
            type = "Victory"

        cost = "(" + str(self.__cost) + ")"

        row_lyst = ["+-----------------+", f"|{self.name:^17}|",
                   "+-----------------+", f"|{actions:^17}|",
                   f"|{buys:^17}|", f"|{cards:^17}|", f"|{treasure:^17}|",
                   "+-----------------+", f"|{type:^17}|",
                   "+-----------------+", f"|{cost:<17}|", "+-----------------+"]

        return row_lyst

    def __str__(self) -> str:
        """Overloads print() to display as output a string representation of a
        KingdomCard

        """
        rows = self.get_row_lyst()
        return "\n".join(rows)

if __name__ == "__main__":
    test_cards = []
    for card_name in ["Moneylender", "Village", "Spy", "Militia", "Moat",
                      "Market"]:
        test_card = KingdomCard(card_name)
        test_cards.append(test_card)
    for card in test_cards:
        print(card)
        print()
        print()