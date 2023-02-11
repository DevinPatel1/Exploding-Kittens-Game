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
# Since python does not enforce access protections on attributes (e.g., protected or private)
# nor has a way to set constants, the following python conventions will be followed:
#   1. Any private attributes or methods will be prefixed with a single underscore '_'.
#   2. Any public attributes or methods will be directly accessible instead of using a getter.
#   3. Any attributes or methods that shouldn't get overriden by a subclass will be prefixed with a double underscore '__'.
#      This tells the python interpreter to instead prefix the attribute or method as '_ClassName_attribute' or '_ClassName_method'.
#   4. Any constants will be all caps.
#
#
# Instance Attributes:
#?   + size (int):                  The number of cards in the deck.
#   - _deck (list: Card):           A list of Card types.
#   - _num_players (int):           The number of players in the game.
#
# Methods:
#   + __init__(number_of_players: int): Initializes the attributes, the deck, and the RNG.
#   + shuffle(): Shuffles the order of the remaining cards in the deck.
#   + draw():    Pops a card from the bottom of the deck list and returns it.
#   + place(card: Card, location="NoNe", index=-1):   Places a card at the specified location OR index in the deck.
#                                     Valid values for location are 'top', 'bottom',
#                                     'middle', or 'random', otherwise a ValueError will be raised.
#   + reset():   Resets the deck with all cards and shuffles.
#               Must be used with a method that clears cards from hands.
#?   + get_deck_count(): Returns the number of remaining cards in the deck.
#   + __str__(): Converts the deck to a string representation for printing/debugging.
#####################################################################################

# Imports
from prog1_Card import Card
import random   # Random Number Generator
import time     # Seeding the Random Number Generator

class Deck(object):
    """
    Deck will contain a list of cards and will be used to shuffle, draw, and reset cards.
    """
    
    def __init__(self, number_of_players) -> None:
        """
        Constructor for the Deck class.
        Sets a local variable for the number of players in the game.
        Initializes the deck with the appropriate number of Cards using reset().
        Seeds the random number generator using time.
        
        Args:
            number_of_players (int): The number of players in the game.
        """
        # Attributes are initialized here instead of in the class definition
        # to avoid the attributes being shared between all instances of the class.
        self._deck = []
        self._num_players = number_of_players
        self.size = 0
        
        # Initialize deck
        self.reset()
        
        # Seeds the RNG with the current time
        random.seed(time.time())
    # End of __init__
    
    
    
    def shuffle(self) -> None:
        """
        Shuffles the order of the remaining cards in the deck.
        """
        random.shuffle(self._deck)
    # End of shuffle
    
    
    
    def draw(self) -> Card:
        """
        Pops a card from the end of the deck list and returns it.
        
        Returns:
            Card: The card that was popped from the end of the list.
        """
        card = self._deck.pop()
        self.size -= 1
        
        return card
    # End of draw
    
    def place(self, card: Card, location="NoNe", index=-1) -> None:
        """
        Places a card at a specified location in the deck.
        If location is not specified, the card will be placed at the index parameter.
        If index is not specified, the card will be placed at the location parameter.
        If both or neither are specified, a ValueError will be raised.
        
        Args:
            card (Card): The card to be placed in the deck.
            location (str, optional if index passed): The location to place the card.
                                                      Valid values are 'top' (last index), 'bottom' (index 0), 'middle', or 'random'.
                                                      Defaults to 'NoNe'.
            index (int, optional if location passed): The index to place the card. Defaults to -1.
        
        Raises:
            ValueError: If the place is not 'top', 'bottom', 'middle', or 'random'.
            ValueError: If both location and index were passed or neither were passed.
            ValueError: If the parameter checks pass but location != "NoNe" and index != -1.
        """
                
        # Check parameters to see if both or neither were passed
        if location == "NoNe" and index == -1: 
            raise ValueError("Specify either a location or an index, but not both.")
        elif location != "NoNe" and index != -1:
            raise ValueError("Specify either a location or an index, but not neither.")
        
        
        # If location was specified, place the card at that location
        if index == -1:
            if location == 'top': self._deck.append(card)
            elif location == 'bottom': self._deck.insert(0, card)
            elif location == 'middle': self._deck.insert(self.size // 2, card)
            elif location == 'random': self._deck.insert(random.randint(0, self.size-1), card)
        
            # Raises a ValueError if the place is invalid
            else: raise ValueError(f"Invalid place: {location}")
        
        # Else if index was specified, place the card at that index
        elif location == "NoNe":
            self._deck.insert(index, card)
        
        # Else raise a ValueError
        else: raise ValueError("Invalid parameters.")
        
        # Once completed, increment the size of the deck
        self.size += 1
        
    # End of place(card, place)
    
    
    def reset(self) -> None:
        """
        Clears the game deck, refills it with the appropriate cards, then shuffles it.
        """
        
        # Clears the deck
        self._deck.clear()
        
        # Add the Exploding Kittens
        for _ in range(self._num_players-1): self._deck.append(Card.EK)
        
        # Add the Defuse cards. This has special rules.
        # Each player gets one Defuse card in their hand, and the rest are put in the deck.
        # However, if there are 2 or 3 players, only 2 Defuse cards get added to the deck.
        # Thus, two generator expressions are used.
        # The first adds 6-number_of_players Defuse cards to the deck if there are more than 3 players.
        [self._deck.append(Card.D) for _ in range(6-self._num_players) if self._num_players > 3]
        
        # The second adds 2 Defuse cards to the deck if there are 2 or 3 players.
        [self._deck.append(Card.D) for _ in range(2) if self._num_players <= 3]
        
        # Add the Nope cards
        for _ in range(5): self._deck.append(Card.N)
        
        # Add the Attack cards
        for _ in range(4): self._deck.append(Card.A)
        
        # Add the Skip cards
        for _ in range(4): self._deck.append(Card.SK)
        
        # Add the Favor cards
        for _ in range(4): self._deck.append(Card.F)
        
        # Add the Shuffle cards
        for _ in range(4): self._deck.append(Card.SH)
        
        # Add the See the Future cards
        for _ in range(5): self._deck.append(Card.STF)
        
        # Add the Taco Cat cards
        for _ in range(4): self._deck.append(Card.TCAT)
        
        # Add the Hairy Potato Cat cards
        for _ in range(4): self._deck.append(Card.HPCAT)
        
        # Add the Cattermelon cards
        for _ in range(4): self._deck.append(Card.CATM)
        
        # Add the Rainbow Ralphing Cat cards
        for _ in range(4): self._deck.append(Card.RRCAT)
        
        # Add the Beard Cat cards
        for _ in range(4): self._deck.append(Card.BCAT)
        
        # Shuffle the deck
        self.shuffle()
        
        # Set the size
        self.size = len(self._deck)
        
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
        s += f"Number of Exploding Kittens: {self._num_players-1}\n"
        s += "Deck:\n["
        
        # Appends deck contents to cumulative string s
        for i, card in enumerate(self._deck):
            
            # If on last element, don't append a comma
            if i == len(self._deck) - 1: 
                s += str(card.name())
            
            # Else append a comma
            else: 
                s += str(card.name()) + ", "
        # End of for loop
        
        s += "]"
        
        return s
    # End of __str__

# End of Deck
    