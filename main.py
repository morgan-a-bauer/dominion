"""main.py
Morgan Bauer and John Cetinkaya
29 March 2024

A Python implementation of the popular deck-building game Dominion.

"""
from random import shuffle
from rules import rule_nums, rule_dict
from supply import Supply
from util import get_players

def main():
    print("Welcome to DOMINION\n")
    player_lyst = get_players()
    print("\nIf you need a refresher on any rules of DOMINION, use this menu:\n")
    selection = -1
    while selection != 6:
        for category, num in rule_nums.items():
            print(f"{category:<16}{num:>4}")
        selection = int(input("\nPlease enter the number of the section you would like: "))
        print()
        if selection != 6:
            print(rule_dict[selection])

if __name__ == "__main__":
    main()