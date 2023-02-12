####################################################################################
# Developer:        Devin Patel
# Project Title:    Programming Assignment 1
# Class:            CS 524-01 - Principles of Programming Languages
# Term:             SP 23
####################################################################################
# Filename:     prog1_Player.py
# Purpose:      To implement a base player class that contains a player's hand of cards.
# @TODO               This class will be inherited by ComputerPlayer.
####################################################################################
# Design Requirements
#
# The Player class will be responsible for the following:
#   1. Maintain, manage, and report a player's hand of cards.
#   2. Facilitate adding and removing cards from the player's hand.
#   3. Keep track of the player's name and number of wins they have.
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
#   + wins (int): Number of wins the player has
#   + hand (list[Card]): List of cards the player has
#   + remaining_turns (int): Number of turns the player has left
#                            This value is negative if the player lost and is no longer playing.
#
# Methods:
#   + __init__(name: str): Initiales an empty hand and sets the name of the player
#   + add_card(card: Card): Adds a card to the player's hand
#   + pop_card(card: Card): Pops a card from the player's hand and returns it
#   + has_card(card: Card): Returns True if the player has the card in their hand
#   + reset(): Resets the player's hand and remaining turns to their initial values
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
        self.hand: list[Card] = []
        self.name = name
        self.wins = 0
        self.remaining_turns = 0
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
            identical_index = self.hand.index(card)
            
            # Exception not raised, so an identical card is found.
            # Insert the new card next to the identical card.
            self.hand.insert(identical_index + 1, card)
            
        except ValueError:
            self.hand.append(card)
    # End of add_card
    
    
    def pop_card(self, card: Card) -> Card:
        """
        Removes a card from the player's hand and returns it.
        
        Args:
            card (Card): Card to remove from the player's hand
        
        Raises:
            ValueError: If the card is not in the player's hand
        """
        return self.hand.pop(self.hand.index(card))
    # End of remove_card
    
    
    def has_card(self, a_card: Card) -> bool:
        """
        Returns True if the player has the card in their hand.

        Args:
            a_card (Card): Card to search for.

        Returns:
            bool: Returns True if the card is in the player's hand. False if otherwise.
        """
        return a_card in self.hand
    # End of has_card
    
    
    def reset(self) -> None:
        """
        Resets the player's hand and remaining turns to their initial values.
        """
        self.hand = []
        self.remaining_turns = 0
    # End of reset
    
    
    def sprintf_hand(self) -> str:
        """
        Returns a string representation of the player's hand for printing.
        
        Returns:
            str: String representation of the player's hand
        """
        return f"{self.name}'s Hand:\n" + "".join(f"\t{card.name()}\n" for card in self.hand)
    # End of sprintf_hand
    
    
    def __str__(self) -> str:
        """
        Returns a string representation of all Player attributes.
        
        Returns:
            str: Player name, win count, and hand
        """
        return f"{self.name} won {self.wins} times.\n{self.sprintf_hand()}"
    # End of __str__
    
# End of Player
