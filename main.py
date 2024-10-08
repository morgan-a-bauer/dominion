"""main.py
Morgan Bauer and John Cetinkaya
29 March 2024

A Python implementation of the popular deck-building game Dominion.

"""
from random import shuffle
from rules import rule_nums, rule_dict
from supply import Supply
import util

def main():
    print("Welcome to DOMINION\n")
    player_lyst = util.get_players()
    print("\nIf you need a refresher on any rules of DOMINION, use this menu:\n")

    # Navigate the rules menu in the text-based environment
    # Selection determines which section of the menu the user may want to access
    selection = -1

    while type(selection) != int or selection != 6:  # Selecting 6 indicates being ready to play

        try:
            for category, num in rule_nums.items():
                # Print list of sections of rules
                print(f"{category:<16}{num:>4}")

            # Get which section to display from user
            selection = int(input("\nPlease enter the number of the section you would like: "))
            print()

            if selection < 6:
                # If the user wants to read a section, display that section
                print(rule_dict[selection])

        except ValueError as e:
            print("Please input an integer between 1 and 6\n")

    the_supply = Supply(len(player_lyst))
    player_index = 0

    # Play the game!
    while not util.game_over(the_supply.supply_counts):
        curr_player = player_lyst[player_index]
        print(f"{curr_player.name}'s turn:\n")
        curr_player.take_turn(the_supply)

        # Cycle through players
        player_index += 1
        player_index %= len(player_lyst)


if __name__ == "__main__":
    main()