####################################################################################
# Developer:        Devin Patel
# Project Title:    Programming Assignment 1
# Class:            CS 524-01 - Principles of Programming Languages
# Term:             SP 23
####################################################################################
# Filename:     prog1_Prompter.py
# Purpose:      To implement user prompts, validate user input, and return
#               input data for Game class.
####################################################################################
# Design Requirements
# 
# The Prompter class will be responsible for the following:
#   1. Formatting and printing any game-related output to the terminal.
#   2. Prompting the user for specific input at certain points in a game of Exploding Kittens.
#   3. Each prompt will be implemented in its own method.
#   4. Each method will be an input loop that breaks only when the user enters valid input.
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
# Class Attributes:
#   - __GAME (str): Indicates to the user that a message is a game update.
#   - __PRMPT (str): Indicates to the user that a message is a prompt.
#   - __ERR (str): Indicates to the user that a message is an error.
#
# Methods:
#   + __init__(): No attributes to initialize, so it does nothing.
#   + prompt_num_players(): Prompts the user for the number of players in the game.
#   + prompt_player_names(num_players: int): Prompts the user for the names of the players.
#   - _input(): Macro that creates the user input prompt and returns the string received from stdin.
#   - _spacer(lines: int): Macro that prints lines of whitespace to the terminal for readability.
####################################################################################

# Imports
from prog1_Player import Player
from prog1_Card import Card

class Prompter:
    """
    Prompter will manage user input and return validated prompt data,
    as well as print any game-related messages to the terminal.
    """
    
    # Class Attributes
    __GAME = "[GAME]"    # For game updates
    __PRMPT = "[PROMPT]" # For prompts
    __ERR = "[ERROR]\a"  # For errors or invalid input
    
    def __init__(self) -> None:
        """
        Nothing initiated here, this is just a functional class.
        """
        pass
    # End of __init__
    
    ########################################
    # Private Macros
    ########################################
    
    def _input(self) -> str:
        """
        Macro that prints the input prompt symbol and returns the string received from stdin.
        The macro also strips the whitespace from the string prior to returning it.

        Returns:
            str: String received from stdin.
        """
        return input(">>").strip()
    # End of _input
    
    def _spacer(self, lines=1) -> None:
        """
        Macro that prints lines of whitespace to the terminal for readability.
        
        Args:
            lines (int, optional): Number of whitespace lines to print. Defaults to 1.
        """
        print("\n"*lines, end="")
    # End of _spacer
    
    
    
    ########################################
    # Prompt Methods
    ########################################
    
    def print_welcome(self) -> None:
        """
        Prints a welcome message to the user.
        """
        print("Welcome to Exploding Kittens!")
        
    
    def prompt_num_players(self) -> int:
        """
        Prompts the user for the number of players in the game.
        Valid input is an integer between 2 and 5.
        
        Returns:
            int: The number of players in the game.
        """
        self._spacer()
        print(f"{self.__PRMPT} How many players are playing? Only 2-5 players are able to play.")
        
        # Input loop
        while True:
            try: # Capture and cast user input as an int
                num_players = int(self._input())
            except ValueError:
                # Input is not an integer
                print(f"{self.__ERR} Please enter a integer that is 2 or greater.")
                continue
            # End of try/except
            
            # Check if there are enough players
            if num_players < 2:
                print(f"{self.__ERR} There must be at least 2 players.")
            elif num_players > 5:
                print(f"{self.__ERR} There can't be more than 5 players.")
            else: # Valid input
                return num_players # Breaks Input loop
        # End of Input loop
    # End of prompt_num_players
    
    
    def prompt_player_names(self, num_players: int) -> list:
        """
        Prompts the user for the names of the players.
        
        Args:
            num_players (int): Number of names to prompt for.
        
        Returns:
            list: List of all the players as Player objects.
        """
        self._spacer()
        list_of_players = []
        
        for i in range(num_players):
            # Prints the prompt for each player
            print(f"{self.__PRMPT} Player {i+1}'s name?")
        
            # Input loop
            while True:
                name = self._input()
                
                # Check if the name is empty or only digits
                if len(name) == 0 or name.isnumeric():
                    print(f"{self.__ERR} Please enter a name with at least some letters.")
                else:
                    # Valid input, append player then break
                    list_of_players.append(Player(name))
                    break
            # End of Input loop
            self._spacer() # Make some space in the terminal
        # End of for loop
        
        return list_of_players
    # End of prompt_player_names
    
# End of Prompter