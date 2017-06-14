from ships import Ship
from squares import Square

class Player:

    def __init__(self, name, ocean, enemy_ocean):
        self.name = name
        self.ocean = ocean
        self.enemy_ocean = enemy_ocean


    def attack_position(self, positions):

        if self.enemy_ocean.board[positions[0]][positions[1]].is_ship:
            self.enemy_ocean.board[positions[0]][positions[1]].fill_square()
        else:
            self.enemy_ocean.board[positions[0]][positions[1]].fill_square()


    def add_ship(self, positions, size, is_vertical):

        try:
            for i in range(size):
                if not is_vertical:
                    self.ocean.board[positions[0]][positions[1] + i].set_as_ship()
                else:
                    self.ocean.board[positions[0] + i][positions[1]].set_as_ship()

        except IndexError:
            print("Wrong coordinates!")


    def valid_position(self, name, coordinates):
        pass


    def win_lose(self):
        pass
