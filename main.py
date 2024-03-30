"""main.py
Morgan Bauer and John Cetinkaya
29 March 2024

A Python implementation of the popular deck-building game Dominion.

"""
from supply import Supply
from util import get_players

def main():
    print("Welcome to DOMINION\n")
    player_lyst = get_players()
    print(player_lyst)

if __name__ == "__main__":
    main()