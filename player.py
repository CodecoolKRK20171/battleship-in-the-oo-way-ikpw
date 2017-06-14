from ships import Ship
from squares import Square

class Player:

    ships = {"Carrier": 5,
            "Battleship": 4,
            "Cruiser": 3,
            "Submarine": 3,
            "Destroyer": 2}

    def __init__(self, ship_name, ocean):

        self.ocean = ocean
        self.size = Ship.ships[ship_name]


    def attack_position(self, positions):
        self.ocean.board[positions[0]][positions[1]].fill_square()


    def add_ship(self, positions, size, is_vertical):

        for i in range(self.size):
            if is_vertical:
                self.ocean.board[positions[1] + i][positions[0]].ship()
            else:
                self.ocean.board[positions[1]][positions[0] + i].ship()

        return positions



    def valid_position(self, name, coordinates):
        pass


    def win_lose(self):
        pass
