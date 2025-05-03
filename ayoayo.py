from typing import List, Any


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
            if x == 6 or x == 13:
                self.board.append(0)
            else:
                self.board.append(4)

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
        self.print_board()


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

# Initialize player 1
player_name = str(input("Enter player 1 name: "))
game.player_one = Player(player_name)

# Initialize player 2
player_name = str(input("Enter player 2 name: "))
game.player_one = Player(player_name)

game.play_game(1, 2)
