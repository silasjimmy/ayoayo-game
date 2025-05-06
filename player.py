'''
Defines the player
'''
class Player():
    def __init__(self, name: str) -> None:
        self.name = name

    '''
    Creates a string representation of the Player object

    Return:
        (str) name of the player
    '''
    def __str__(self) -> str:
        return self.name
