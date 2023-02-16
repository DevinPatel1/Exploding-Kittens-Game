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
#   + alert_player_turn(player: Player): Alerts which user's turn it is so their hand can't be seen by other players.
#   + prompt_play_or_pass(player: Player, cards_in_deck: int, num_EK: int): Prompts the user to play a card or pass.
#   + alert_draw(player: Player, card: Card): Alerts the user that they drew a card.
#   + player_lost(player: Player): Alerts the user that they lost the game.
#   + print_winner(winner: Player, players: list[Player]): Prints the winner of the game and the scoreboard of all players' wins.
#   + prompt_play_again(): Prompts the user to play again. If yes, prompt to play with the same players or different players.
#
# Action Card Methods:
#   + alert_nope(current_player: Player, played_card: Card): Alerts the user that they played a Nope card.
#   + prompt_for_nope(played_card: Card, current_player: Player, players: list[Player]): Prompts the user group to play a Nope card if they have one.
#   + prompt_for_counter_nope(noper: Player, current_player: Player, players: list[Player]): Prompts the user group to counter play a Nope card if they have one.
#   + report_nope(current_player: Player, noper: Player, noped_card: Card): Reports that the user played a Nope card.
#   + report_counter_nope(current_player:Player, noper: Player, counter_noper: Player): Reports that the user played a Counter Nope card.
#   + prompt_play_defuse(player: Player, max_index: int): Prompts the user to specify an index to place an Exploding Kitten card or set the index to -1 (i.e., they quit).
#   + prompt_play_favor(current_player: Player, players: list[Player]): Prompts the user to specify a player to target with a Favor card.
#   + prompt_play_favor_target(target: Player, stealer: Player): Prompts the targeted player to specify a card to give to the current player.
#   + report_attack(player: Player): Reports that the user played an Attack card.
#   + report_skip(player: Player): Reports that the user played a Skip card.
#   + report_favor(player: Player, target: Player, stolen_card: Card): Reports that the user played a Favor card and who they targeted.
#   + report_shuffle(player: Player): Reports that the user played a Shuffle card.
#   + report_see_the_future(player: Player, cards: list): Reports that the user played a See the Future card and shows the user the top 3 cards.
#   + report_cat(player: Player, target: Player, used_card: Card, stolen_card: Card): Reports that the user played a pair of cat cards and who they targeted.
#
# Macros:
#   - _input(prompt_symbol=">>"): Macro that creates the user input prompt and returns the string received from stdin.
#   - _spacer(lines: int): Macro that prints lines of whitespace to the terminal for readability.
#   - _continue(): Macro that prompts the user to press enter to continue.
#   - _game(game_msg: str): Macro that prints a game message to the terminal.
#   - _prompt(prompt_msg: str): Macro that prints a prompt message to the terminal.
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
    # End of _continue
    
    def _game(self, game_msg: str) -> None:
        """
        Macro that prints a game message to the terminal.
        
        Args:
            game_msg (str): The game message to print.
        """
        print(f"{self.__GAME} {game_msg}")
    # End of _game
    
    def _prompt(self, prompt_msg: str) -> None:
        """
        Macro that prints a prompt message to the terminal.
        
        Args:
            prompt_msg (str): The prompt message to print.
        """
        print(f"{self.__PRMPT} {prompt_msg}")
    # End of _prompt
    
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
    # End of _error
    
    
    
    ########################################
    # Prompt Methods
    ########################################
    
    def print_welcome(self) -> None:
        """
        Prints a welcome message to the user.
        """
        # Print ascii letter title
        print("#########################################################################################" + "\n"
            + "##    ______            _           _ _               _  ___ _   _                     ##" + "\n"
            + "##   |  ____|          | |         | (_)             | |/ (_) | | |                    ##" + "\n"
            + "##   | |__  __  ___ __ | | ___   __| |_ _ __   __ _  | ' / _| |_| |_ ___ _ __  ___     ##" + "\n"
            + "##   |  __| \\ \\/ / '_ \\| |/ _ \\ / _` | | '_ \\ / _` | |  < | | __| __/ _ \\ '_ \\/ __|    ##" + "\n"
            + "##   | |____ >  <| |_) | | (_) | (_| | | | | | (_| | | . \\| | |_| ||  __/ | | \\__ \\    ##" + "\n"
            + "##   |______/_/\\_\\ .__/|_|\\___/ \\__,_|_|_| |_|\\__, | |_|\\_\\_|\\__|\\__\\___|_| |_|___/    ##" + "\n"
            + "##               | |                           __/ |                                   ##" + "\n"
            + "##               |_|                          |___/                                    ##")
        
        print("##" + " "*85 + "##")
        print("##" + " "*85 + "##")
        
        # Print ascii cover art
        print("##" + " "*24 + "            _ ._  _ , _ ._                                   ##" + "\n"
            + "##" + " "*24 + "          (_ ' ( `  )_  .__)                                 ##" + "\n"
            + "##" + " "*24 + "        ( (  (    )   `)  ) _)                               ##" + "\n"
            + "##" + " "*24 + "       (__ (_   (_ . _) _) ,__)                              ##" + "\n"
            + "##" + " "*24 + "           `~~`\\ ' . /`~~`                                   ##" + "\n"
            + "##" + " "*24 + "   /\\_/\\        ;   ;        /\\_/\\                           ##" + "\n"
            + "##" + " "*24 + "  ( o.o )       /   \\       ( o.o )                          ##" + "\n"
            + "##" + " "*24 + " __> ^ <_______/_ __ \\_______> ^ <__                         ##" + "\n"
            + "#########################################################################################" + "\n\n")
        
        self._continue()
        self._spacer(10)
    # End of print_welcome
        
        
    
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
            self._prompt("How many players are playing? Only 2-5 players are able to play.")

            # Validate user input as int
            try:
                num_players = int(self._input())
            except ValueError:
                # Input is not an integer
                self._error("Please enter an integer that is between 2 and 5.")
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
            list[Player]: List of all the players as Player objects.
        """
        self._spacer()
        list_of_players = []
        
        # Some prompts require a keyword to be used, so we need to ensure no Players are named them
        LIST_OF_INVALID_NAMES = list([card.name().lower() for card in Card] # All the card names
                              + [card.name().lower()+'?' for card in Card]  # All the card names with a question mark
                              + ["show", "pass", "?", "no", "n", "yes", "y", "top", "bottom", "middle", "random"])
        
        for i in range(num_players):
            # Input loop
            while True:
                # Prints the prompt for each player
                self._spacer()
                self._prompt(f"Player {i+1}'s name?")
        
                name = self._input()
                
                # Check if the name is empty or only digits
                if len(name) == 0 or name.isnumeric():
                    self._error("Please enter a name with at least some letters.")
                    
                # Check if the name is one of the invalid names
                elif name.lower() in LIST_OF_INVALID_NAMES:
                    self._error("You can't use that name.")
                
                # Check if the name is a duplicate
                elif name in [p.name for p in list_of_players]:
                    self._error("Someone already took that name.")
                
                # Check if there are any letters in the name
                elif not name.isalnum():
                    self._error("Only letters and numbers are allowed.")
                
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
        Also alerts any effects present on the player (e.g., an attack card was played).

        Args:
            player (Player): The player whose turn it is.
        """
        self._spacer(50)
        self._game(f"It is {player.name}'s turn.\n")
            
        self._spacer()
        self._continue()
    # End of alert_player_turn
    
    
    def prompt_play_or_pass(self, player: Player, cards_in_deck: int, num_EK: int) -> tuple[Card, bool]:
        """
        Prompts the user to play a card or pass.
        Their hand will be printed to the terminal to show them what they can play.
        To play a card, the user must enter the name of the card.
        The user cannot play a Defuse or Nope card here.
        
        The following key words have functionality:
            1. pass    - Effectively ends their turn. They will draw a card.
            2. show    - Prints the player's hand.
            3. <card>? - Prints the name and description of that card.
            4. ?       - Prints the name and description of all cards.
        All other input is invalid.

        Args:
            player (Player): The player whose turn it is.
            cards_in_deck (int): The number of cards left in the deck.
            num_EK (int): The number of Exploding Kittens in the deck.

        Returns:
            tuple[Card, bool]: Returns the card the user wants to play and
                               a boolean denoting whether the user wants to pass.
                               True means the user wants to pass, and False
                               means the user wants to play.
        """
        self._spacer(3)
        self._game(player.sprintf_hand()) # Print the player's hand
        
        
        # Print information
        self._game("Stats:" + "\n"
                 + f"\tWins: {player.wins}" + "\n"
                 + f"\tCards in deck: {cards_in_deck}" + "\n"
                 + f"\tExploding Kittens: {num_EK}" + "\n"
                 + f"\tRemaining turns: {player.remaining_turns}" + "\n")
        
        # Input loop only breaks when valid input is returned
        while True:
            self._spacer()
            
            # Print the prompt
            self._prompt(f"{player.name}, please enter one of the following:")
            print(f"{len(self.__PRMPT)*' '}   1) The name of the card from your hand to play")
            print(f"{len(self.__PRMPT)*' '}   2) The name of any card followed by \'?\' to see its description")
            print(f"{len(self.__PRMPT)*' '}   3) Just a \'?\' to see all card descriptions")
            print(f"{len(self.__PRMPT)*' '}   4) 'show' to see your hand and stats")
            print(f"{len(self.__PRMPT)*' '}   5) 'pass' to end your turn and draw a card")
            
            input = self._input().lower()
            
            # Check for pass
            if input == 'pass' or input == '5': return (None, True)
            
            # Check for show, print hand if so
            if input == 'show' or input == '4':
                self._game(player.sprintf_hand())
                self._spacer()
                self._continue()
                # Print information
                self._game("Stats:" + "\n"
                         + f"\tWins: {player.wins}" + "\n"
                         + f"\tCards in deck: {cards_in_deck}" + "\n"
                         + f"\tExploding Kittens: {num_EK}" + "\n"
                         + f"\tRemaining turns: {player.remaining_turns}" + "\n")
                self._continue()
                continue
            
            # Check for just a '?'
            if input == '?' or input == '3':
                for card in Card:
                    self._spacer(2)
                    self._game(str(card))
                self._spacer()
                self._continue()
                continue
            
            # Check for card description
            if len(input) > 0 and input[-1] == '?':
                try:
                    for card in Card:
                        if card.name().lower() == input[:-1]: # Card found
                            self._spacer(2)
                            self._game(f"{card}\n")             # Print the card's description
                            self._continue()                    # Wait for user to continue
                            raise Exception("Dummy Exception")  # Break out of the for loop so the input loop can continue
                except Exception:
                    self._spacer()
                    continue
            
            # Check for defuse card
            if input == Card.D.name().lower():
                self._error("You can't play your Defuse card now.")
                continue
            
            # Check for nope card
            if input == Card.N.name().lower():
                self._error("You can't play your Nope card now.")
                continue
            
            # Check if the player has that card. If they do, play it.
            try:
                for card in player.hand:                    
                    # Check if input is a cat card. They need to have a pair of like cats to play it.
                    selected_pair: Card = None
                    if   input == Card.TCAT.name().lower():  selected_pair = Card.TCAT
                    elif input == Card.HPCAT.name().lower(): selected_pair = Card.HPCAT
                    elif input == Card.CATM.name().lower():  selected_pair = Card.CATM
                    elif input == Card.RRCAT.name().lower(): selected_pair = Card.RRCAT
                    elif input == Card.BCAT.name().lower():  selected_pair = Card.BCAT
                    
                    # Check if the player has a pair of like cats. If so, return it.
                    if selected_pair and player.has_pair(selected_pair):
                        return (selected_pair, False)
                    elif selected_pair and not player.has_pair(selected_pair):
                        self._error(f"You need a pair of {selected_pair.name()}s to play them.")
                        raise Exception("Dummy Exception") # Break out of the for loop so the input loop can continue

                    # Otherwise, return the action card
                    if card.name().lower() == input:
                        return (card, False)
                # End of for loop
            except Exception: continue
            
            # Everything else is either unacceptable input or the player doesn't have the card
            self._error("Please enter \'pass\', \'show\', or a valid card name from your hand.")
        # End of Input loop
    # End of prompt_play_or_pass
    
    
    def alert_draw(self, player: Player, card: Card):
        """
        Alerts the user the card they drew.
        """
        self._spacer(2)
        self._game(f"{player.name} drew a/an {card.name()}.")
        self._continue()
    # End of alert_draw
    
    
    def player_lost(self, player: Player) -> None:
        """
        Prints a message to the terminal to let the user know that they lost.

        Args:
            player (Player): The player who lost.
        """
        self._spacer(5)
        self._game(f"{player.name} has blown up. They can no longer play this game.")
        self._continue()
    # End of player_lost
    
    
    def print_winner(self, winner: Player, players: list[Player]) -> None:
        """
        Reports to the user that the game is over.
        Display the winner's name and the scoreboard of all the player's win counts.

        Args:
            winner (Player): Player who won
            players (list[Player]): List of all the players in the game
        """
        self._spacer(5)
        
        self._game(f"{winner.name} has won the game!\n")
        self._game("Here is the scoreboard:")

        # Prints each player's name and win count in a table
        print(f"{len(self.__GAME)*' '} \tName\tWins")
        print("".join(f"{len(self.__GAME)*' '} \t{p.name}\t{p.wins}\n" for p in players))
        
        self._spacer()
        self._continue()
    # End of print_winner
    
    
    def prompt_play_again(self) -> int:
        """
        Prompts the user if they would like to play again.
        If yes, ask a follow-up prompt to determine if they want to play with the same players.
        Return one of the following:
            0: Quit
            1: Play again with the same players
            2: Play again with different players

        Returns:
            int: 0: Quit, 1: Play again with the same players, 2: Play again with different players
        """
        self._spacer(5)
                
        # Input loop to play again, reset the game, or quit.
        while True:
            self._prompt("Would you like to play again? (y/n)")
            play_again = self._input().lower()
            
            if play_again == 'y': # If yes, prompt to keep the players or reset
                self._prompt("Would you like to reset the players? (y/n): ")
                play_reset = self._input().lower()
                self._spacer(5)
                
                if play_reset == 'y': # If yes, reset game and start it.
                    return 2
                elif play_reset == 'n': # If no, start another game in the same instance
                    return 1
                else: # Invalid input
                    print("Invalid input. Please enter a \'y\' or \'n\'.")
                    
            elif play_again == 'n': # If no, quit the program
                print("\n\nQuitting...")
                return 0
            else: # Invalid input
                print("Invalid input. Please enter \'y\' or \'n\'.")
        # End of input loop
    # End of prompt_play_again
    
    
    ###############################
    # Action Card Prompt Methods  
    ###############################
    
    def alert_nope(self, current_player: Player, played_card: Card) -> None:
        """
        Alerts the user group that an opportunity to Nope is available.

        Args:
            current_player (Player): The player who played the card.
            played_card (Card): The card that was played.
        """
        self._spacer(40)
        self._game(f"{current_player.name} played a/an {played_card.name()}.")
        self._continue()
    # End of alert_nope
    

    def prompt_for_nope(self, played_card: Card, current_player: Player, players: list[Player]) -> Player:
        """
        Prompts the user group if anyone wants to play a Nope card.
        
        If one does, check that player's hand for a Nope card.
            If they have one, return the player.
            If they don't, print an error message and reprompt.
        If they don't want to play a nope card, they must type "No".

        Args:
            played_card (Card): The card that is being Nope'd.
            current_player (Player): The player who is going to get Nope'd.
            players (list[Player]): List of all the players in the game.

        Returns:
            Player or False: Player if the card has been Nope'd, False if not.
        """
        self._spacer(10)

        # Input loop to get a valid player name or "No"
        while True:
            self._spacer(2)
            
            # Prompt for anyone wanting to play Nope
            self._prompt(f"Does anyone want to play a Nope card on {current_player.name}'s {played_card.name()}? Select a player or type \'No\'.")
            print("".join(f"{len(self.__PRMPT)*' '}   -> {p.name}\n" for p in players if p.remaining_turns >= 0 and p.name != current_player.name))

            input = self._input().lower()
            
            # Check if no one wants to play a Nope
            if input == 'no': return False
            
            # Check if they typed the current player's name
            if input == current_player.name.lower():
                self._error(f"{current_player.name}, you can't Nope your own card.")
                continue
            
            # Check if the input is a valid player name
            try:                
                for player in players:
                    if player == current_player: continue # Skip the current player
                    if player.remaining_turns < 0 and input == player.name.lower(): # Can't choose a player that is out of the game
                        self._error(f"{player.name} is out of the game.")
                        raise Exception("Dummy Exception")
                    
                    # If the input is a valid player name, check if they have a Nope card
                    if player.name.lower() == input:
                        if player.has_card(Card.N):
                            return player   # This player is playing a Nope card.
                        else:
                            self._error(f"{player.name} does not have a Nope card.")
                            raise Exception("Dummy Exception")
                        
            except Exception: continue  # Gets called if the input is invalid
                
            self._error("Please enter a player's name or \'No\'.")
        # End of input loop
    # End of prompt_for_nope
    

    def prompt_for_counter_nope(self, noper: Player, current_player: Player, players: list[Player]) -> Player:
        """
        Prompts the user group to counter play a Nope card if a Nope card has been used.
        
        If one does, check that player's hand for a Nope card.
            If they have one, return the player.
            If they don't, print an error message and reprompt.
        If they don't want to play a nope card, they must type "No".

        Args:
            noper (Player): The player that played the Nope card.
            current_player (Player): The player that got Nope'd.
            players (list[Player]): List of all the players in the game.

        Returns:
            Player or False: Player if anyone plays a counter nope, False if not.
        """
        self._spacer(10)
        self._game(f"{noper.name} played a {Card.N.name()} card on {current_player.name}.")
        self._continue()
        
        # Input loop to get a valid player name or "No"
        while True:
            self._spacer()
            
            # Prompt for anyone wanting to play Nope
            self._prompt(f"Does anyone want to counter-play a Nope card? Select a player or type \'No\'.")
            print("".join(f"{len(self.__PRMPT)*' '}   -> {p.name}\n" for p in players if p.remaining_turns >= 0 and p.name != noper.name))

            input = self._input().lower()
            
            # Check if no one wants to play a Nope
            if input == 'no': return False
            
            # Check if they typed the current player's name
            if input == noper.name.lower():
                self._error(f"{noper.name}, you can't Nope your own Nope card.")
                continue
            
            # Check if the input is a valid player name
            try:                
                for player in players:
                    if player == noper: continue # Skip the player that played the Nope card
                    if player.remaining_turns < 0 and input == player.name.lower(): # Can't choose a player that is out of the game
                        self._error(f"{player.name} is out of the game.")
                        raise Exception("Dummy Exception")     
                                   
                    # If the input is a valid player name, check if they have a Nope card
                    if player.name.lower() == input:
                        if player.has_card(Card.N):
                            return player   # This player is counter playing a Nope card.
                        else:
                            self._error(f"{player.name} does not have a Nope card.")
                            raise Exception("Dummy Exception")
                        
            except Exception: continue  # Gets called if the input is invalid
                
            self._error("Please enter a player's name or \'No\'.")
        # End of input loop
    # End of prompt_for_counter_nope
    
    
    def report_nope(self, current_player: Player, noper: Player, noped_card: Card):
        """
        Reports that a Nope card was played on a player.

        Args:
            current_player (Player): The player that got Nope'd.
            noper (Player): The player that played the Nope card.
        """
        self._spacer(3)
        self._game(f"{current_player.name} tried to play {noped_card.name()} but got Noped by {noper.name}.")
        self._continue()
    # End of report_nope
    
    def report_counter_nope(self, current_player:Player, noper: Player, counter_noper: Player):
        """
        Reports a counter Nope card was played on a player.

        Args:
            current_player (Player): The player that got Nope'd initially.
            noper (Player): The player that played a Nope card on current_player.
            counter_noper (Player): The player that counter played a Nope card on noper.
        """
        self._spacer(3)
        self._game(f"{noper.name} tried to Nope {current_player.name} but got counter-Noped by {counter_noper.name}.")
        self._continue()
    # End of report_counter_nope
    
    
    def prompt_play_defuse(self, player: Player, max_index: int) -> str:
        """
        Prompts the user to play a Defuse card if they have one.
        They can choose to play it or take the loss and quit playing.
        If they choose to play it, they must enter the index of where they want to place an Exploding Kitten
        or specify a location keyword as defined in the Deck.place() method.

        Args:
            max_index (int): The maximum index of where to place an Exploding Kitten.

        Returns:
            str: Returns either the index of where in the deck to place an Exploding Kitten as a string or a location keyword.
                 If the user wants to quit, return -1.
        """
        self._spacer(3)
        self._game(f"{player.name}, you drew an Exploding Kitten!\n{len(self.__GAME)*' '} Do you want to use your Defuse card (Y/n)?\n"
                 + f"{len(self.__GAME)*' '} (If you don't use your Defuse card, you'll lose the game.)")
        
        # Play input loop
        while True:
            input = self._input().lower()
            
            if input == 'y' or input == 'yes' or input == '': break
            elif input == 'n' or input == 'no': return '-1'
            else: self._error("Please enter \'y\' or \'n\'.")
        # End of play input loop
        
        
        # Now prompt for where to palce the Exploding Kitten
        self._game(f"Where do you want to place the Exploding Kitten?\n"
              + f"{len(self.__GAME)*' '} Enter one of the following inputs:\n"
              + f"{len(self.__GAME)*' '} \t1) An integer between 0 and {max_index} denoting how many cards below the top card it should be placed\n"
              + f"{len(self.__GAME)*' '} \t2) \'top\' to place it on top of the draw pile (next card)\n"
              + f"{len(self.__GAME)*' '} \t3) \'middle\' to place it in the middle of the draw pile\n"
              + f"{len(self.__GAME)*' '} \t4) \'bottom\' to place it on the bottom of the draw pile (last card)\n"
              + f"{len(self.__GAME)*' '} \t5) \'random\' to place it at a random index in the draw pile")
            
        # Index input loop
        while True:
            input = self._input()
            
            # Check for the keywords first
            if input == 'top': return 'top'
            elif input == 'middle': return 'middle'
            elif input == 'bottom': return 'bottom'
            elif input == 'random': return 'random'
            
            # All keywords checked, now validate input for int
            try:
                num_cards_down = int(input)
            except ValueError:
                # Input is not an integer
                self._error("Please enter an integer.")
                continue
            # End of try/except
            
            # Check if index is in bounds
            if num_cards_down < 0 or num_cards_down > max_index:
                self._error(f"Please enter an integer between 0 and {max_index}.")
                continue
            
            # Input is valid, return it
            return str(num_cards_down)
        # End of index input loop
    # End of prompt_play_defuse
    
    
    def report_prompt_play_defuse(self, player: Player, location: str) -> None:
        """
        Reports to the user where they placed the Exploding Kitten after using a Defuse.

        Args:
            player (Player): The player who played the Defuse card.
            location (str): The index or location where the Exploding Kitten was placed.
        """
        self._spacer(2)
        s = ""
        
        if location == 'top' or location == '0': s = "on top of the deck"
        elif location == 'middle': s = "in the middle of the deck"
        elif location == 'bottom': s = "on the bottom of the deck"
        elif location.isnumeric(): s = f"{location} cards from the top of the deck"
        
        self._game(f"{player.name} placed the Exploding Kitten {s}.")
        self._continue()
    # End of report_prompt_play_defuse
        
    
    def prompt_play_favor(self, current_player: Player, players: list[Player]) -> Player:
        """
        Prompts the user to specify which player to steal a card from.

        Args:
            current_player (Player): The player who played the Favor card.
            players (list[Player]): The list of players in the game.

        Returns:
            Player: The target player selected by the current player.
        """
        self._spacer(3)
        self._game(f"{current_player.name}, you played a Favor card.")
        
        # Input loop to get the target player
        while True:
            self._spacer()
            
            # Prompts user to enter a number to select the player
            self._prompt(f"Which player do you want to steal a card from? (Type a number)")
            
            # Loops to create the list of players to choose from
            print("".join(f"{len(self.__PRMPT)*' '}   {i}) {p.name}\n" for i, p in enumerate(players, start=1) if p.remaining_turns >= 0 and p != current_player))
                        
            # Now get and validate the input
            # Check if input is an integer
            try:
                index = int(self._input())-1
            except ValueError:
                self._error("Please enter an integer value.")
                continue
            
            # Check if integer is in range
            if index < 0 or index > len(players)-1:
                self._error("Please enter the number that corresponds to one of the listed players.")
                continue
            
            # Check if the player chosen is the current player
            chosen_player = players[index]
            if chosen_player == current_player:  # The references should be the same since both references came from the same list. This isn't a true equality check.
                self._error("You cannot choose yourself.")
                continue
            
            # Check if the chosen player is someone who is out of the game
            if chosen_player.remaining_turns < 0:
                self._error(f"{chosen_player.name} is out of the game.")
                continue

            # Checks passed, return the chosen player
            else: return chosen_player
        # End of input loop
    # End of prompt_play_favor
        
        
    def prompt_play_favor_target(self, target: Player, stealer: Player) -> Card:
        """
        Prompts the targeted player which card to give to the current player.

        Args:
            target (Player): The targeted player chosen by the current player.
            stealer (Player): The current player who played the Favor card.

        Returns:
            Card: The card the targeted player chose.
        """
        # Create a bunch of space and an alert to get the target player in the seat.
        self._spacer(50)
        self._game(f"{target.name} is now picking a card to give to {stealer.name}.")
        self._continue()
        
        # Input loop to get which card to give to the stealer
        while True: 
            self._spacer()
            
            # Prompt the target player to choose a card from their hand.
            self._prompt(f"Which card do you want to give to {stealer.name}? (Type a number)")
            print("".join(f"{len(self.__PRMPT)*' '}   {i}) {c.name()}\n" for i, c in enumerate(target.hand, start=1)))

            try:
                index = int(self._input())-1
            except ValueError:
                self._error("Please enter an integer value.")
                continue
            
            # Check if integer is in range
            if index < 0 or index > len(target.hand)-1:
                self._error("Please enter the number that corresponds to one of the listed cards.")
                continue
            
            # Checks passed, return the chosen card
            else: return target.hand[index]
        # End of input loop
    # End of prompt_play_favor_target
    
    
    def prompt_play_cat(self, current_player: Player, players: list[Player], played_card: Card) -> Player:
        """
        Prompts the user to specify which player to steal a card from.

        Args:
            current_player (Player): The player who played the Cat cards.
            players (list[Player]): The list of players in the game.

        Returns:
            Player: The target player selected by the current player.
        """
        self._spacer(3)
        self._game(f"{current_player.name}, you played a pair of {played_card.name()}s.")
        
        # Input loop to get the target player
        while True:
            self._spacer()
            
            # Prompts user to enter a number to select the player
            self._prompt(f"Which player do you want to steal a card from? (Type a number)")
            
            # Loops to create the list of players to choose from
            print("".join(f"{len(self.__PRMPT)*' '}   {i}) {p.name}\n" for i, p in enumerate(players, start=1) if p.remaining_turns >= 0 and p != current_player)) # Print the player in an enumerated list            # End of for loop
                        
            # Now get and validate the input
            # Check if input is an integer
            try:
                index = int(self._input())-1
            except ValueError:
                self._error("Please enter an integer value.")
                continue
            
            # Check if integer is in range
            if index < 0 or index > len(players)-1:
                self._error("Please enter the number that corresponds to one of the listed players.")
                continue
            
            # Check if the player chosen is the current player
            chosen_player = players[index]
            if chosen_player == current_player:  # The references should be the same since both references came from the same list. This isn't a true equality check.
                self._error("You cannot choose yourself.")
                continue
            
            # Check if the chosen player is someone who is out of the game
            if chosen_player.remaining_turns < 0:
                self._error(f"{chosen_player.name} is out of the game.")
                continue

            # Checks passed, return the chosen player
            else: return chosen_player
        # End of input loop
    # End of prompt_play_cat
    
    
    def report_attack(self, player: Player) -> None:
        """
        Reports to the user that a player played an Attack card.

        Args:
            player (Player): The player who played the Attack card.
        """
        self._spacer(3)
        self._game(f"{player.name} played an {Card.A.name()} card. The next person now has to take two additional turns.")
        self._continue()
    # End of report_Attack   
    
    
    def report_skip(self, player: Player) -> None:
        """
        Reports to the user that a player played a Skip card.

        Args:
            player (Player): The player who played the Skip card.
        """
        self._spacer(3)
        self._game(f"{player.name} played a {Card.SK.name()} card. The number of turns has been decreased by 1.")
        self._continue()
    # End of report_Skip
    
    
    def report_favor(self, player: Player, target: Player, stolen_card: Card) -> None:
        """
        Reports to the user that a player played a Favor card, who they targeted, and what card they stole.

        Args:
            player (Player): The player who played the Favor card.
            target (Player): The player who was targeted by the Favor card.
            stolen_card (Card): The card that was stolen from the target.
        """
        self._spacer(3)
        self._game(f"{player.name} used a {Card.F.name()} card to steal a/an {stolen_card.name()} from {target.name}.")
        self._continue()
        
        self.alert_player_turn(player)
    # End of report_Favor
    
    
    def report_shuffle(self, player: Player) -> None:
        """
        Reports to the user that a player played a Shuffle card.

        Args:
            player (Player): The player who played the Shuffle card.
        """
        self._spacer(3)
        self._game(f"{player.name} played a {Card.SH.name()} card. The deck is now shuffled.")
        self._continue()
    # End of report_Shuffle
    
    
    def report_see_the_future(self, player: Player, cards: list[Card]) -> None:
        """
        Reports to the user that a player played a See the Future card and shows them the next three cards in the deck.

        Args:
            player (Player): The player who played the See the Future card.
            cards (list[Card]): The next three cards in the deck.
        """
        self._spacer(3)
        self._game(f"{player.name} played a {Card.STF.name()} card.\n{len(self.__GAME)*' '} The next three cards from the top of the deck are:")
        for i, card in enumerate(cards, start=1): print(f"{len(self.__GAME)*' '} \t{i}) {card.name()}")
        self._continue()
    # End of report_see_the_future
    
    
    def report_cat(self, player: Player, target: Player, used_card: Card, stolen_card: Card) -> None:
        """
        Reports to the user that a player played a Cat card, who they targeted, and what card they stole.

        Args:
            player (Player): The player who played the Cat card.
            target (Player): The player who was targeted by the Cat card.
            used_card (Card): The pair of cards that was used to steal stolen_card.
            stolen_card (Card): The card that was stolen from the target.
        """
        self._spacer(3)
        self._game(f"{player.name} used a pair of {used_card.name()}s to steal a/an {stolen_card.name()} from {target.name}.")
        self._continue()
    # End of report_cat
    
# End of Prompter
