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
#   + print_welcome(): Prints a welcome message to the user.
#   + prompt_num_players(): Prompts the user for the number of players in the game.
#   + prompt_player_names(num_players: int): Prompts the user for the names of the players.
#   + alert_player_turn(): Alerts which user's turn it is so their hand can't be seen by other players.
#   + prompt_play_or_pass(): Prompts the user to play a card or pass.
#
# Macros:
#   - _input(prompt_symbol=">>"): Macro that creates the user input prompt and returns the string received from stdin.
#   - _spacer(lines: int): Macro that prints lines of whitespace to the terminal for readability.
#   - _continue(): Macro that prompts the user to press enter to continue.
#   - _error(error_msg: str): Macro that prints an error message to the terminal.
####################################################################################

# Imports
from prog1_Player import Player
from prog1_Card import Card

class Prompter:
    """
    Prompter will facilitate user input and return validated prompt data,
    as well as print any game-related messages to the terminal.
    """
    
    # Class Attributes
    __GAME = "[GAME]"    # For game updates
    __PRMPT = "[PROMPT]" # For prompts
    __ERR = "[ERROR]\a"  # For errors or invalid input. Plays a bell char if the terminal supports it.
    
    def __init__(self) -> None:
        """
        Nothing initiated here, Prompter is a stateless class.
        """
        pass
    # End of __init__
    
    ########################################
    # Private Macros
    ########################################
    
    def _input(self, prompt_symbol=">>") -> str:
        """
        Macro that prints the input prompt symbol and returns the string received from stdin.
        The macro also strips the whitespace from the string prior to returning it.

            input(<prompt_symbol>).strip()

        Args:
            prompt_symbol (str, optional): The symbol to print indicating user input. Defaults to ">>".

        Returns:
            str: String received from stdin.
        """
        return input(prompt_symbol).strip()
    # End of _input
    
    def _spacer(self, lines=1) -> None:
        """
        Macro that prints lines of whitespace to the terminal for readability.
        
        Args:
            lines (int, optional): Number of whitespace lines to print. Defaults to 1.
        """
        print("\n"*lines, end="")
    # End of _spacer
    
    def _continue(self) -> None:
        """
        Macro that prompts the user to press enter to continue.
        """
        input("Press [Enter] to continue...")
    
    def _error(self, error_msg: str) -> None:
        """
        Macro that prints an error message to the terminal.
        The user then presses enter to continue.
        
        Args:
            error_msg (str): The error message to print.
        """
        self._spacer()
        print(f"{self.__ERR} {error_msg}")
        self._continue()
    
    
    
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
        # Input loop
        while True:
            self._spacer()
            print(f"{self.__PRMPT} How many players are playing? Only 2-5 players are able to play.")
        
            try: # Capture and cast user input as an int
                num_players = int(self._input())
            except ValueError:
                # Input is not an integer
                self._error("Please enter a integer that is 2 or greater.")
                continue
            # End of try/except
            
            # Check if there are enough players
            if num_players < 2:
                self._error("There must be at least 2 players.")
            elif num_players > 5:
                self._error("There can't be more than 5 players.")
            else: # Valid input
                return num_players # Breaks Input loop
        # End of Input loop
    # End of prompt_num_players
    
    
    def prompt_player_names(self, num_players: int) -> list[Player]:
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
            # Input loop
            while True:
                # Prints the prompt for each player
                self._spacer()
                print(f"{self.__PRMPT} Player {i+1}'s name?")
        
                name = self._input()
                
                # Check if the name is empty or only digits
                if len(name) == 0 or name.isnumeric():
                    self._error("Please enter a name with at least some letters.")
                else:
                    # Valid input, append player then break
                    list_of_players.append(Player(name))
                    break
            # End of Input loop
            self._spacer() # Make some space in the terminal
        # End of for loop
        
        return list_of_players
    # End of prompt_player_names
    
    
    def alert_player_turn(self, player: Player) -> None:
        """
        Alerts which user's turn it is so their hand can't be seen by other players.

        Args:
            player (Player): The player whose turn it is.
        """
        self._spacer(50)
        print(f"{self.__GAME} It is {player.name}'s turn.")
        self._continue()
        
        
    # End of alert_player_turn
    
    
    def prompt_play_or_pass(self, player: Player) -> tuple[Card, bool]:
        """
        Prompts the user to play a card or pass.
        Their hand will be printed to the terminal to show them what they can play.
        To play a card, the user must enter the name of the card.
        The user cannot play a Defuse card here.
        
        The following key words have functionality:
            1. pass    - Effectively ends their turn. They will draw a card.
            2. show    - Prints the player's hand.
            3. <card>? - Prints the name and description of that card.
            4. ?       - Prints the name and description of all cards.
        All other input is invalid.

        Args:
            player (Player): The player whose turn it is.

        Returns:
            tuple[Card, bool]: Returns the card the user wants to play and
                               a boolean denoting whether the user wants to pass.
                               True means the user wants to pass, and False
                               means the user wants to play.
        """
        self._spacer(3)
        print(f"{self.__GAME} {player.sprintf_hand()}") # Print the player's hand
        
        # Input loop only breaks when valid input is returned
        while True:
            self._spacer()
            print(f"{self.__PRMPT} {player.name}, please enter one of the following:")
            print(f"{len(self.__PRMPT)*' '}   1) The name of the card from your hand to play")
            print(f"{len(self.__PRMPT)*' '}   2) The name of any card followed by \'?\' to see its description")
            print(f"{len(self.__PRMPT)*' '}   3) Just a \'?\' to see all card descriptions")
            print(f"{len(self.__PRMPT)*' '}   4) 'show' to see your hand")
            print(f"{len(self.__PRMPT)*' '}   5) 'pass' to end your turn and draw a card")
            
            input = self._input().lower()
            
            # Check for pass
            if input == 'pass' or input == '5': return (None, True)
            
            # Check for show, print hand if so
            if input == 'show' or input == '4':
                print(f"{self.__GAME} {player.sprintf_hand()}")
                self._spacer()
                continue
            
            # Check for just a '?'
            if input == '?' or input == '3':
                for card in Card:
                    self._spacer(2)
                    print(f"{self.__GAME} {card}")
                self._spacer()
                continue
            
            # Check for card description
            try:
                for card in Card:
                    if card.name().lower() == input[:-1]: # Card found
                        self._spacer(2)
                        print(f"{self.__GAME} {card}")    # Print the card's description
                        raise Exception()  # Break out of the for loop so the input loop can continue
            except Exception:
                self._spacer()
                continue
            
            # Check for defuse card
            if input == 'defuse':
                self._error("You can't play your Defuse card now.")
                continue
            
            # Check if the player has that card. If they do, play it.
            for card in player.hand:
                if card == Card.EK: continue       # Skip Exploding Kittens
                
                # Check if input is a cat card. They need to have a pair of like cats to play it.
                selected_pair: Card = None
                if input == Card.TCAT.name().lower(): selected_pair = Card.TCAT
                elif input == Card.HPCAT.name().lower(): selected_pair = Card.HPCAT
                elif input == Card.CATM.name().lower(): selected_pair = Card.CATM
                elif input == Card.RRCAT.name().lower(): selected_pair = Card.RRCAT
                elif input == Card.BCAT.name().lower(): selected_pair = Card.BCAT
                
                # Check if the player has a pair of like cats. If so, return it.
                if selected_pair and player.has_pair(selected_pair):
                    return (card, False)
                elif selected_pair and not player.has_pair(selected_pair):
                    self._error(f"You need a pair of {selected_pair.name()}s to play them.")
                    continue
                    
                # Otherwise, return the action card
                if card.name().lower() == input:
                    return (card, False)
            # End of for loop
            
            # Everything else is either unacceptable input or the player doesn't have the card
            self._error("Please enter \'pass\', \'show\', or a valid card name from your hand.")
        # End of Input loop
        
    # End of prompt_play_or_pass
    
# End of Prompter