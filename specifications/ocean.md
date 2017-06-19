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
