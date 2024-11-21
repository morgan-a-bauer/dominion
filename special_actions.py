"""special_actions.py
Morgan Bauer and John Cetinkaya
08 Oct 2024

Special actions used by cards in Dominion

"""

def discard_and_draw(player, param_lyst = [-1, -1]):
    """A player discards a given number of cards and then draws a given number
    of cards

    Input:
    player -- the player who is playing the card
    param_lyst -- a list containing other optional parameters. In this case,
                  the number of cards t odiscard followed by the number of
                  cards to draw

    """
    num_to_discard = param_lyst[0]
    num_to_draw = param_lyst[1]
    while num_to_discard < 0 or num_to_discard > len(player.hand.hand):
        try:
            num_to_discard = int(input("How many cards would you like to discard? "))
            num_to_draw = num_to_discard

        except ValueError:
            print("Please enter an integer")

    num_discarded = 0
    cards_in_hand = [card.name for card in player.hand.hand]

    # Discard specified number of cards
    for i in range(num_to_discard):
        discard = "Black Lotus"
        while discard not in cards_in_hand:
            print()
            discard = input("Choose a card to discard from your hand: ").capitalize().strip()

        player.discard_card(discard)

        # Print remaining cards in hand
        if len(player.hand.hand) != 0:
            print(player.hand)

    # Draw specified number of cards
    for i in range(num_to_draw):
        player.draw_card()

actions = [[discard_and_draw]]