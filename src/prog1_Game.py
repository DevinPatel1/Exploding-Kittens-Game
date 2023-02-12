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
#   2. Prompt the user for the number of players and their names.
#   3. Instantiate a deck of cards and deal them to the players.
#   4. Cycle through the players' turns until someone loses to an Exploding Kitten.
#   5. A player's turn will consist of the following:
#       5.1. The player will be prompted to either enter a card to play or pass.
#       5.2. If the player plays a card, the game must apply the rules of that card.
#       5.3. If the player passes, nothing will happen.
#       5.4. The player will draw a card from the deck (assuming they haven't played a card that bypasses this).
#       5.5. If the player draws an Exploding Kitten, and they have a Defuse card, they will be prompted
#            to play it (default option) or not (which results in a loss and game over).
#       5.6. If the player draws an Exploding Kitten, and they do not have a Defuse card, they lose, and are no longer playing the game.
#            The player's play state will change to False, and the game will continue with the remaining players.
#       5.7. Once the player's turn is over, a prompt will be displayed to switch to the next player before continuing.
#    6. The game ends when one person is left, and the user will be prompted to either play again or quit in program1.main().
#    7. All user input will be sanitized and checked in an input loop prior to being used.
#       If any of the checks fail, the user will be reprompted to re-enter the input.
#
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
#   - _prompter (Prompter):        Facilitates user input for all game prompts
#   - _draw_pile (Deck):           Deck of cards representing the draw pile
#   - _players (list[Player]):     List of players
#   - _num_players (int):          Number of players in the game
#   - _remaining_players (int):    Number of players remaining in the game
#
# Methods:
#   + __init__(): Initializes the game object
#   + start(): Starts the game by initializing the attributes and entering the game loop
#   - _deal(): Deals cards to the players
#   - _game_loop(): Runs the game loop until a player loses,
#                   at which point the user is prompted to play again.
#   - _player_turn(player: Player, player_index: int): Facilitates a play-or-pass loop for a player's turn.
#   - _play_card(player: Player, player_index: int, card: Card): Facilitates the playing of a card.
#   - _end_turn(player: Player): Ends a player's turn and facilitates the drawing process.
####################################################################################

# Imports
from prog1_Card import Card
from prog1_Deck import Deck
from prog1_Player import Player
from prog1_Prompter import Prompter

