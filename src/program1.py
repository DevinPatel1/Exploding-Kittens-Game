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
from prog1_Game import Game

def main() -> None:
    game = Game()
    game.start()
    
    # Input loop to play again, reset the game, or quit.
    while True:
        play_again = input("Would you like to play again? (y/n): ").strip().lower()
        
        if play_again == 'y': # If yes, prompt to keep the players or reset
            play_reset = input("Would you like to reset the players? (y/n): ").strip().lower()
            print("\n"*4) # Clears the screen for the next game
            
            if play_reset == 'y': # If yes, reset game and start it.
                game.reset()
                game.start()
            elif play_reset == 'n': # If no, start another game in the same instance
                game.start()
            else: # Invalid input
                print("Invalid input. Please enter a \'y\' or \'n\'.")
                
        elif play_again == 'n': # If no, quit the program
            print("\n\nQuitting...")
            return
        else: # Invalid input
            print("Invalid input. Please enter \'y\' or \'n\'.")
    # End of input loop
# End of main

if __name__ == '__main__':
    main()
    exit(0)
