# Class Ship
  contains squares objects that togather creates ships
  Contains data necessary to make whole ship from separate square objects

__Atributes__

  * 'name'
    data: string
    description: name of the ship (out of 5 possible ships)
  * ' positions'
    data: tuples
    description: tuple of square objects togather creating ship
  * 'ship_length'
    data: int
    description: length of the current ship
  * 'placement'
    data: bool
    description: True if vertical or False if horizontal

__instance methods__

  * '__init__(self, name, positions)'
      creator of the ship with given positions
  * 'is_destroyed(self)'
      check if ship is destroyed or not
