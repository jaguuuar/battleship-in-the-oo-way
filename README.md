#  in the OOP way

## The story

Game Objective

The object of Battleship is to try and sink all of the other player's before they sink all of your ships. All of the other player's ships are somewhere on his/her board.  You try and hit them by calling out the coordinates of one of the squares on the board.  The other player also tries to hit your ships by calling out coordinates. Neither you nor the other player can see the other's board so you must try to guess where they are.

Starting a New Game

Each player places the 5 ships somewhere on their board. The board is a square with side's length equals 10 (spaces). The ships can only be placed vertically or horizontally. Diagonal placement is not allowed. No part of a ship may hang off the edge of the board.  Ships may not overlap each other.  No ships may be placed on another ship. Ships may not touch each other.

The 5 ships are: Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).

You sets ships by enter ship's name, answer the question if it's horizontal and the number of space which it occupies. You can add only one ship of each kind.

Once the guessing begins, the players may not move the ships.

Playing the Game

Player's take turns guessing by calling out the coordinates. The opponent responds with "hit" or "miss" as appropriate. Both players should mark their board with signs: 'X' for hit, 'O' for miss. For example, if you call out F6 and your opponent does not have any ship located at F6, your opponent would respond with "miss".  You record the miss F6 by placing a white peg on the lower part of your board at F6. Your opponent records the miss by placing.

When all of the squares that one your ships occupies have been hit, the ship will be sunk. You should announce "hit and sunk".

As soon as all of one player's ships have been sunk, the game ends.

Based on: https://www.cs.nmsu.edu/~bdu/TA/487/brules.htm



New requirements

There should be three game modes: Single player (PvC), Multiplayer (Hot Seat), Simulation (CvC).
There should be 3 difficulty levels (easy, medium, hard). Different levels should be different AI algorithms. AI should follow the same rules as human - AI cannot know player's ships' positions.
Hard level should be really difficult - mentor should have huge problems to win during evaluation.
Class krk 2016.1 should not implement or edit following classes: Ship, Square, Ocean, Player. It's 2017.1's responsibility. (We'll git blame you ;) )
There should be a hall of fame feature ;)
(*) If you're ambitious implement another game mode: Multiplayer over Internet.*
(*) Add sound effects :)*

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

* `is_hit`
  - data: bool
  - description: contains True if square was hit, otherwise contains False
  Default value is False

* `ship`
- data: string/None
- description: contains ship's *name* if is a part of *Ship*, otherwise contains None
    Default value is None.

__Instance methods__

* ##### ` __init__(self, ship, is_hit) `

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

* ##### ` __init__(self, ship_type, is_vertical, start_row, start_column, is_sunk) `

  Constructs a *Ship* object

* `build_ship(self, size)`

    Basing on provided *size*, construct a ship, by appending *Square* objects
    to *self.squares* list

* `check_if_sunk(self)`

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

### `player.py`

This is the file containing a logic of player.

### Class Player

__Instance Attributes__

* `name`
  - data: string
  - description: Player's name

* `is_winner`
- data: bool
- description: contains True if every *Ship* object's attribute *is_sunk* is set to True, otherwise contains False. Default value is False


__Instance methods__

* ##### ` __init__(self, name) `

  Constructs a *Player* object

* `insert_ships(self)`

    Inserts every player's *Ship* objects on attribute self.board in *Ocean*

* `get_ship_direction(self, ship_name)`

    Basing on user input, returns True if attribute *is_vertical of *Ship* object will be True, otherwise returns False

* `get_ship_coordinates(self, ship_name)`

    Basing on user input, returns *Ship* starting_point.
