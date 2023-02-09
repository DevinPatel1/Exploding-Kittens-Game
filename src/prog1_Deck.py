####################################################################################
# Developer:        Devin Patel
# Project Title:    Programming Assignment 1
# Class:            CS 524-01 - Principles of Programming Languages
# Term:             SP 23
####################################################################################
# Filename:     prog1_Deck.py
# Purpose:      To implement a card deck class that contains
#               a list (representing the deck) of Exploding Kittens
#               cards and can shuffle, draw, and reset cards.
####################################################################################
# Design Requirements
#
# The card deck class will contain a list of Card types to represent the deck.
#
# The following cards will be included in the deck:
#   - Exploding Kitten: Player Count - 1 cards
#   - Defuse: 6 cards
#   - Nope: 5 cards
#   - Attack: 4 cards
#   - Skip: 4 cards
#   - Favor: 4 cards
#   - Shuffle: 4 cards
#   - See the Future: 5 cards
#   - Cat Cards: 5 cats x 4 cards each
#       -- Taco Cat
#       -- Hairy Potato Cat
#       -- Cattermelon
#       -- Rainbow Ralphing Cat
#       -- Beard Cat
#####################################################################################
# Class Specification
#
# Since python does not inherently have a private attribute modifier nor has a way
# to set constants, the following PEP8 python naming conventions will be used:
#   1. Any private attributes will be prefixed with a double underscore '__'.
#   2. Any methods that aren't meant to be used outside of the class will be
#      prefixed with a single underscore '_'.
#   3. Any constants will be all caps.
#
#
# Attributes:
#? + size:            The number of cards in the deck.
# - __deck:          A list of Card types.
# - __PARENT_DECK:   A list of cards that will be used to reset the deck.
#                    This list will be imported from a json file.
#
# Methods:
#  + __init__(number_of_players): Initializes the attributes.
#  + shuffle(): Shuffles the order of the remaining cards in the deck.
#  + draw():    Pops a card from the deck and returns it.
#  + reset():   Resets the deck with all cards and shuffles.
#               Must be used with a method that clears cards from hands.
#?  + get_deck_count(): Returns the number of remaining cards in the deck.
#  + __str__(): Converts the deck to a string representation for printing/debugging.
#
#  - _initialize_parent_deck(): Initializes the PARENT_DECK with a
#                                predefined list of Card types.
####################################################################################


# Imports
from prog1_Card import Card
import random

"""
Deck will contain a list of cards and will be used to shuffle, draw, and reset cards.
"""
class Deck:
    
    # Attributes
    __deck = []
    __PARENT_DECK = []
    size = 0
    
    
    
    """
    Constructor for the Deck class.
    Initializes the PARENT_DECK with a predefined list of Card types.
    Initializes the size of the deck.
    Initializes the deck with the PARENT_DECK.
    
    Args:
        number_of_players (int): The number of players in the game.
    """    
    def __init__(self, number_of_players):
        self._initialize_parent_deck(number_of_players)
        self.size = len(self.__deck)
        self.reset()
    # End of __init__
    
    
    
    """
    Initializes the PARENT_DECK with a predefined list of Card types stored in a json file.
    The deck will include number_of_players - 1 Exploding Kitten cards.
    
    Args:
        number_of_players (int): The number of players in the game.
    """
    def _initialize_parent_deck(self, number_of_players):
        pass
    # End of _initialize_deck
    
    
    
    """
    Shuffles the order of the remaining cards in the deck.
    """
    def shuffle(self):
        pass
    # End of shuffle
    
    
    
    """
    Pops a card from the deck list and returns it.
    
    Returns (Card): The card that was popped from the deck.
    """
    def draw(self):
        pass
    # End of draw
    
    
    
    """
    Clears the game deck and copies the PARENT_DECK to the game deck.
    """
    def reset(self):
        pass
    # End of reset
    
    
    # @TODO Delete this if not needed. If it is, add it back to the documentation header above.
    """
    Returns the number of remaining cards in the deck.
    
    Returns:
        int: The number of remaining cards in the deck.
    """
    def get_deck_count(self): return self.size
    


    # @TODO Implement this method
    """
    Converts the deck to a string representation for printing/debugging.
    
    Returns (str): The string representation of the deck.
    """
    def __str__(self):
        return str(self.deck)
    # End of __str__

# End of Deck
    