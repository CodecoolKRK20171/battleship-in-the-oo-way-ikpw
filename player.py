from ocean import Ocean
from ship import Ship

class Player:
    def __init__(self, name):
        self.name = name

    def place_ships_on_board(self, ):
        '''take input from player to place ships on board'''

        available_ships = ['Carrier (5)', 'Battleship (4)', 'Cruiser (3)', 'Submarine (3)', 'Destroyer (2)']


    def valid_position(self, name, coordinates):
        '''checks if players input is in the board and ships are in separate places'''

        pass

    def attack_position(self):
        '''takes positions to attack from player'''

        pass

    def win_lose(self):
        '''check if enemy or player ships still exist'''

        pass
