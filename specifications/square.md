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
