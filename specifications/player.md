# Class Player
  Module contains players choose and win or lose logic
  Atributes of player

__Atributes__

  * 'name'
    data: string
    description: nickname

__instance methods__

  * 'place_ships_on_board(self, input)'
    - take input from player to place ships on board
  * 'valid_position(self, name, coordinates)'
    -  checks if players input is in the board and ships are in separate places
  * 'attack_position(self)'
    - takes positions to attack ffrom player
  * 'win_lose(self)'
    - check if enemy or player ships still exist
