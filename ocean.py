from ships import Ship
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

    def attack_position(self, positions):

        self.ocean.board[positions[0]][positions[1]].fill_square()

    def format_board(self):

        index = 0
        letters = 'ABCDEFGHIJ'
        self.board = []
        for i in range(0, 10):
            self.board.append([])
            for j in range(0, 10):
                self.board[i].append(Square(i, j))
            self.board[i].append("\n")

        self.second_board = self.board[:]

        #for line in self.second_board:
            #line.insert(0, letters[index])
            #line.insert(1, '|')
            #line.append('|')
            #index += 1
