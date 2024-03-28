"""supply.py
Morgan Bauer and John Cetinkaya
28 March 2024

A class representing the game's supply in the game Dominion

"""
from base_set import kingdom_cards as kc
from random import choice

class Supply:
    def __init__(self, num_players: int, cards_used = []):
        """Stores a dictionary with card names as keys and the number of cards
        available in the supply as values

        """
        self.__counts = {"Copper": 60,
                         "Silver": 40,
                         "Gold":   30}

        if num_players == 2:
            self.__counts["Estate"] = 8
            self.__counts["Duchy"] = 8
            self.__counts["Province"] = 8
            self.__counts["Curse"] = 10

        else:
            self.__counts["Estate"] = 12
            self.__counts["Duchy"] = 12
            self.__counts["Province"] = 12

            if num_players == 3:
                self.__counts["Curse"] = 20

            else:
                self.__counts["Curse"] = 30

        if cards_used == []:
            for i in range(10):
                card_name = choice(kc.keys())
                while card_name in kc.keys():
                    card_name = choice(kc.keys())
                self.__counts[card_name] = 10

    @property
    def counts(self):
        return self.__counts