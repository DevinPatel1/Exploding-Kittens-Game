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
#       -> Taco Cat
#       -> Hairy Potato Cat
#       -> Cattermelon
#       -> Rainbow Ralphing Cat
#       -> Beard Cat
#####################################################################################
# Class Specification
#
# Since python does not support private attributes nor has a way
# to set constants nor has any access protections on attributes, the following
# PEP8 python naming conventions will be used:
#   1. Any private attributes will be prefixed with a double underscore '__'.
#   2. Any public attributes will be directly accessible instead of using a getter.
#   3. Any methods that aren't meant to be used outside of the class will be
#      prefixed with a single underscore '_'.
#   4. Any constants will be all caps.
#
#
# Attributes:
#? + size (int):                  The number of cards in the deck.
# + remaining_kittens (int):      The number of remaining Exploding Kittens.
# - __deck (list<Card>):          A list of Card types.
# - __BASE_CARD_COUNT (int):      The number of cards in the deck without the Exploding Kittens.
#
# Methods:
#  + __init__(number_of_players: int): Initializes the attributes.
#  + shuffle(): Shuffles the order of the remaining cards in the deck.
#  + draw():    Pops a card from the deck and returns it.
#  + reset():   Resets the deck with all cards and shuffles.
#               Must be used with a method that clears cards from hands.
#?  + get_deck_count(): Returns the number of remaining cards in the deck.
#  + __str__(): Converts the deck to a string representation for printing/debugging.
####################################################################################


# Imports
from prog1_Card import Card
import random

class Deck:
    """
    Deck will contain a list of cards and will be used to shuffle, draw, and reset cards.
    
    Attributes:
        size (int): The number of remaining cards in the draw pile.
    """

    # Attributes
    __deck = []
    __BASE_CARD_COUNT = 62 # Number of cards without the Exploding Kittens
    remaining_kittens = 0  # Number of remaining Exploding Kittens
    size = 0
    
    
    
    def __init__(self, number_of_players) -> None:
        """
        Constructor for the Deck class.
        Initializes the size of the deck.
          There are 62 plus number_of_players-1 Exploding Kitten cards in the deck.
        Initializes the deck with the appropriate number of Cards.
        
        Args:
            number_of_players (int): The number of players in the game.
        """
        self.remaining_kittens = number_of_players - 1
        self.size = self.__BASE_CARD_COUNT + self.remaining_kittens
        self.reset()
    # End of __init__
    
    
    
    def shuffle(self) -> None:
        """
        Shuffles the order of the remaining cards in the deck.
        """
        random.shuffle(self.__deck)
    # End of shuffle
    
    
    
    def draw(self) -> Card:
        """
        Pops a card from the deck list and returns it.
        
        Returns (Card): The card that was popped from the deck.
        """
        pass
    # End of draw
    
    
    
    def reset(self) -> None:
        """
        Clears the game deck, refills it with the appropriate cards, then shuffles it.
        """
        self.__deck.clear()
        
        # Add the Exploding Kittens
        for _ in range(self.remaining_kittens): self.__deck.append(Card.EK)
        
        # Add the Defuse cards
        for _ in range(6): self.__deck.append(Card.D)
        
        # Add the Nope cards
        for _ in range(5): self.__deck.append(Card.N)
        
        # Add the Attack cards
        for _ in range(4): self.__deck.append(Card.A)
        
        # Add the Skip cards
        for _ in range(4): self.__deck.append(Card.SK)
        
        # Add the Favor cards
        for _ in range(4): self.__deck.append(Card.F)
        
        # Add the Shuffle cards
        for _ in range(4): self.__deck.append(Card.SH)
        
        # Add the See the Future cards
        for _ in range(5): self.__deck.append(Card.STF)
        
        # Add the Taco Cat cards
        for _ in range(4): self.__deck.append(Card.TCAT)
        
        # Add the Hairy Potato Cat cards
        for _ in range(4): self.__deck.append(Card.HPCAT)
        
        # Add the Cattermelon cards
        for _ in range(4): self.__deck.append(Card.CATM)
        
        # Add the Rainbow Ralphing Cat cards
        for _ in range(4): self.__deck.append(Card.RRCAT)
        
        # Add the Beard Cat cards
        for _ in range(4): self.__deck.append(Card.BCAT)
        
        # Shuffle the deck
        self.shuffle()
                
    # End of reset
    
    
    # @TODO Delete this if not needed. If it is, add it back to the documentation header above.
    def get_deck_count(self) -> int:
        """
        Returns the number of remaining cards in the deck.
        
        Returns:
            int: The number of remaining cards in the deck.
        """
        return self.size
    # End of get_deck_count
    


    def __str__(self) -> str:
        """
        Converts the deck to a string representation for printing/debugging.
        
        Returns (str): The string representation of the deck.
        """
        # Print size
        s = ""
        
        s += f"Deck size: {self.size}\n"
        s += f"Remaining Exploding Kittens: {self.remaining_kittens}\n"
        s += "Deck:\n["
        
        # Appends deck contents to cumulative string s
        for i, card in enumerate(self.__deck):
            
            # If on last element, don't append a comma
            if i == len(self.__deck) - 1: 
                s += str(card.value[0])
            
            # Else append a comma
            else: 
                s += str(card.value[0]) + ", "
        # End of for loop
        
        s += "]"
        
        return s
    # End of __str__

# End of Deck
    