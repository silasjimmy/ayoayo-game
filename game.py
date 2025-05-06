from constants import PLAYER_ONE_STORE_INDEX, PLAYER_TWO_STORE_INDEX
from utils import is_play_valid
from ayoayo import Ayoayo
from player import Player

if __name__ == "__main__":
    # Initialize the players
    player_one_name = input("Enter player 1 name: ")
    player_one = Player(player_one_name)

    player_two_name = input("Enter player 2 name: ")
    player_two = Player(player_two_name)

    # Keeps track of the current player
    player_index = 1

    # Create the game
    game = Ayoayo(player_one, player_two)

    game.print_board()

    while not game.is_game_over():
        # Keep track of the current player's pit indicies
        current_player_store_index = PLAYER_ONE_STORE_INDEX if player_index == 1 else PLAYER_TWO_STORE_INDEX

        pit_index = input("Player {} take a turn: ".format(player_index))

        if is_play_valid(pit_index):
            selected_pit = int(pit_index)

            last_pit_index = game.play_game(player_index, selected_pit)

            game.print_board()

            if last_pit_index == current_player_store_index:
                continue
            else:
                # Change player's turn
                player_index = 2 if player_index == 1 else 1
        else:
            continue

    # Determine the winner of the game
    winner = game.return_winner()

    if winner:
        print("Winner is player {}: {}".format(player_index, winner))
    else:
        print("It's a tie")
