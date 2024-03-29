"""base_set.py
Morgan Bauer and John Cetinkaya
27 March 2024

A dictionary of characteristic information regarding cards in the Dominion
Base Set. Includes both first and second edition.

"""

"""Supply card information is represented as follows:

<card_name>[0]: 0 indicates treasure card, 1 indicates victory card
<card_name>[1]: cost of the card
<card_name>[2]: sign of the card's value
<card_name>[3]: value of the card

"""

supply_cards = {"Copper":   "00+1",
                "Curse":    "10-1",
                "Estate":   "12+1",
                "Silver":   "03+2",
                "Duchy":    "15+3",
                "Gold":     "06+3",
                "Province": "18+6"}

"""Kingdom card information is represented as follows:

<card_name>[0]: 0 indicates standard action, 1 indicates attack, 2 indicates
                reaction, 3 indicates victory card
<card_name>[1]: cost of the card
<card_name>[2]: number of additional actions
<card_name>[3]: number of additional buys
<card_name>[4]: number of additional cards
<card_name>[5]: amount of additional treasure


"""

kingdom_cards = {"Cellar":       "021000",
                 "Chapel":       "020000",
                 "Moat":         "220020",
                 "Chancellor":   "030002",
                 "Harbinger":    "031010",
                 "Merchant":     "031010",
                 "Vassal":       "030002",
                 "Village":      "031020",
                 "Woodcutter":   "030102",
                 "Workshop":     "030000",
                 "Bureaucrat":   "140000",
                 "Feast":        "040000",
                 "Gardens":      "340000",
                 "Militia":      "140002",
                 "Moneylender":  "040000",
                 "Poacher":      "041011",
                 "Remodel":      "040000",
                 "Smithy":       "040030",
                 "Spy":          "141010",
                 "Theif":        "140000",
                 "Throne Room":  "040000",
                 "Bandit":       "150000",
                 "Council Room": "050140",
                 "Festival":     "052102",
                 "Laboratory":   "051020",
                 "Library":      "050000",
                 "Market":       "051111",
                 "Mine":         "050000",
                 "Sentry":       "051010",
                 "Witch":        "150020",
                 "Adventurer":   "060000",
                 "Artisan":      "060000"}