from ships import Ship
from squares import Square

class Player:

    def __init__(self, name, ocean, enemy_ocean):

        self.name = name
        self.ocean = ocean
        self.enemy_ocean = enemy_ocean


    def attack_position(self, positions):

        """
        Method allows to attack ships

        Parameters
        ----------
        positions: attack positions on the ship

        Returns
        ---------
        None
        """

        self.enemy_ocean.board[positions[0]][positions[1]].fill_square()



    def add_ship(self, positions, size, is_vertical):

        """
        Method adds ships to the board.

        Parameters
        ----------
        size: lenght of ship
        coordinates: ship coords
        is_vertical: arrangement of the ship

        Returns
        ---------
        None
        """

        try:
            for i in range(size):
                if not is_vertical:
                    #self.valid_position(size, positions, is_vertical)
                    self.ocean.board[positions[0]][positions[1] + i].set_as_ship()
                else:
                    #self.valid_position(size, positions, is_vertical)
                    self.ocean.board[positions[0] + i][positions[1]].set_as_ship()

        except IndexError or AttributeError:
            print("Wrong coordinates!")

    def valid_position(self, size, coordinates, is_vertical):

        """
        Method checks that the ship can be placed on the board.

        Parameters
        ----------
        size: lenght of ship
        coordinates: ship coords
        is_vertical: arrangement of the ship

        Returns
        ---------
        None
        """

        max_postion = 10

        if is_vertical:
            if coordinates[0] + size >= max_postion:
                raise KeyError
        else:
            if coordinates[1] + size >= max_postion:
                raise KeyError

    def frame_make(self, positions):

        frame = []
        for position in positions:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    add_block = (position[0] + x, position[1] + y)
                    if add_block not in frame and add_block not in positions:
                        frame.append(add_block)

        return frame



    def win_lose(self):
        pass
