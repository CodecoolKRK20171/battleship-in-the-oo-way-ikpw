# Class Square
  This file contains class that makes parts of ships

__Attributes__

* data: bool
  - 'is_water': sets everything to one char

* data: bool
  - 'is_ship': sets bool to true if specific square is part of ship

* data: int
  - 'row': letters that are responsible for lines

* data: int
  - 'columns': numbers responsible for columns


__Instance methods__

 * ##### '__init__(self, row, column, is_picked)'

Constructs Squares of diffrent ships

  * '__str__()'

Returns formated string of one square ( x or 0)

  * 'fill_square(self)'

  set is_water to False than ship will be marked

  * 'set_as_ship(self)'

  set is_ship to true (that marks ship as X)
