from squares import Square
from ocean import Ocean
from ships import Ship
from player import Player
import os


def main_menu(player):
    print('''
          (1) Start game
          (0) Exit game
            ''')

    choose = input("Enter action")
    if choose == '1':
        player.add_ship(positions_on_board(), 3, True)
    if choose.isalpha():
        raise ValuError


def positions_on_board(ocean):

    validate = '0123456789'
    while True:
        print(ocean)
        coordinate_x = input("Enter x: ")
        coordinate_y = input("Enter y: ")
        if coordinate_x not in validate and coordinate_y not in validate:
            os.system('clear')
            print("Wrong input")
        else:
            target = (int(coordinate_x), int(coordinate_y))
            return target


def main():

    ocean = Ocean()
    ocean.format_board()
    player = Player('Carrier', ocean)
    player.add_ship((2, 4), 'Carrier', True)
    while True:
        player.attack_position(positions_on_board(ocean))


if __name__ == "__main__":
    main()
