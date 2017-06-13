from ships import Ship
from squares import Square


class Ocean:

    def __init__(self):
        self.ships = []
        self.board = []

    def __str__(self):

        letters = 'ABCDEFGHIJ'
        index = 0
        ocean = ''
        for line in self.board:
            ocean += '{}'.format(index) +' |'
            line.insert(-1, '|')
            index += 1
            for square in line:
                ocean += str(square)

        return ocean


    def format_board(self):

        self.board = []
        for i in range(0, 10):
            self.board.append([])
            for j in range(0, 10):
                self.board[i].append(Square(i, j))
            self.board[i].append("\n")
