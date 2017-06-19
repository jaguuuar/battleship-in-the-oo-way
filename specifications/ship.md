
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
