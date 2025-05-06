'''
Validates the player's input to check if the selected pit is valid
'''


def is_play_valid(selected_pit: str) -> bool:
    # Check if the input is an integer
    if selected_pit.isdigit():
        selected_pit = int(selected_pit)

        # Check if the pit index is valid
        if selected_pit <= 0 or selected_pit > 6:
            print("Invalid play! Please enter a number between 1 and 6 to continue")

            return False
        else:
            return True
    else:
        print("Invalid play! Please enter a number to continue")

        return False
