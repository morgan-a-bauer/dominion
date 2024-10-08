"""supply_card.py
Morgan Bauer and John Cetinkaya
28 March 2024

A class representing a supply card in the game Dominion

"""
from base_set import supply_cards as sc
from card import Card

class SupplyCard(Card):
    def __init__(self, name):
        Card.__init__(self, name)
        self.__type = int(sc[self.name][0])
        self.__cost = int(sc[self.name][1])
        self.__value = int(sc[self.name][2:])

    @property
    def type(self) -> int:
        return self.__type

    @property
    def cost(self) -> int:
        return self.__cost

    @property
    def value(self) -> int:
        return self.__value

    def play(self, player):
        """Add attributes of the card to the running totals of a given hand.
        Carry out any special actions

        Input:
        player -- the player whose hand the card belongs to

        """
        hand = player.hand

        # If the card is a treasure card, add its value to a running total
        if self.__type == 0:
            hand.treasure += self.__value

        player.discard_pile.graveyard.append(self)

    def get_row_lyst(self) -> list:
        """Builds a list of the rows in the textual representation of a card.
        This is primarily helpful when printing all cards in a player's hand

        """
        cost = f"({self.__cost})"

        # Display treasure values in parentheses
        if self.__type == 0:
            type = "Treasure"
            value = f"({self.__value})"

        # Display victory values alone
        elif self.__type == 1:
            type = "Victory"
            value = str(self.__value)

        row_lyst = ["+-----------------+", f"|{self.name:^17}|",
                   "+-----------------+", f"|                 |",
                   f"|{value:^17}|", f"|                 |",
                   f"|                 |", "+-----------------+",
                   f"|{type:^17}|", "+-----------------+", f"|{cost:<17}|",
                   "+-----------------+"]

        return row_lyst

    def __str__(self) -> str:
        """Overloads print() to display as output a string representation of a
        SupplyCard

        """
        rows = self.get_row_lyst()
        return "\n".join(rows)

if __name__ == "__main__":
    test_cards = []
    for card_name in ["Copper", "Silver", "Gold", "Estate", "Duchy", "Province"]:
        test_card = SupplyCard(card_name)
        test_cards.append(test_card)
    for card in test_cards:
        print(card)
        print()
        print()