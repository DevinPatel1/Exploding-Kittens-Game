####################################################################################
# Developer:        Devin Patel
# Project Title:    Programming Assignment 1
# Class:            CS 524-01 - Principles of Programming Languages
# Term:             SP 23
####################################################################################
# Filename:     prog1_Prompts.py
# Purpose:      To implement user prompts, validate user input, and return
#               input data for Game class.
####################################################################################
# Design Requirements
# 
# The Prompts class will be responsible for the following:
#   1. Prompting the user for specific input at certain points in a game of Exploding Kittens.
#   2. Each prompt will be implemented in its own method.
#   3. Each method will be an input loop that breaks only when the user enters valid input.
#####################################################################################
# Class Specification
# @TODO Update this section as code is written
# Since python does not enforce access protections on attributes (e.g., protected or private)
# nor has a way to set constants, the following python conventions will be followed:
#   1. Any private attributes or methods will be prefixed with a single underscore '_'.
#   2. Any public attributes or methods will be directly accessible instead of using a getter.
#   3. Any attributes or methods that shouldn't get overriden by a subclass will be prefixed with a double underscore '__'.
#      This tells the python interpreter to instead prefix the attribute or method as '_ClassName__attribute' or '_ClassName_method'.
#   4. Any constants will be all caps.
#
#
# Attributes:
#   None
#
# Methods:
#   + __init__(): No attributes to initialize, so it does nothing.
#   + prompt_num_players(): Prompts the user for the number of players in the game.
#   - _input(): Macro that creates the user input prompt and returns the string received from stdin.
####################################################################################

class Prompts:
    """
    Prompts will manage user input and return validated prompt data for the Game class.
    """
    
    def __init__(self) -> None:
        """
        Nothing initiated here, this is just a functional class.
        """
        pass
    # End of __init__
    
    
    def _input(self) -> str:
        """
        Macro that creates the user input prompt and returns the string received from stdin.
        The macro also strips the whitespace from the string prior to returning it.

        Returns:
            str: String received from stdin.
        """
        return input(">>").strip()
    # End of _input
    
    
    def print_welcome(self) -> None:
        """
        Prints a welcome message to the user.
        """
        print("Welcome to Exploding Kittens!\n")
        
    
    def prompt_num_players(self) -> int:
        """
        Prompts the user for the number of players in the game.
        
        Returns:
            int: The number of players in the game.
        """
        print("How many players are playing?")
        print("Please type an integer that is 2 or greater.")
        
        # Input loop
        while True:
            try:
                num_players = int(self._input())
                if num_players < 2:
                    print("There must be at least 2 players.")
                else:
                    return num_players # Breaks Input loop
            except ValueError:
                print("Please enter a integer that is 2 or greater.")
        # End of Input loop
    # End of prompt_num_players
    
    
# End of Prompts