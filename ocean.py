from squares import Square


class Ocean:

    def __init__(self):
        self.board = []

    def __str__(self):

        ocean = ''
        ocean += '0123456789\n'
        for line in self.board:
            for square in line:
                ocean += str(square)

        return ocean

    def format_board(self):
        """
        Method that format board to have 10 lists with Square object as items
        """

        self.board = []
        for i in range(0, 10):
            self.board.append([])
            for j in range(0, 10):
                self.board[i].append(Square(i, j))
            self.board[i].append("\n")
