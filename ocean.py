from ships import Ship
from squares import Square


class Ocean:

    def __init__(self):
        self.ships = []
        self.board = []

    def __str__(self):

        ocean = ''
        for line in self.board:
            ocean += '|'
            line.insert(-1, '|')
            for square in line:
                ocean += str(square)

        return ocean


    def format_board(self):

        self.board = []
        for i in range(0, 10):
            squares_list = []
            for j in range(0, 10):
                squares_list.append(Square(i, j))
            squares_list.append("\n")
            self.board.append(temp_list)
