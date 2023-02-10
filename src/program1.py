####################################################################################
# Developer:        Devin Patel
# Project Title:    Programming Assignment 1
# Class:            CS 524-01 - Principles of Programming Languages
# Term:             SP 23
####################################################################################
# Filename:     program1.py
# Purpose:      This is the main program for Programming Assignment 1
#               and the starting point for Exploding Kittens.
####################################################################################

# Imports
from prog1_Card import Card
from prog1_Deck import Deck
from prog1_Player import Player

def main():
    deck = Deck(number_of_players=3)
    player1 = Player("Player 1")
    
    for _ in range(7): player1.add_card(deck.draw())
    print(player1)
    
# End of main



if __name__ == '__main__':
    main()

