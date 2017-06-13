class Squares:

    def __init__(self, row, column):

        self.row = row
        self.column = column
        self.is_marked = False

    def __str__(self):

        if self.is_marked:
            mark = 'X'
        else:
            mark = '0'
        return mark
