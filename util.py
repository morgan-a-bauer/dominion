"""util.py
Morgan Bauer and John Cetinkaya
29 March 2024

Utility functions for the game Dominion

"""
from player import Player
from random import shuffle

def get_players() -> list:
    """Asks for players to enter their names in the shell and assembles a list
    of Player objects using those names. Dominion can be played with 2-4 players

    """
    player_lyst = []

    print("DOMINION can be played with 2-4 players\n")

    # Keep asking for player names to have at most 4 players
    while len(player_lyst) < 4:
        try:
            player_name = input(f"Player {len(player_lyst) + 1}, please enter" +\
                            " your name: ")

            # Names must contain only letters
            if not player_name.isalpha():
                raise ValueError("USAGE: Names must be strictly alphabetic")

            # Append the new player to the list of players
            new_player = Player(player_name.capitalize())
            player_lyst.append(new_player)

            # Give the option to play with only 2 or 3 players
            more_players = "John is an idiot"
            while more_players not in "yn" and len(player_lyst) != 4:
                more_players = input("Would you like to add another player? (y/n): ")

            # Make sure there are at least two players to quit player entry
            if more_players == "n" and len(player_lyst) >= 2:
                break

            print()

        # Except clause for non-alphabetic names
        except ValueError as err:
            print(err)

    # Assign random turn order
    shuffle(player_lyst)

    return player_lyst

def game_over(supply_dict: dict) -> bool:
    if supply_dict["Province"] == 0:
        return True

    if list(supply_dict.values()).count(0) == 3:
        return True

    return False