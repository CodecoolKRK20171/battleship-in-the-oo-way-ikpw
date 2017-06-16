class Square:

    def __init__(self, row, column):

        self.row = row
        self.column = column
        self.is_empty = True
        self.is_ship = False
        self.is_water = False

    def fill_square(self):
        self.is_empty = False

    def water(self):
        self.is_water = True

    def set_as_ship(self):
        self.is_ship = True

    def set_water(self):
        self.is_water = True

    def __str__(self):

        if self.is_empty:
            mark = '~'
        else:
            if self.is_ship:
                mark = 'X'
            else:
                mark = '0'

        return mark
