####################################################################################
# Developer:        Devin Patel
# Project Title:    Programming Assignment 1
# Class:            CS 524-01 - Principles of Programming Languages
# Term:             SP 23
####################################################################################
# Filename:     prog1_Game.py
# Purpose:      To implement the main game functionality and game loop.
####################################################################################
# Design Requirements
#
# The Game class will be responsible for the following:
#   1. Run a game of Exploding Kittens per the rules of the board game (minus combos).
#   2. Prompt the user for the number of players and their names. Display a confirmation
#      of all the players and their names before continuing.
#   3. Instantiate a deck of cards and deal them to the players.
#   4. Cycle through the players' turns until someone loses to an Exploding Kitten.
#   5. A player's turn will consist of the following:
#       5.1. The player will be prompted to either enter a card to play or pass.
#       5.2. If the player plays a card, the game must apply the rules of that card.
#       5.3. If the player passes, nothing will happen.
#       5.4. The player will draw a card from the deck (assuming they haven't played a card that bypasses this).
#       5.5. If the player draws an Exploding Kitten, and they have a Defuse card, they will be prompted
#            to play it (default option) or not (which results in a loss and game over).
#       5.6. If the player draws an Exploding Kitten, and they do not have a Defuse card, they lose, and the game is over.
#            Increment that player's loss count and display the scoreboard for each player.
#       5.7. Once the player's turn is over, a prompt will be displayed to switch to the next player before continuing.
#    6. If the game is over, prompt the user to either play again or quit.
#       6.1. If the player wants to change the number of players, they will have to restart the program.
#    7. All user input will be sanitized and checked in an input loop prior to being used.
#       If any of the checks fail, the user will be reprompted to re-enter the input.
#
#####################################################################################
# Class Specification
# @TODO Finish this section as the code is written
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
#   - _draw_pile (Deck):        Deck of cards representing the draw pile
#   - _players (list: Player):  List of players
#   - _current_player (int):    Index of which player's turn it is
#   - _num_players (int):       Number of players in the game
#
# Methods:
#   + __init__(): Initializes the game object
#   + start(): Starts the game
#   - _deal(): Deals cards to the players
####################################################################################

# Imports
from prog1_Card import Card
from prog1_Deck import Deck
from prog1_Player import Player

class Game:
    """
    Game will facilitate Exploding Kittens functionality and game loop.
    """
    
    def __init__(self):
        """
        Declares the game class attributes.
        The start method will be in charge of properly initializing the game attributes.
        """
        # Attributes are initialized here instead of in the class definition
        # to avoid the attributes being shared between all instances of the class.
        self._draw_pile = Deck()
        self._players = []
        self._current_player = 0
        self._num_players = 0
    # End of __init__
    
# End of Game
