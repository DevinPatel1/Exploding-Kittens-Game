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
#   - _current_player_index (int): Index of the current player in the _players list
#   - _num_players (int):          Number of players in the game
#   - _remaining_players (int):    Number of players remaining in the game
#
#
# Setup Methods:
#   + __init__(): Initializes the game object
#   + _setup(): Sets up the game by initializing the attributes
#   + _reset(): Resets the game attributes to their default values
#   - _deal(): Deals cards to the players
#
# Game Loop Method:
#   - _game_loop(): Runs the game loop until a player loses,
#                   at which point the user is prompted to play again.
# 
# Player Turn Methods:
#   - _increment_next_player(): Increments the current player index to the next player.
#   - _player_turn(player: Player): Facilitates a play-or-pass loop for a player's turn.
#   - _play_card(player: Player, card: Card): Facilitates the playing of a card.
#   - _draw_card(player: Player): Facilitates the drawing process for a player.
# 
# Action Card Methods:
#   - _defuse(player: Player): Facilitates the playing of a Defuse card.
#   - _nope_card(player: Player, played_card: Card): Facilitates the playing of a Nope card.
#   - _attack_card(player: Player): Facilitates the playing of an Attack card.
#   - _skip_card(player: Player): Facilitates the playing of a Skip card.
#   - _favor_card(player: Player): Facilitates the playing of a Favor card.
#   - _shuffle_card(player: Player): Facilitates the playing of a Shuffle card.
#   - _see_the_future_card(player: Player): Facilitates the playing of a See the Future card.
#   - _cat_cards(player: Player, card: Card): Facilitates the playing of a Cat card.
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
        The setup method will properly initialize the game attributes.
        """
        # Attributes are initialized here instead of in the class definition
        # to avoid the attributes being shared between all instances of the class.
        self._prompter = Prompter()
        self._draw_pile: Deck = None
        self._players: list[Player] = []
        self._current_player_index = 0
        self._num_players = -1
        self._remaining_players = 0
        
        # Prints welcome message
        self._prompter.print_welcome()
        
        # Performs setup
        self._setup()
        
        # Setup complete, enter game loop
        self._game_loop()
        
    # End of __init__
    
    
    ##############################
    # Setup Methods
    ##############################
    
    def _setup(self) -> None:
        """
        Sets up the game by initializing the attributes.
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
        
        # Set the current player index to 0
        self._current_player_index = 0

        # Initialize the deck using the player count if this is the first game. Else just reset the deck.
        if self._draw_pile: self._draw_pile.reset()
        else: self._draw_pile = Deck(num_players=self._num_players)
        
        # Deal cards to players
        self._deal()
    # End of _setup
    
    
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
            i = 0 # Counter for remaining cards to draw
            while i < 7:
                draw = self._draw_pile.draw()
                
                # If drawn card is Defuse or Exploding Kitten, place it back on the bottom
                if draw == Card.D or draw == Card.EK:
                    self._draw_pile.place(draw, location='bottom')
                else: # Valid card drawn
                    player.add_card(draw)
                    i+=1
            # End of step 4 for loop
        # End of step 2 and 4 for loop
        
        self._draw_pile.shuffle() # Step 5
    # End of _deal
    
    
    def _reset(self) -> None:
        """
        Resets the game attributes such that a game with new players can be started.
        """
        # 1) The draw pile needs to be set to None so that it can be reinstantiated with a different player count.
        # 2) Clear the players list.
        # 3) Set the number of players to -1 so that the number of players can be prompted for.
        # 4) The remaining players will be set in setup(), so it does not need to be reset here.
        # 5) Current player index will be set in setup(), so it does not need to be reset here.
        
        self._draw_pile = None
        self._players.clear()
        self._num_players = -1
    # End of _reset
    
    
    
    ##############################
    # Game Loop Method
    ##############################
    
    def _game_loop(self) -> None:
        """
        Game loop that cycles through the players' turns until everyone loses to an Exploding Kitten.
        All card rules are applied here.
        """
        # Program loop
        while True:
            # Game Loop
            while True:
                current_player = self._players[self._current_player_index]
                
                # If there is only one player left, then they are the winner.
                if self._remaining_players == 1:
                    break
                
                # If the player lost, skip them. Losing players have negative remaining turns.
                if current_player.remaining_turns < 0:
                    self._increment_next_player()
                    continue
                
                # If the player has no remaining turns, give them one turn.
                if current_player.remaining_turns == 0:
                    current_player.remaining_turns += 1
                
                # Alert the player it is their turn
                self._prompter.alert_player_turn(current_player)
                
                # Loops until player uses all their turns
                while current_player.remaining_turns > 0:
                    self._player_turn(current_player)
                
                # Player's turn is done, move to next player
                self._increment_next_player()
            # End of game loop
        
            # Game is over. Get the winning player.
            winner: Player = None

            for player in self._players:
                if player.remaining_turns >= 0:
                    winner = player
                    break

            # Increment the winner's win count
            winner.wins += 1

            # Now display the winner and the wins scoreboard
            self._prompter.print_winner(winner, self._players)
            
            # Prompt to start a new game or quit
            play_again = self._prompter.prompt_play_again()
            
            # Depending on what the user wants to do, either
            # quit, start a new game, or start a new game with new players
            match play_again:
                case 0: return          # Quit game
                case 1: self._setup()    # Start new game with same players
                case 2:                 # Start new game with new players
                    self._reset()
                    self._setup()
            # End of match
                
        # End of program loop
            
    # End of _game_loop
    
    
    ##############################
    # Player Turn Methods
    ##############################
    
    def _increment_next_player(self) -> None:
        """
        Increments the current player index to the next player.
        """
        # Player's turn is done, move to next player
        self._current_player_index += 1
        # Wrap around if current player was the last player
        if self._current_player_index >= self._num_players: self._current_player_index = 0
    # End of increment_next_player
    
    
    def _player_turn(self, player: Player) -> None:
        """
        Facilitates a play-or-pass loop for a player's turn.
        
        Times to break turn loop:
            1. Player chooses to pass
            2. Player plays an Attack card
            3. Player plays a Skip card
            
        Times to skip drawing a card:
            1. Player plays a Defuse card
            2. Player plays an Attack card
            3. Player plays a Skip card
        
        Args:
            player (Player): The current player whose turn it is.
        """
        # skip_draw is a boolean control flag that is set to True if the player has
        # to immediately end their turn without drawing.
        skip_draw: bool = None
        
        # Play-or-pass loop that breaks when the player chooses to pass or a skip card is played.
        while True:
        
            # Prompt for card to play
            card, pass_ = self._prompter.prompt_play_or_pass(player, self._draw_pile.size, self._draw_pile.get_num_EK())
            
            # If the player chooses to pass, end their turn and return to the game loop
            if pass_: break
            
            # Check if anyone wants to Nope this card
            noper = self._nope_card(player, card)
            
            # If the card was Nope'd, they don't get to play it
            # _nope_card() would have removed the Noped card from the player's hand
            if noper:
                self._prompter.report_nope(player, noper, card)
                continue
            else: skip_draw = self._play_card(card, player)
            
            # Break if skip_draw is True
            if skip_draw: break
        # End of play-or-pass loop
        
        # End of the player's turn, draw if allowed
        if player.remaining_turns > 0: player.remaining_turns -= 1
        if not skip_draw: self._draw_card(player)
            
    # End of _player_turn
    
    
    def _play_card(self, card: Card, player: Player) -> bool:
        """
        Checks the played card and performs the appropriate action.
        Returns a boolean control flag to indicate if the player should skip drawing a card.

        Args:
            card (Card): The card that was played
            player (Player): The player that played the card
        
        Returns:
            bool: False if the player should draw a card, True otherwise.
        
        Raises:
            ValueError: If an invalid card is played.
                        This should never happen since the input is validated in Prompter.play_or_pass().
        """
        SKIP_DRAW = True  # Constant for readability
        
        # Remove the card from the hand
        # For cat cards, it needs to be removed twice. The second remove_card call will be in Game._cat_cards().
        player.remove_card(card)
        
        # Check each card type and apply the appropriate action
        match card:
            case Card.A:                    # Attack
                self._attack_card(player)
                return SKIP_DRAW
            case Card.SK:                   # Skip
                return self._skip_card(player)
            case Card.F:                    # Favor
                self._favor_card(player)
                return not SKIP_DRAW
            case Card.SH:                   # Shuffle
                self._shuffle_card(player)
                return not SKIP_DRAW
            case Card.STF:                  # See the Future
                self._see_the_future_card(player)
                return not SKIP_DRAW
            case Card.TCAT:                 # Taco Cat
                self._cat_cards(player, Card.TCAT)
                return not SKIP_DRAW
            case Card.HPCAT:                # Hairy Potato Cat
                self._cat_cards(player, Card.HPCAT)
                return not SKIP_DRAW
            case Card.CATM:                 # Cattermelon
                self._cat_cards(player, Card.CATM)
                return not SKIP_DRAW
            case Card.RRCAT:                # Rainbow Ralphing Cat
                self._cat_cards(player, Card.RRCAT)
                return not SKIP_DRAW
            case Card.BCAT:                 # Bearded Cat
                self._cat_cards(player, Card.BCAT)
                return not SKIP_DRAW
            case _:                         # Invalid card
                raise ValueError(f"Invalid card played: {card.name()}")
    # End of _play_card


    def _draw_card(self, player: Player) -> None:
        """
        Facilitates the drawing process.
        Also handles Exploding Kitten draws and Defuse plays.
        
        Args:
            player (Player): The current player whose turn it is.
        """
        # Draw a card
        draw = self._draw_pile.draw()
        
        # Check if the card is an Exploding Kitten
        if draw == Card.EK:
            self._prompter.alert_draw(player, draw)
            self._defuse(player)
        
        # Else add it to the player's hand
        else:
            player.add_card(draw)
            self._prompter.alert_draw(player, draw)
    # End of _draw_card
    
    
    
    ##############################
    # Action Card Methods
    ##############################
    
    def _defuse(self, player: Player) -> None:
        """
        Handles the Defuse card actions.
        
        This card needs to accomplish the following:
            1. Prompt the user where to place the Defuse card.
            2. If the user specifies an index, then place the Exploding Kitten back in the draw pile at that index.
            3. If the user chooses not to use a Defuse card (i.e., the specified index is negative), then the player loses.
        
        Args:
            player (Player): The current player whose turn it is.
        """
        # If the player has a Defuse card, play it.
        if player.has_card(Card.D):
            # Prompt the player to play the Defuse card
            play_defuse = self._prompter.prompt_play_defuse(player, self._draw_pile.size-1)
            
            # Check if the return value was -1
            if play_defuse == '-1':
                pass # Fall through to the player losing.
            
            # Check if play_defuse is a number
            elif play_defuse.isnumeric():
                int_play_defuse = int(play_defuse)
                
                player.remove_card(Card.D)
                self._draw_pile.place(Card.EK, index=int_play_defuse)
                self._prompter.report_prompt_play_defuse(player, play_defuse)
                return
                # Else just fall through to the player losing.
                
            else: # play_defuse is one of the location keywords
                player.remove_card(Card.D)
                placed_index = self._draw_pile.place(Card.EK, location=play_defuse)
                if play_defuse == 'random': self._prompter.report_prompt_play_defuse(player, str(self._draw_pile.size-1 - placed_index))
                else: self._prompter.report_prompt_play_defuse(player, play_defuse)
                return
        # End of if player.has_card(Card.D)
        
        player.lose() # If the player does not have a Defuse card, they lose.
        self._prompter.player_lost(player)
        self._remaining_players -= 1
    

    def _nope_card(self, player: Player, played_card: Card) -> str:
        """
        Handles the Nope card actions.
        
        This card needs to accomplish the following:
            1. Go through a Nope loop that prompts the other players to play a Nope card.
            2. If a player plays a Nope card, then the rest of the players (including the current player) are prompted to counter-play a Nope card if they have one.
            3. If the counter-play occurs, then both Nope cards are discarded and the current player's card is still active. Loop again and reprompt.
            4. The loop ends when either no one counters a Nope or no one initiates a Nope.
        
        Args:
            player (Player): The player whose turn it is.
            played_card (Card): The card is going to be Nope'd.

        Returns:
            str or False: Noper's name if the final result was a Nope, False if the final result was not a Nope.
        """
        self._prompter.alert_nope(player, played_card)
        
        # Nope loop
        while True:
            noper = self._prompter.prompt_for_nope(played_card, player, self._players)
            if noper: counter_noper = self._prompter.prompt_for_counter_nope(noper, player, self._players)
            else: return False  # No one played a Nope card.
            
            # Card was noped and someone played a counter nope:
            if counter_noper:
                # Remove the nope cards from the players' hands. Current player still has an active card.
                noper.remove_card(Card.N)
                counter_noper.remove_card(Card.N)
                self._prompter.report_counter_nope(player, noper, counter_noper)
                
            # Card was noped but no one counter Nope'd
            else:
                # If the noped card was a pair of cats, both must be removed from the player's hand.
                if (played_card == Card.TCAT
                or  played_card == Card.HPCAT
                or  played_card == Card.CATM
                or  played_card == Card.RRCAT
                or  played_card == Card.BCAT):
                    player.remove_card(played_card)
                    player.remove_card(played_card)
                
                # Else remove just the one played card from the player's hand.
                else: player.remove_card(played_card)
                    
                # Remove the noper's nope card
                noper.remove_card(Card.N)
                return noper
            
            # Loop back and reprompt for another chance to nope the current player's card.
        # End of Nope loop
    # End of _nope_card
    
    
    def _attack_card(self, player: Player) -> None:
        """
        Handles the Attack card actions.
        
        This card needs to accomplish the following:
            1. Skip the current player's draw phase (handled in _play_card()).
            2. Add 2 turns plus the current player's remaining turns to the next player.
            3. Set the current player's remaining turns to 0, so the loop would break when their current turn ends.
        
        Args:
            player (Player): The player whose turn it is.
        """
        # Get next player
        try: next_player = self._players[self._current_player_index+1]
        except IndexError: next_player = self._players[0]
        
        # Add 2 turns (1 if there haven't been compounded attacks)
        # plus the current player's remaining turns to the next player
        if player.remaining_turns > 1: next_player.remaining_turns += player.remaining_turns + 2
        else: next_player.remaining_turns += player.remaining_turns + 1
        
        # Set the current player's remaining turns to 0
        player.remaining_turns = 0
        
        self._prompter.report_attack(player)
    # End of _attack_card


    def _skip_card(self, player: Player) -> bool:
        """
        Handles the Skip card actions.
        
        This card needs to accomplish the following:
            1. Immediately decrement the number of turns the player has left.
            2. Check if there are > 0 turns left.
               2.1 If so, return a False control flag to indicate the player should draw a card.
               2.2 If there are 0 turns left, return a True control flag to indicate the player should skip drawing a card.
        
        Args:
            player (Player): The player whose turn it is.
            
        Returns:
            bool: False if the the player has > 0 turns left, True otherwise.
        """
        if player.remaining_turns > 0: player.remaining_turns -= 1
        self._prompter.report_skip(player)
        return not player.remaining_turns > 0
    # End of _skip_card
    
    
    def _favor_card(self, player: Player) -> None:
        """
        Handles the Favor card actions.
        
        This card needs to accomplish the following:
            1. Prompt the current player to select a player to target.
            2. Send an alert to tell the target player to take over.
            3. Prompt the target player to select a card to give to the current player.
            4. Report the transaction before continuing the current player's turn.
        
        Args:
            player (Player): The player whose turn it is.
        """
        # Prompt the current player to select a player to target.
        target = self._prompter.prompt_play_favor(player, self._players)
        
        # Prompt the target player to select a card to give to the current player.
        target_card = self._prompter.prompt_play_favor_target(target, player)
        
        # Now perform the swap. The target card needs to be removed from the target player's hand
        # and added to the current player's hand.
        target.remove_card(target_card)
        player.add_card(target_card)
        
        # Swap complete, report what happened and return
        self._prompter.report_favor(player, target, target_card)
    # End of _favor_card
    
    
    def _shuffle_card(self, player: Player) -> None:
        """
        Handles the Shuffle card actions.
        
        This card needs to accomplish the following:
            1. Shuffle the draw pile.
        
        Args:
            player (Player): The player whose turn it is.
        """
        self._draw_pile.shuffle()
        self._prompter.report_shuffle(player)
    # End of _shuffle_card
    
    
    def _see_the_future_card(self, player: Player) -> None:
        """
        Handles the See the Future card actions.
        
        This card needs to accomplish the following:
            1. Fetch the top three cards of the draw pile.
            2. Tell the user what the top three cards are.
        
        Args:
            player (Player): The player whose turn it is.
        """
        self._prompter.report_see_the_future(player, self._draw_pile.peek_top_three())
    # End of _see_the_future_card
    
    
    def _cat_cards(self, player: Player, cat_card: Card) -> None:
        """
        Handles the Cat cards actions.
        
        This card needs to accomplish the following:
            1. Remove the second cat card from the player's hand.
            2. Prompt the current player to select a player to target.
            3. Randomly choose a card from the target player's hand to give to the current player.
            4. Report the transaction before continuing the current player's turn.
        
        Args:
            card (Card): The cat card that was played
            player (Player): The player whose turn it is.
        """
        # Remove the second card from the player's hand
        player.remove_card(cat_card)
        
        
        # Prompt the current player to select a player to target.
        target = self._prompter.prompt_play_cat(player, self._players, cat_card)
        
        # Randomly choose a card from the target player's hand to give to the current player.
        from random import choice
        target_card = choice(target.hand)
        
        # Now perform the swap. The target card needs to be removed from the target player's hand
        # and added to the current player's hand.
        target.remove_card(target_card)
        player.add_card(target_card)
        
        # Swap complete, report what happened and return
        self._prompter.report_cat(player, target, cat_card, target_card)
        
    # End of _cat_cards
    
    
# End of Game
