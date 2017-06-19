# Battleship in the OOP way

## The story

## Specification


__main.py__

### `main.py`

This is the file containing flow of the programm

__Functions__


* `print_menu()`

  Prints main menu

* `main()`

  Handle the flow of menu and program.

__square.py__


### `square.py`

This is the file containing a logic of squares (single pieces of ship)

### Class Square


__Instance Attributes__

* `row`
  - data: int
  - description: row coordinate

* `column`
- data: int
- description: column coordinate

* `is_hit`
  - data: bool
  - description: contains True if square was hit, otherwise contains False
  Default value is False

* `is_ship_part`
- data: bool
- description: contains True if square is a part of a ship, otherwise contains False (if is a part of board)

__Instance methods__

* ##### ` __init__(self, row, column) `

  Constructs a *Square* object

* `hit(self)`

  Marks *is_hit* attribute of *Square* object as True

* `__str__(self)`

  Returns 'X' if *is_hit* attribute of *Square* object is True,
  otherwise returns ' ' (empty string)


__ship.py__



### `ship.py`

This is the file containing a logic of ship (made out of squares).

### Class Ship

__Instance Attributes__

* `size`
  - data: int
  - description: number of squares that make a ship

* `is_sunk`
- data: bool
- description: contains True if all of the *Square* objects (in this ship) has an attribute *is_hit* set to True, otherwise contains False. Default value is False.

* `is_vertical`
- data: bool
- description: contains True if *Ship* placement is vertical, otherwise (horizontal) contains False.

* `start_row`
  - data: int
  - description: row coordinate where *Ship* object starts

* `start_column`
- data: int
- description: column coordinate where *Ship* object starts

* `squares`
- data: list
- description: list contains *Square* objects that make a *Ship* object

* `is_sunk`
- data: bool
- description: Contains True if every *Square* object that makes a *ship* has an attribute *is_hit* set to True,
otherwise contains False, default value is False

__Instance methods__

* ##### ` __init__(self, size, is_vertical, start_row, start_column) `

  Constructs a *Ship* object

* `build_ship(self, size)`

    Makes a string that simbolises a ship (based on provided size)

* `check_if_sunk(self, is_sunk)`

    Returns True if every *Square* objects attributes *is_hit* are set to True, otherwise returns False.
    Default value is False.

* `__str__(self)`

    Returns a formatted string (joined lists of squares that make a ship)


__ocean.py__

### `ocean.py`

This is the file containing a logic of board.

### Class Ocean

__Instance Attributes__

* `ships`
  - data: list
  - description: list contains *Ship* objects

* `board`
- data: list
- description: list contains *Square* objects


__Instance methods__

* ##### ` __init__(self) `

  Constructs a *Ocean* object

* `build_board(self)`

    Fills the *board* with *Square* objects

* `are_sunk(self)`

    Returns True if every *Ship* objects attributes *is_sunk* are set to True, otherwise returns False.
    Default value is False.

* `insert_ships(self)`

    Fills the *board* with *Ship* objects

* `__str__(self)`

    Returns a formatted string (board)
