from squares import Square
from ocean import Ocean
from ships import Ship
from player import Player
import os
import sys


def choose_all_ships(player):
    """
    Function takes all neccesary information from player to place his ships

    Parameters
    ----------
    player: actual player

    Returns
    -------
    None
    """

    ships = {"Carrier": 5,
            "Battleship": 4}
            #"Cruiser": 3,
            #"Submarine": 3,
            #"Destroyer": 2}

    while len(ships.keys()) > 0:
        os.system('clear')
        print(player.ocean)
        print("Ships left for {}: ".format(player.name))
        for key, value in ships.items():
            print(key, value)
        choose_ship = input("Choose ship: ")
        if choose_ship in ships.keys():
            size = ships[choose_ship]
            direction = input('What direction vertical or horizontal (v or h)')
            if direction not in 'vh':
                print('Wrong input')
                continue
            elif direction == 'v':
                is_vertical = True
            elif direction == 'h':
                is_vertical = False
            player.add_ship(set_positions_on_board(), size, is_vertical)
            del ships[choose_ship]
        else:
            print("There is no such a ship")


def set_positions_on_board():
    """
    function takes coordinates from player

    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    error_message = "Wrong coordinates"
    letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
               'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    while True:
        try:
            coordinate_x_y = input("Enter coordinates (a1): ")
            if len(coordinate_x_y) > 2:
                print(error_message)
                coordinate_x, coordinate_y = coordinate_x_y[0].upper(), int(coordinate_x_y[1])
                if coordinate_x in letters.keys() and coordinate_y in range(0, 10):
                    target = ((letters[coordinate_x]), coordinate_y)
                    return target
                else:
                    print(error_message)
        except ValueError:
            print(error_message)



def change_turns(player):
    """
    Function that change turns of game from player one to player two

    Parameters
    ----------
    player: parameter with object of player

    Returns
    -------
    None
    """

    player.attack_position(set_positions_on_board())
    print("Your board")
    print(player.ocean)
    print("Enemy board")
    print(player.enemy_ocean)


def ask_name(player):
    """Function asks for nickname of the player"""

    name = input("Enter nickname {}: ".format(player))
    return name

def main():

    os.system('clear')
    ocean1 = Ocean()
    ocean2 = Ocean()
    ocean1.format_board()
    ocean2.format_board()
    player1 = Player(ask_name('player1'), ocean1, ocean2)
    player2 = Player(ask_name('player2'), ocean2, ocean1)
    choose_all_ships(player1)
    choose_all_ships(player2)

    while True:

        print("{} TURN".format(player1.name.upper()))
        change_turns(player1)
        print("{} TURN".format(player2.name.upper()))
        change_turns(player2)


if __name__ == "__main__":
   main()