class Game:
    """
    Game will facilitate Exploding Kittens functionality and game loop.
    """
    
    def __init__(self) -> None:
        """
        Declares the game class attributes.
        The start method will properly initialize the game attributes.
        """
        # Attributes are initialized here instead of in the class definition
        # to avoid the attributes being shared between all instances of the class.
        self._prompter = Prompter()
        self._draw_pile: Deck = None
        self._players: list[Player] = []
        self._num_players = -1
        self._remaining_players = 0
        
        # Prints welcome message
        self._prompter.print_welcome()
    # End of __init__
    
    
    ##############################
    # Setup Methods
    ##############################
    
    def start(self) -> None:
        """
        Starts the game by initializing the attributes and completing setup.
        Ends with entering the game loop.
        """
        print("A new game of Exploding Kittens has started!")
        
        # Prompt for number of players if this is the first game
        if self._num_players == -1: self._num_players = self._prompter.prompt_num_players()
        
        # Initialize the list of players if this is the first game
        if len(self._players) == 0: self._players = self._prompter.prompt_player_names(self._num_players)
        else: # Reset the players' play states if this is not a first game
            for player in self._players: player.reset()
        
        # Set the remaining players to the number of players
        self._remaining_players = self._num_players

        # Initialize the deck using the player count
        self._draw_pile = Deck(num_players=self._num_players)
        
        # Deal cards to players
        self._deal()
        
        # Setup complete, enter game loop
        self._game_loop()
    # End of start
    
    
    def _deal(self) -> None:
        """
        Deals cards to the players.
        Setup is as follows:
            1. Remove all Exploding Kittens from the deck
               (in this case, every drawn Exploding Kitten will be placed on the bottom).
            2. Every player gets 1 Defuse card to start with. The Deck reset() method handles
               what to do with the remaining Defuse cards. In this method, drawn Defuse cards
               get placed on the bottom.
            3. The deck was shuffled when it was instantiated, so there is no need to shuffle prior to dealing.
            4. Every player gets 7 cards such that their hand will have 7 cards plus 1 Defuse.
               As with steps 1 and 2, any drawn Defuses or Exploding Kittens will be placed on the bottom.
            5. Shuffle the deck again to get the Defuses and Exploding Kittens mixed out of the bottom.
        """
        # No action for Steps 1 and 3
        # Steps 2 and 4:
        for player in self._players:
            player.add_card(Card.D) # Step 2
            
            # Step 4:
            for i in range(7):
                draw = self._draw_pile.draw()
                
                # If drawn card is Defuse or Exploding Kitten, place it back on the bottom
                if draw == Card.D or draw == Card.EK:
                    self._draw_pile.place(draw, location='bottom')
                    i -= 1 # Draw again
                else: # Valid card drawn
                    player.add_card(draw)
            # End of step 4 for loop
        # End of step 2 and 4 for loop
        
        self._draw_pile.shuffle() # Step 5
    # End of _deal
    
    
    ##############################
    # Game Loop Method
    ##############################
    
    def _game_loop(self) -> None: # @bookmark _game_loop()
        """
        Game loop that cycles through the players' turns until everyone loses to an Exploding Kitten.
        All card rules are applied here.
        """
        current_player_index = 0  # Keep this value between 0 and _num_players-1
        
        # Game loop
        while True:
            current_player = self._players[current_player_index]
            
            # If there is only one player left, then they are the winner.
            if self._remaining_players == 1:
                break
            
            # If the player lost, skip them. Losing players have negataive remaining turns.
            if current_player.remaining_turns < 0: continue
            
            # If the player has no remaining turns, give them one turn.
            if current_player.remaining_turns == 0:
                current_player.remaining_turns += 1
                
            # If the player had an attack card played on them,
            # then remaining_turns will already be set to the correct
            # value in the previous player's turn.
            
            # Loops until player uses all their turns (usually breaks after one turn)
            while current_player.remaining_turns > 0:
                self._player_turn(current_player, current_player_index)
            
            # Player's turn is done, move to next player
            current_player_index += 1
            # Wrap around if current player was the last player
            if current_player_index >= self._num_players: current_player_index = 0
            
        # End of game loop
        
        # Game is over, display the winner and the wins scoreboard and return to main()
        # to prompt the user to play again.
        # @TODO Implement an end_game() method to do this.
        
    # End of _game_loop
    
    
    ##############################
    # Game Helper Methods
    ##############################
    
    def _player_turn(self, player: Player, player_index: int) -> None:
        """
        Facilitates a play-or-pass loop for a player's turn.
        Times to break loop:
            1. Player chooses to pass
            2. Player plays a Skip card
        Times to skip drawing a card:
            1. Player plays a Skip card
            2. Player plays a Defuse card
            3. Player plays an Attack card
        
        Args:
            player (Player): The current player whose turn it is.
            player_index (int): The index of the current player whose turn it is.
        """
        # Alert the player it is their turn
        self._prompter.alert_player_turn(player)
        
        # Play-or-pass loop that breaks when the player chooses to pass or a skip card is played.
        while True:
        
            # Prompt for card to play
            card, pass_ = self._prompter.prompt_play_or_pass(player)
            
            # If the player chooses to pass, end their turn and return to the game loop
            if pass_: break
            
            # If player plays a card, apply the rules of the card.
            self._play_card(card, player, player_index)
            
        # End of play-or-pass loop
        self._end_turn(player)
            
    # End of _player_turn
    
    
    def _play_card(self, card: Card, player: Player, player_index: int) -> None:
        """
        Checks the played card and performs the appropriate action.

        Args:
            card (Card): The card that was played
            player (Player): The player that played rthe card
            player_index (int): The index of the player that played the card
        """
        # @TODO Implement this method
        pass
    # End of _play_card

    
    
    def _end_turn(self, player: Player) -> None:
        """
        Ends the player's turn. This method handles the drawing process
        and handles Exploding Kitten draws and Defuse plays.
        
        Args:
            player (Player): The current player whose turn it is.
        """
        player.remaining_turns -= 1
        self._draw_card(player)
    # End of _end_turn
        

    def _draw_card(self, player: Player) -> None:
        """
        Facilitates the drawing process.
        Also handles Exploding Kitten draws and Defuse plays.
        
        Args:
            player (Player): The current player whose turn it is.
        """
        # @TODO Implement this method
        pass
    # End of _draw_card
# End of Game
