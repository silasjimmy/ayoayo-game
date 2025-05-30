from typing import Any
from constants import PLAYER_ONE_PIT_INDICIES, PLAYER_TWO_PIT_INDICIES, PLAYER_ONE_STORE_INDEX, PLAYER_TWO_STORE_INDEX
from player import Player

'''
Defines the Ayoayo game
'''
class Ayoayo():
    def __init__(self, player_one: Any, player_two: Any, seeds: int) -> None:
        self.board = []
        self.player_one = player_one
        self.player_two = player_two

        self.create_board(seeds)

    '''
    Initializes the board when the game begins.

    Arguments:
        seeds (int): the number of seeds to place in each pit
    '''
    def create_board(self, seeds) -> None:
        for x in range(14):
            if x == PLAYER_ONE_STORE_INDEX or x == PLAYER_TWO_STORE_INDEX:
                # Set the players stores to 0
                self.board.append(0)
            else:
                # Set the pits to `seeds` seeds each
                self.board.append(seeds)

    '''
    Updates the board state once a player makes a move

    Arguments:
        start_index (int): the player's selected pit index on the board

    Return:
        drop_index (int): the last pit index the player has sowed their seed
    '''
    def update_board(self, start_index: int) -> int:
        # Get the number of seeds from the selected pit
        seeds = self.board[start_index]

        # Clear the number of seeds in the selected pit
        self.board[start_index] = 0

        # Get the pit where the player will start sowing the seeds
        drop_index = start_index + 1

        # Update the pits
        for x in range(seeds):
            # Update the number of seeds in the pit at the specified index
            self.board[drop_index] = self.board[drop_index] + 1

            if drop_index == 13:
                # Start at the first pit if player reaches the end of the list
                drop_index = 0
            else:
                # Get the pit index which the player will sow the next seed
                drop_index = drop_index + 1

        return drop_index

    '''
    Creates a player for the game

    Arguments:
        player_name (str) name of the player to create

    Return:
        Player (obj) a player object
    '''
    def create_player(self, player_name: str) -> Any:
        return Player(player_name)

    '''
    Prints the current state of the board
    '''
    def print_board(self) -> None:
        print(
            '''
            player 1:
            store: {}
            {}

            player 2:
            store: {}
            {}

            Game has not ended
            '''.format(self.board[6], self.board[:6], self.board[13], self.board[7:13])
        )

    '''
    Determines the winner of the game

    Return:
        (obj) a Player object if either player is the winner, None if it is a tie
    '''
    def return_winner(self) -> Any:
        player_one_total = sum(self.board[:7])
        player_two_total = sum(self.board[7:])

        if player_one_total > player_two_total:
            return self.player_one
        elif player_two_total > player_one_total:
            return self.player_two
        else:
            return None

    '''
    Checks if the game is over

    Return:
        (bool) True if the game has ended, False otherwise
    '''
    def is_game_over(self) -> bool:
        player_one_pits_sum = sum(self.board[:6])
        player_two_pits_sum = sum(self.board[7:13])

        if player_one_pits_sum == 0 or player_two_pits_sum == 0:
            return True

        return False

    '''
    Controls the game play by alternating players' turns and updating the board

    Arguments:
        player_index (int): the current player
        pit_index (int): the pit position the current player chose to pick seeds from

    Return:
        last_pit_index (int): the index of the pit the current player finishes sowing their seeds
    '''
    def play_game(self, player_index: int, pit_index: int) -> None:
        # Get the player's store and pits to use in the current turn
        current_player_store_index = None
        current_player_pit_indicies = None
        opponent_player_pit_indicies = None

        # Get the pit index which the player will pick their seeds from
        start_index = None

        if player_index == 1:
            current_player_store_index = PLAYER_ONE_STORE_INDEX
            current_player_pit_indicies = PLAYER_ONE_PIT_INDICIES
            opponent_player_pit_indicies = PLAYER_TWO_PIT_INDICIES
            start_index = PLAYER_ONE_PIT_INDICIES[pit_index - 1]
        else:
            current_player_store_index = PLAYER_TWO_STORE_INDEX
            current_player_pit_indicies = PLAYER_TWO_PIT_INDICIES
            opponent_player_pit_indicies = PLAYER_ONE_PIT_INDICIES
            start_index = PLAYER_TWO_PIT_INDICIES[pit_index - 1]

        last_pit_index = self.update_board(start_index)

        if (last_pit_index in current_player_pit_indicies) and self.board[last_pit_index] == 1:
            # Get the position of the last_pit_index in the player's indicies list
            current_player_pit_index_pos = current_player_pit_indicies.index(
                last_pit_index)
            opponent_player_pit_index = opponent_player_pit_indicies[current_player_pit_index_pos]

            # Update the current player's store
            self.board[current_player_store_index] = self.board[current_player_store_index] + \
                self.board[opponent_player_pit_index] + 1

            # Clear the current player's last pit to sow a seed
            self.board[last_pit_index] = 0

            # Clear the opponent player's pit to have been grabbed
            self.board[opponent_player_pit_index] = 0

        return last_pit_index
