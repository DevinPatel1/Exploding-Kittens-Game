####################################################################################
# Developer:        Devin Patel
# Project Title:    Programming Assignment 1
# Class:            CS 524-01 - Principles of Programming Languages
# Term:             SP 23
####################################################################################
# Filename:     prog1_Card.py
# Purpose:      To implement a Card enum class that contains
#               all of the cards' names and descriptions in a tuple.
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
#             cards, secretly put it back in the draw pile anywhere you’d like. Want to
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
#   - Shuffle: Shuffles the draw pile.
#
#   - See the Future: Privately view the top 3 cards from the draw pile.
#   - Cat Cards: <Cat Type> are powerless on their own, but if you collect any 2 matching
#                <Cat Type> cards, you can play them as a pair to steal a random card from any player.
#       Cat Types:
#       - Taco Cat
#       - Hairy Potato Cat
#       - Cattermelon
#       - Rainbow Ralphing Cat
#       - Beard Cat
####################################################################################
# Class Specification
#
# Since python does not support private attributes nor has a way
# to set constants nor has any access protections on attributes, the immutable
# type tuple will be used in conjunction with Enums to store the names and descriptions of the
# cards.
#
# Card will extend the Enum class.
#
# Attributes/Enums:
#   + EK: ("Exploding Kitten", description)
#   + D: ("Defuse", description)
#   + N: ("Nope", description)
#   + A: ("Attack", description)
#   + SK: ("Skip", description)
#   + F: ("Favor", description)
#   + SH: ("Shuffle", description)
#   + STF: ("See the Future", description)
#   + TCAT: ("Taco Cat", description)
#   + HPCAT: ("Hairy Potato Cat", description)
#   + CATMELON: ("Cattermelon", description)
#   + RRCAT: ("Rainbow Ralphing Cat", description)
#   + BCAT: ("Beard Cat", description)
#
# Methods:
#   None
####################################################################################


# Imports
from enum import Enum

class Card(Enum):
    """
    Extends the Enum class.
    Contains all of the cards' names and descriptions in a tuple (name, description).
    """
    
    EK = ("Exploding Kitten", "\tYou must show this card immediately.\n"
          + "\tUnless you have a Defuse Card, you're dead.\n"
          + "\tDiscard all of your cards, including the Exploding Kitten.")
    
    D = ("Defuse", "\tIf you drew an Exploding Kitten, you can play this card instead of dying.\n"
         + "\tThen take the Exploding Kitten, and without reordering or viewing the other cards, secretly"
         + "put it back in the draw pile anywhere you'd like.\n\tWant to hurt the player right after you?"
         + "Put the Kitten right on top of the deck.\n\tYour turn is over after playing this card.\nThe Defuse card can only be used once.")
    
    N = ("Nope", "\tStop any action except for an Exploding Kitten or a Defuse Card.\n"
         + "\tImagine that any card beneath a Nope Card never existed.\n"
         + "\tA Nope can also be played on another Nope to negate it and create a Yup, and so on.\n"
         + "\tNope can be played at any time before an action has begun, even if it's not your turn.\n"
         + "\tAny cards that have been Noped are lost.")
    
    A = ("Attack", "\tDo not draw any cards.\n"
         + "\tInstead, immediately force the next player to take 2 turns in a row.\n"
         + "\tPlay then continues from that player.\n"
         + "\tThe victim of this card takes a turn as normal (play-or-pass then draw).\n"
         + "\tThen, when their first turn is over, it's their turn again.\n\n"
         + "\tIf the victim of an Attack Card plays an Attack Card on any of their turns,"
         + "the new target must take any remaining turns plus the number of attacks on "
         + "the Attack Card just played (e.g. 4 turns, then 6, and so on).")
    
    SK = ("Skip", "\tImmediately end your turn without drawing a card.\n"
          + "\tIf you play a Skip Card as a defense to an Attack Card, it only ends 1 of the 2 turns.\n"
          + "\t2 Skip Cards would end both turns.")
    
    F = ("Favor", "\tForce another player to give you one of their cards. They can choose which one.")
    
    SH = ("Shuffle", "\tShuffles the draw pile.")
    
    STF = ("See the Future", "\tPrivately view the top 3 cards from the draw pile.")
    
    TCAT = ("Taco Cat", "\tTaco Cats are powerless on their own, but if you collect any 2 matching Taco Cat cards,\n"
            + "\tyou can play them as a pair to steal a random card from any player.")
    
    HPCAT = ("Hairy Potato Cat", "\tHairy Potato Cats are powerless on their own, but if you collect any 2 matching Hairy Potato Cat cards,\n"
             + "\tyou can play them as a pair to steal a random card from any player.")
    
    CATM = ("Cattermelon", "\tCattermelons are powerless on their own, but if you collect any 2 matching Cattermelon cards,\n"
                + "\tyou can play them as a pair to steal a random card from any player.")
    
    RRCAT = ("Rainbow Ralphing Cat", "\tRainbow Ralphing Cats are powerless on their own, but if you collect any 2 matching Rainbow Ralphing Cat cards,\n"
              + "\tyou can play them as a pair to steal a random card from any player.")
    
    BCAT = ("Beard Cat", "\tBeard Cats are powerless on their own, but if you collect any 2 matching Beard Cat cards,\n"
            + "\tyou can play them as a pair to steal a random card from any player.")
    
    
    
    