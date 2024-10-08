"""main.py
Morgan Bauer and John Cetinkaya
29 March 2024

A Python implementation of the popular deck-building game Dominion.

"""
from rules import rule_nums, rule_dict
from supply import Supply
from supply_card import SupplyCard
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

    high_score = 0
    winners = []

    # Coutn victory points to determine winner
    for player in player_lyst:
        player_score = 0

        # Count victory points in each player's deck
        for card in player.deck.deck:
            if type(card) == SupplyCard:

                # If the card is a victory card
                if card.type == 1:
                    player_score += card.value

        # Count victory points in each player's hand
        for card in player.hand.hand:
            if type(card) == SupplyCard:

                # If the card is a victory card
                if card.type == 1:
                    player_score += card.value

        # Count victory points in each player's discard pile
        for card in player.discard_pile.graveyard:
            if type(card) == SupplyCard:

                # If the card is a victory card
                if card.type == 1:
                    player_score += card.value

        # If there is a tie with the current high score
        if player_score == high_score:
            winners.append(player.name)

        # If there is a newly encoutered high score
        if player_score > high_score:
            winners.clear()
            winners.append(player.name)
            high_score = player_score

        print(f"{player.name:<15}: {player_score:>3}")

    if len(winners) == 1:
        print(f"\n{winners[0]} won!")

    else:
        winner_str = ''
        for name in winners[:-1]:
            if len(winners) == 2:
                winner_str += name + ' '
            else:
                winner_str += (name + ', ')

        winner_str += f'and {winners[-1]}'

        print(f'\n{winner_str} tied for first!')



if __name__ == "__main__":
    main()