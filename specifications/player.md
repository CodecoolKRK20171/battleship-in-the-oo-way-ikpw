# Class Player
  Module contains players choose and win or lose logic
  Atributes of player

__Atributes__

  * 'name'
    data: string
    description: nickname

__instance methods__

  * '__init__(self, name, ocean, enemy_ocean)'
    - name: name of the player
    - ocean: board of the player
    - enemy_ocean: board of the enemy player
  * 'valid_position(self, name, coordinates)'
    -  checks if players input is in the board and ships are in separate places
  * 'attack_position(self)'
    - takes positions to attack ffrom player
  * 'add_ship(positions, size, is_vertical)'
    - function makes ships in right coordinates
    - size: size of the ship(value from dict)
    - positions: tuple of coordinates
    - is_vertical: bool that decides if ship will be vertical or horizontal
  * 'win_lose(self)'
    - check if enemy or player ships still exist
