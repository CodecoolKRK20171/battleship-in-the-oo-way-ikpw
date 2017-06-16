class Square:

    def __init__(self, row, column):

        self.row = row
        self.column = column
        self.is_empty = True
        self.is_ship = False
        self.is_water = False

    def fill_square(self):

        """
        Constructs Squares of diffrent ships

        Returns
        -------
        None
        """

        self.is_empty = False

    def water(self):

        """
        Constructs Squares of water

        Returns
        -------
        None
        """

        self.is_water = True

    def set_as_ship(self):

        """
        Set is_ship to true (that marks ship as X)

        Returns
        -------
        None
        """
        self.is_ship = True

    def __str__(self):

        """
        Returns formated string of one square ( x or 0)

        Parameters
        ----------
        positions: attack positions on the ship

        Returns
        -------
        None
        """

        if self.is_ship:
            mark = 'X'
        else:
            mark = '0'

        return mark
