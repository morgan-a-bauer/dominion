"""kingdom_card.py
Morgan Bauer and John Cetinkaya
28 March 2024

A class representing a kingdom card in the game Dominion

"""
from base_set import kingdom_cards as kc
from card import Card
from special_actions import actions

class KingdomCard(Card):
    def __init__(self, name):
        Card.__init__(self, name)
        card_info = kc[self.name]
        self.__type = int(card_info[0])
        self.__cost = int(card_info[1])
        self.__actions = int(card_info[2])
        self.__buys = int(card_info[3])
        self.__cards = int(card_info[4])
        self.__treasure = int(card_info[5])
        if len(card_info) > 6:
            self.__special_actions = [int(action) for action in card_info[6:]]
        else:
            self.__special_actions = []

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

    def play(self, player) -> None:
        """Add attributes of the card to the running totals of a given hand.
        Carry out any special actions

        Input:
        player -- the player whose hand the card belongs to

        """
        hand = player.hand
        hand.actions += self.__actions - 1
        hand.buys += self.__buys
        hand.treasure += self.__treasure
        for i in range(self.__cards):
            player.draw_card()

        self.discard(player)

        #TODO: Implement special actions
        for sa in self.__special_actions:
            sa = actions[sa]
            if len(sa) == 1:
                sa[0](player)
            else:
                sa[0](player, sa[1:])

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

        # The type of action the card represents
        type = "Action"
        if self.__type == 1:
            type += " - Attack"

        elif self.__type == 2:
            type += " - Reaction"

        elif self.__type == 3:
            type = "Victory"

        # Cost of the cards
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