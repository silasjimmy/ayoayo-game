from typing import List, Any

# Keeps track of the players' pit and store positions in the game board
PLAYER_ONE_STORE_INDEX = 6
PLAYER_TWO_STORE_INDEX = 13
PLAYER_ONE_PIT_INDICIES = [0, 1, 2, 3, 4, 5]
PLAYER_TWO_PIT_INDICIES = [7, 8, 9, 10, 11, 12]


class Ayoayo():
    def __init__(self) -> None:
        self.board = []
        self.player_one = None
        self.player_two = None

        self.create_board()

    '''
    Initializes the board when the game begins.

    Creates 12 pits with 4 seeds in each pit and 2 stores with 0 seeds in each store
    '''

    def create_board(self) -> None:
        for x in range(14):
            if x == PLAYER_ONE_STORE_INDEX or x == PLAYER_TWO_STORE_INDEX:
                # Set the players stores to 0
                self.board.append(0)
            else:
                # Set the pits to 4 seeds each
                self.board.append(4)

    '''
    Updates the board state once a player makes a move

    Arguments:
        start_index (int): the player's selected pit index on the board

    Return:
        drop_index (int): the last pit index the player has sowed their seed
    '''

    def update_board(self, start_index) -> int:
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

    parameter:
        player_name (str) name of the player to create

    return:
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
            '''.format(self.board[6], self.board[:6], self.board[13], self.board[7:13])
        )

    def return_winner(self):
        return 'winner'

    def play_game(self, player_index: int, pit_index: int) -> None:
        # Get the pit index which the player will pick their seeds from
        start_index = None

        if player_index == 1:
            start_index = PLAYER_ONE_PIT_INDICIES[pit_index - 1]
        else:
            start_index = PLAYER_TWO_PIT_INDICIES[pit_index - 1]

        self.update_board(start_index)


class Player():
    def __init__(self, name: str) -> None:
        self.name = name

    '''
    Creates a string representation of the Player object

    return:
        (str) name of the player
    '''

    def __str__(self) -> str:
        return self.name


# Create the game
game = Ayoayo()

# # Initialize player 1
# player_name = input("Enter player 1 name: ")
# game.player_one = Player(player_name)

# # Initialize player 2
# player_name = input("Enter player 2 name: ")
# game.player_one = Player(player_name)

# # Start the game play
# pit_index = input("Player 1 take a turn: ")

# # Check if the input is an integer
# if pit_index.isdigit():
#     pit_index = int(pit_index)

#     # Check if the pit index is valid
#     if pit_index <= 0 or pit_index > 6:
#         print("Invalid play! Please enter a number between 1 and 6 to continue")
#     else:
#         game.play_game(1, pit_index)
# else:
#     print("Invalid play! Please enter a number to continue")

game.play_game(2, 6)
