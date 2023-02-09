####################################################################################
# Developer:        Devin Patel
# Project Title:    Programming Assignment 1
# Class:            CS 524-01 - Principles of Programming Languages
# Term:             SP 23
####################################################################################
# Filename:     prog1_Card.py
# Purpose:      To implement an individual Card class that contains
#               the card's name and description.
####################################################################################
# Design Requirements
#
# The following card names and descriptions will be implemented:
#   - Exploding Kitten: You must show this card immediately.
#                        Unless you have a Defuse Card, you’re dead.
#                        Discard all of your cards, including the Exploding Kitten.
#
#   - Defuse: If you drew an Exploding Kitten, you can play this card instead of dying.
#             Then take the Exploding Kitten, and without reordering or viewing the other
#             cards, secretly put it back in the Draw Pile anywhere you’d like. Want to
#             hurt the player right after you? Put the Kitten right on top of the deck.
#             If you’d like, hold the deck under the table so that no one else can see
#             where you put it. Your turn is over after playing this card.
#             The Defuse card can only be used once.
#
#   - Nope: Stop any action except for an Exploding Kitten or a Defuse Card.
#           Imagine that any card beneath a Nope Card never existed.
#           A Nope can also be played on another Nope to negate it and create a Yup, and so on.
#           Nope can be played at any time before an action has begun, even if it’s not your turn.
#           Any cards that have been Noped are lost.
#
#   - Attack: Do not draw any cards.
#             Instead, immediately force the next player to take 2 turns in a row.
#             Play then continues from that player.
#             The victim of this card takes a turn as normal (play-or-pass then draw).
#             Then, when their first turn is over, it's their turn again.
#
#             If the victim of an Attack Card plays an Attack Card on any of their turns,
#             the new target must take any remaining turns plus the number of attacks on
#             the Attack Card just played (e.g. 4 turns, then 6, and so on).
#
#   - Skip: Immediately end your turn without drawing a card.
#           If you play a Skip Card as a defense to an Attack Card, it only ends 1 of the 2 turns.
#           2 Skip Cards would end both turns.
#
#   - Favor: Force another player to give you one of their cards. They can choose which one.
#
#   - Shuffle: Shuffle the Draw Pile.
#
#   - See the Future: Privately view the top 3 cards from the Draw Pile.
#   - Cat Cards: These cards are powerless on their own, but if you collect any 2 matching
#                Cat Cards, you can play them as a Pair to steal a random card from any player.
#       -- Taco Cat
#       -- Hairy Potato Cat
#       -- Cattermelon
#       -- Rainbow Ralphing Cat
#       -- Beard Cat
####################################################################################
# Class Specification
#
# Since python does not have a private attribute modifier nor has a way to
# set constants, the following PEP8 python naming conventions will be used:
#   1. Any private attributes will be prefixed with a double underscore '__'.
#   2. Any methods that aren't meant to be used outside of the class will be
#      prefixed with a single underscore '_'.
#   3. Any constants will be all caps.
#
#
# Attributes:
#
#
# Methods:
#
####################################################################################





# Each card will have a name and description of what it does.
# Make card and enum type for all the card names and descriptions
# Needs to have a __str__ method and a copy method

class Card:
    pass