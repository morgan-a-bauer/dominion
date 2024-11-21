"""card.py
Morgan Bauer and John Cetinkaya
27 March 2024

A class representing a generic card in the game Dominion. SupplyCard and
KingdomCard are child classes of Card

"""

class Card:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    def discard(self, player) -> None:
        """Allow the player to discard a card by removing it from the player's
        hand and placing it in the player's discard pile

        """
        # Remove card from player's hand
        player.hand.hand.remove(self)

        # Put the card in the player's discard pile
        player.discard_pile.graveyard.append(self)