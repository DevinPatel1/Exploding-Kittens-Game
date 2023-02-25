####################################################################################
# Developer:        Devin Patel
# Project Title:    Programming Assignment 1
# Class:            CS 524-01 - Principles of Programming Languages
# Term:             SP 23
####################################################################################
# Filename:     prog1_Computer.py
# Purpose:      To implement a computer player class that inherits from the Player class.
####################################################################################
# Design Requirements
#
# The Computer class will be responsible for the following:
#   1. Maintain, manage, and report a computer player's hand of cards.
#   2. Facilitate adding and removing cards from the computer player's hand.
#   3. Keep track of the computer player's name and number of wins they have.
#   4. Facilitate taking a turn for the computer player.
####################################################################################
# Class Specification
#
# Since python does not enforce access protections on attributes (e.g., protected or private)
# nor has a way to set constants, the following python conventions will be followed:
#   1. Any private attributes or methods will be prefixed with a single underscore '_'.
#   2. Any public attributes or methods will be directly accessible instead of using a getter.
#   3. Any attributes or methods that shouldn't get overriden by a subclass will be prefixed with a double underscore '__'.
#      This tells the python interpreter to instead prefix the attribute or method as '_ClassName_attribute' or '_ClassName_method'.
#   4. Any constants will be all caps.
#
#
# This class is a subclass of the Player class.
#
#
# Instance Attributes:
#   + name (str): Name of the player
#   + wins (int): Number of wins the player has
#   + hand (list[Card]): List of cards the player has
#   + remaining_turns (int): Number of turns the player has left
#                            This value is negative if the player lost and is no longer playing.
#
# Methods:
#   + __init__(name: str): Initializes an empty hand and sets the name of the player
#   
####################################################################################

# Imports
from prog1_Card import Card
from prog1_Player import Player


class Computer(Player):
    """
    Contains a player's hand of cards and facilitates adding and removing cards.
    Performs the required moves for the computer player.
    """
    
    def __init__(self, name: str) -> None:
        """
        Constructor for the Computer class.
        Initializes an empty hand and sets the name of the Computer.
        
        Args:
            name (str): Name of the player
        """
        # Attributes are initialized here instead of in the class definition
        # to avoid the attributes being shared between all instances of the class.
        self.hand: list[Card] = []
        self.name = name
        self.wins = 0
        self.remaining_turns = 0
    # End of __init__
    
    
# End of Player
