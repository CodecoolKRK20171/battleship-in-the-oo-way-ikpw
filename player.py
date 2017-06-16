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
        -------
        None
        """

        self.enemy_ocean.board[positions[0]][positions[1]].fill_square()
        if self.enemy_ocean.board[positions[0]][positions[1]].is_ship:
            print("HIT")
        else:
            print("MISS")

    def add_squares_around_horizontal(self, square_around_list, positions, size, is_horizontal):

        """
        Method adds squares around ship
        Parameters
        ----------
        size: lenght of ship
        coordinates: ship coords
        is_horizontal: arrangement of the ship
        Returns
        ---------
        None
        """

        for i in range(size):
            self.ocean.board[positions[1]][positions[0]+i].set_as_ship()
            for element in square_around_list:
                x = positions[1] + element[0]
                y = positions[0] + element[1] + i

                if x in range(0, 10) and y in range(0, 10):
                    self.ocean.board[x][y].water()

    def add_squares_around_vertical(self, square_around_list, positions, size, is_horizontal):

        for i in range(size):
            self.ocean.board[positions[1]+i][positions[0]].set_as_ship()
            for element in square_around_list:
                x = positions[0] + element[0] + i
                y = positions[1] + element[1]

                if x in range(0, 10) and y in range(0, 10):
                    self.ocean.board[x][y].water()

    def add_ship(self, positions, size, is_horizontal):

        """
        Method adds ships to the board.
        Parameters
        ----------
        size: lenght of ship
        coordinates: ship coords
        is_horizontal: arrangement of the ship
        Returns
        ---------
        None
        """

        positions_around_ship = [[-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0]]

        if is_horizontal:
            self.add_squares_around_horizontal(positions_around_ship, positions, size, is_horizontal)
        else:
            self.add_squares_around_vertical(positions_around_ship, positions, size, is_horizontal)

    def check_position(self, positions, size, is_horizontal):

        """
        Method checks that the ship can be placed on the board.
        Parameters
        ----------
        size: lenght of ship
        coordinates: ship coords
        is_horizontal: arrangement of the ship
        Returns
        ---------
        None
        """

        if is_horizontal:
            for i in range(size):
                x = positions[1]
                y = positions[0] + i

                if x in range(0, 10) and y in range(0, 10):
                    if self.ocean.board[x][y].is_water:
                        return False

                else:
                    return False
            return True

        else:
            for i in range(size):
                x = positions[1] + i
                y = positions[0]

                if x in range(0, 10) and y in range(0, 10):
                    if self.ocean.board[x][y].is_water:
                        return False

                else:
                    return False
            return True

    def is_win(self):
        pass
