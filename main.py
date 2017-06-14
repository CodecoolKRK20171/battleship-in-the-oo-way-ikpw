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
            player.add_ship(positions_on_board(ocean),choose_ship , is_vertical)
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
            raise ValuError


def positions_on_board(ocean):

    letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    while True:
        print(ocean)
        coordinate_x_y = input("Enter coordinates (a1): ")
        try:
            coordinate_x, coordinate_y = coordinate_x_y[0].upper(), int(coordinate_x_y[1])
        except ValueError:
            print("Wrong dupa")
        except IndexError:
            print("Wrong pierogi")
        if coordinate_x in letters.keys() and coordinate_y in range(0, 10):
            target = ((letters[coordinate_x]), int(coordinate_y) + 2)
            return target
        else:
            print("Wrong nic")


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
