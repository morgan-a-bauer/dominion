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

        Input:
        num_players -- the number of players playing the game
        cards_used  -- (optional) players may choose to provide a list of
                       kingdom cards to be used

        """

        # Treasure cards
        self.__supply_counts = {"Copper": 60 - 7 * num_players,
                         "Silver": 40,
                         "Gold":   30}

        # Victory cards for a 2-player game
        if num_players == 2:
            vc_num = 8
            self.__supply_counts["Curse"] = 10

        # Victory cards for a 2- or 4-player game
        else:
            vc_num = 12

            if num_players == 3:
                self.__supply_counts["Curse"] = 20

            else:
                self.__supply_counts["Curse"] = 30

        self.__supply_counts["Estate"] = vc_num
        self.__supply_counts["Duchy"] = vc_num
        self.__supply_counts["Province"] = vc_num

        # If players do not provide kingdom cards to use
        if cards_used == []:

            # Choose 10 random cards without replacement
            for i in range(10):
                card_name = choice(list(kc.keys()))
                while card_name in self.__supply_counts:
                    card_name = choice(list(kc.keys()))

                # Kingdom Cards of type Victory use the appropriate number
                # (rather than 10)
                if kc[card_name][0] == 3:
                    self.__supply_counts[card_name] = vc_num
                else:
                    self.__supply_counts[card_name] = 10

        # If players do provide kingdom cards to use
        else:
            for i in range(10):
                # Check for complete or partial list of unique kingdom cards
                if i < len(cards_used) and cards_used[i] not in\
                                           self.__supply_counts.keys():
                    card_name = cards_used[i]

                # If a complete list is not provided, randomly choose the rest
                # without replacement
                else:
                    card_name = choice(list(kc.keys()))
                    while card_name in self.__supply_counts:
                        card_name = choice(list(kc.keys()))

                # Kingdom Cards of type Victory use the appropriate number
                # (rather than 10)
                if int(kc[card_name][0]) == 3:
                    self.__supply_counts[card_name] = vc_num
                else:
                    self.__supply_counts[card_name] = 10


    @property
    def supply_counts(self):
        return self.__supply_counts

    def __str__(self) -> str:
        supply_str = ""
        for card, num in self.__supply_counts.items():
            supply_str += f"{card:<12}:{num:>2}\n"

        return supply_str

if __name__ == "__main__":
    # All these test cases were written before I wrote __str__(), so that was
    # kind of an oversight, but at least I didn't write a __str__() method
    # and then print everything else out, so...

    # Test 2 players, no cards provided
    print("2 players, no cards provided")
    num_plrs = 2
    test_supply1 = Supply(num_plrs)

    for card, num in test_supply1.supply_counts.items():
        print(f"{card:<12}:{num:>2}")

    print()
    print()

    # Test 2 players, all cards provided and unique
    print("2 players, all cards provided and unique")
    test_supply2 = Supply(num_plrs, ["Village", "Gardens", "Market", "Spy",
                                     "Smithy", "Witch", "Militia", "Moat",
                                     "Throne Room", "Laboratory"])

    for card, num in test_supply2.supply_counts.items():
        print(f"{card:<12}:{num:>2}")

    print()
    print()

    # Test 2 players, all cards provided and not unique
    print("2 players, all cards provided and not unique")
    test_supply3 = Supply(num_plrs, ["Village", "Village", "Gardens", "Gardens",
                                     "Market", "Market", "Spy", "Spy", "Witch",
                                     "Witch"])

    for card, num in test_supply3.supply_counts.items():
        print(f"{card:<12}:{num:>2}")

    print()
    print()

    # Test 2 players, not all cards provided
    print("2 players, not all cards_provided")
    test_supply4 = Supply(num_plrs, ["Village", "Market", "Witch"])

    for card, num in test_supply4.supply_counts.items():
        print(f"{card:<12}:{num:>2}")

    print()
    print()

    # Test 3 players, no cards provided
    print("3 players, no cards provided")
    num_plrs = 3
    test_supply5 = Supply(num_plrs)

    for card, num in test_supply5.supply_counts.items():
        print(f"{card:<12}:{num:>2}")

    print()
    print()

    # Test 3 players, all cards provided and unique
    print("3 players, all cards provided and unique")
    test_supply6 = Supply(num_plrs, ["Village", "Gardens", "Market", "Spy",
                                     "Smithy", "Witch", "Militia", "Moat",
                                     "Throne Room", "Laboratory"])

    for card, num in test_supply6.supply_counts.items():
        print(f"{card:<12}:{num:>2}")

    print()
    print()

    # Test 3 players, all cards provided and not unique
    print("3 players, all cards provided and not unique")
    test_supply7 = Supply(num_plrs, ["Village", "Village", "Gardens", "Gardens",
                                     "Market", "Market", "Spy", "Spy", "Witch",
                                     "Witch"])

    for card, num in test_supply7.supply_counts.items():
        print(f"{card:<12}:{num:>2}")

    print()
    print()

    # Test 3 players, not all cards provided
    print("3 players, not all cards_provided")
    test_supply8 = Supply(num_plrs, ["Village", "Market", "Witch"])

    for card, num in test_supply8.supply_counts.items():
        print(f"{card:<12}:{num:>2}")

    print()
    print()

    # Test 4 players, no cards provided
    print("4 players, no cards provided")
    num_plrs = 4
    test_supply9 = Supply(num_plrs)

    for card, num in test_supply9.supply_counts.items():
        print(f"{card:<12}:{num:>2}")

    print()
    print()

    # Test 4 players, all cards provided and unique
    print("4 players, all cards provided and unique")
    test_supply10 = Supply(num_plrs, ["Village", "Gardens", "Market", "Spy",
                                     "Smithy", "Witch", "Militia", "Moat",
                                     "Throne Room", "Laboratory"])

    for card, num in test_supply10.supply_counts.items():
        print(f"{card:<12}:{num:>2}")

    print()
    print()

    # Test 4 players, all cards provided and not unique
    print("4 players, all cards provided and not unique")
    test_supply11 = Supply(num_plrs, ["Village", "Village", "Gardens", "Gardens",
                                     "Market", "Market", "Spy", "Spy", "Witch",
                                     "Witch"])

    for card, num in test_supply11.supply_counts.items():
        print(f"{card:<12}:{num:>2}")

    print()
    print()

    # Test 4 players, not all cards provided
    print("4 players, not all cards_provided")
    test_supply12 = Supply(num_plrs, ["Village", "Market", "Witch"])

    for card, num in test_supply12.supply_counts.items():
        print(f"{card:<12}:{num:>2}")

    print()
    print()