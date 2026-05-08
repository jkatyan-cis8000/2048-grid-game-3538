# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

- src/grid.py: 4x4 grid state management, tile placement, cell availability checks
- src/board.py: Move logic (slide and merge), score tracking, game-over detection
- src/game.py: Game loop, input handling, turn management, state persistence
- src/ui.py: Terminal rendering, user input parsing, score/highest-tile display

## Interfaces

### grid.py
- Grid class with:
  - `__init__(): Grid` - creates empty 4x4 grid
  - `clone(): Grid` - deep copy of grid state
  - `is_empty(row, col) -> bool` - checks if cell is empty
  - `set_cell(row, col, value) -> None` - places tile at position
  - `get_cell(row, col) -> int` - retrieves tile value
  - `get_empty_cells() -> list[(row, col)]` - returns list of empty positions
  - `to_string() -> str` - returns grid for debugging

### board.py
- Board class with:
- `__init__(): Board` - creates board with initial tiles
- `clone(): Board` - deep copy of board state
- `move(direction) -> bool` - slides all tiles in direction, returns True if changed
- `get_score() -> int` - returns current score
- `get_highest_tile() -> int` - returns highest tile value on board
- `is_game_over() -> bool` - checks if no moves possible
- `to_string() -> str` - returns formatted grid for display

### game.py
- Game class with:
- `__init__(): Game` - initializes game state
- `start(): None` - starts the game loop
- `handle_input(key) -> bool` - processes arrow key, returns False if quit
- `get_status() -> dict` - returns score, highest_tile, grid state
- `is_running() -> bool` - checks if game is active

### ui.py
- UI class with:
- `render(board: Board, score: int, highest_tile: int) -> None` - displays game state
- `get_user_input() -> str` - reads arrow key or quit command
- `show_game_over(score: int, highest_tile: int) -> None` - displays end message
- `show_invalid_move() -> None` - indicates invalid move attempted

## Shared Data Structures

### Tile
- `value: int` - power of 2 (2, 4, 8, 16, ...)
- `position: (row, col)` - tuple of integers 0-3

### Direction
- String values: "up", "down", "left", "right"

### Game State
```python
{
    "score": int,
    "highest_tile": int,
    "grid": list[list[int]],  # 4x4 grid where 0 means empty
    "game_over": bool
}
```

## External Dependencies

- No external dependencies required
- Uses standard library: `random` for tile placement, `sys` for input handling
