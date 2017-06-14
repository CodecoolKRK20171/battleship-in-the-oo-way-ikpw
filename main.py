from squares import Square
from ocean import Ocean
from ships import Ship
from player import Player
import os
import sys


def choose_all_ships(player):

    ships = {"Carrier": 5,
            "Battleship": 4,
            "Cruiser": 3,
            "Submarine": 3,
            "Destroyer": 2}

    ships_list = ['Carrier']#, 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
    while len(ships_list) > 0:
        print("Ships left for {}: ".format(player.name))
        for ship in ships_list:
            print(ship)
        choose_ship = input("Choose ship: ")
        if choose_ship in ships_list:
            ships_list.remove(choose_ship)
            size = ships[choose_ship]
            direction = input('What direction vertical or horizontal (v or h)')
            if direction == 'v':
                is_vertical = True
                player.add_ship(positions_on_board(), size, is_vertical)
            elif direction == 'h':
                is_vertical = False
                player.add_ship(positions_on_board(), size, is_vertical)
            else:
                print('Wrong input')

        else:
            print("There is no such a ship")


def main_menu(player1, player2):

   print('''
         (1) Start game
         (0) Exit game
           ''')

   while True:
       choose = input("Enter action")
       if choose == '1':
           choose_all_ships(player1)
           choose_all_ships(player2)
           break
       elif choose == '0':
           sys.exit()
       elif choose.isalpha():
           raise ValueError


def positions_on_board():

    error_message = "Wrong coordinates"
    letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
               'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    while True:
       coordinate_x_y = input("Enter coordinates (a1): ")
       try:
           coordinate_x, coordinate_y = coordinate_x_y[0].upper(), int(coordinate_x_y[1])
       except ValueError:
           print(error_message)
       except IndexError:
           print(error_message)
       if coordinate_x in letters.keys() and coordinate_y in range(0, 10):
           target = ((letters[coordinate_x]), coordinate_y)
           return target
       else:
           print(error_message)

def print_boards(ocean1, ocean2):
    print("Your board\n")
    print(ocean1)
    print("Enemy board\n")
    print(ocean2)


def ask_name():

    name = input("Enter name: ")
    return name

def main():

    os.system('clear')
    ocean1 = Ocean()
    ocean2 = Ocean()
    ocean1.format_board()
    ocean2.format_board()
    player1 = Player(ask_name(), ocean1, ocean2)
    player2 = Player("Janusz", ocean2, ocean1)
    main_menu(player1, player2)
    while True:
        print_boards(ocean1, ocean2)
        player1.attack_position(positions_on_board())


if __name__ == "__main__":
   main()
