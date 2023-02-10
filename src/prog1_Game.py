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
#       5.7. Once the player's turn is over, a prompt will be displayed to switch to the next player before continuing.
#    6. If the game is over, prompt the user to either play again or quit.
#       6.1. If the player wants to change the number of players, they will have to restart the program.
#    7. All user input will be sanitized and checked in an input loop prior to being used.
#       If any of the checks fail, the user will be reprompted to re-enter the input.
#
#####################################################################################
# Class Specification
#
# Since python does not support access protections on attributes (like protected or private)
# nor has a way to set constants, the following PEP8 python naming conventions will be used:
#   1. Any private attributes will be prefixed with a double underscore '__'.
#   2. Any public attributes will be directly accessible instead of using a getter.
#   3. Any methods that aren't meant to be used outside of the class will be
#      prefixed with a single underscore '_'.
#   4. Any constants will be all caps.
#
#
# Attributes:
#
#
# Methods:
#   + deal(): deals cards to the players
####################################################################################