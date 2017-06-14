class Square:

    def __init__(self, row, column):

        self.row = row
        self.column = column
        self.is_empty = True
        self.is_ship = False

    def __str__(self):

        if self.is_empty:
            mark = ' '
        else:
            if self.is_ship:
                mark = 'X'
            else:
                mark = '0'
        return mark

    def fill_square(self):
        self.is_empty = False

    def ship(self):
        self.is_ship = True
