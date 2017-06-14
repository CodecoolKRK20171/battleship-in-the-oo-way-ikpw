from squares import Square
from ocean import Ocean
from ships import Ship
from player import Player
import os


def choose_all_ships(ocean, player):

    ships_list = ['Carrier']#, 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
    while len(ships_list) > 0:
        choose_ship = input("Choose ship: ")
        if choose_ship in ships_list:
            ships_list.remove(choose_ship)
            direction = input('What direction vertical or horizontal (v or h)')
            if direction == 'v':
                is_vertical = True
            elif direction == 'h':
                is_vertical = False
            else:
                print('Wrong input')
            player.add_ship(positions_on_board(ocean), choose_ship, is_vertical)
        else:
            print("There is no such a ship")


def main_menu(player, ocean):
    print('''
          (1) Start game
          (0) Exit game
            ''')

    while True:
        choose = input("Enter action")
        if choose == '1':
            choose_all_ships(player, ocean)
        elif choose == '0':
            break
        if choose.isalpha():
            raise ValueError


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
    main_menu(ocean, player)
    while True:
        player.attack_position(positions_on_board(ocean))


if __name__ == "__main__":
    main()
