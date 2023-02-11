####################################################################################
# Developer:        Devin Patel
# Project Title:    Programming Assignment 1
# Class:            CS 524-01 - Principles of Programming Languages
# Term:             SP 23
####################################################################################
# Filename:     prog1_Player.py
# Purpose:      To implement a base player class that contains a player's hand of cards.
#?               This class will be inherited by ComputerPlayer.
####################################################################################
# Design Requirements
#
#
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
# Instance Attributes:
#   + name (str):   Name of the player
#   + losses (int): Number of losses the player has
#   - _hand (list: Card): List of cards the player has
#
# Methods:
#   + __init__(name: str): Initiales an empty hand and sets the name of the player
#   + add_card(card: Card): Adds a card to the player's hand
#   + pop_card(card: Card): Pops a card from the player's hand
#   + sprintf_hand(): Returns a string representation of the player's hand
#   + __str__(): Returns a string representation of all Player attributes
####################################################################################

# Imports
from prog1_Card import Card


class Player:
    """
    Contains a player's hand of cards and facilitates adding and removing cards.
    """
    
    def __init__(self, name: str) -> None:
        """
        Constructor for the Player class.
        Initializes an empty hand and sets the name of the player.
        
        Args:
            name (str): Name of the player
        """
        # Attributes are initialized here instead of in the class definition
        # to avoid the attributes being shared between all instances of the class.
        self._hand = []
        self.name = name
        self.losses = 0
    # End of __init__
    
    
    def add_card(self, card: Card) -> None:
        """
        Adds a card to the player's hand.
        To keep identical cards grouped together, a search for the added card is done first.
        If a identical card is found, the new card is inserted after the identical card.
        If a identical card is not found, the new card is appended to the end of the list.
        
        Args:
            card (Card): Card to add to the player's hand
        """
        
        # list.index() raises a ValueError if the card is not found.
        # If an exception is caught, then append the card to the end of the list.
        try:
            identical_index = self._hand.index(card)
            
            # Exception not raised, so an identical card is found.
            # Insert the new card next to the identical card.
            self._hand.insert(identical_index + 1, card)
            
        except ValueError:
            self._hand.append(card)
    # End of add_card
    
    
    def remove_card(self, card: Card) -> None:
        """
        Removes a card from the player's hand.
        
        Args:
            card (Card): Card to remove from the player's hand
        
        Raises:
            ValueError: If the card is not in the player's hand
        """
        self._hand.remove(card)
    # End of remove_card
    
    
    def sprintf_hand(self) -> str:
        """
        Returns a string representation of the player's hand for printing.
        
        Returns:
            str: String representation of the player's hand
        """
        return "".join(f"\t{card.name()}\n" for card in self._hand)
    # End of sprintf_hand
    
    def __str__(self) -> str:
        """
        Returns a string representation of all Player attributes.
        
        Returns:
            str: Player name and hand
        """
        return f"{self.name}'s Hand:\n{self.sprintf_hand()}"
    # End of __str__
    
# End of Player
