# UI Module Design

## Overview

The `src/ui.py` module handles all terminal-based rendering and user input for the 2048 game. It provides a clean interface between the game logic and the terminal display.

## Architecture

```
┌─────────────────────────────────────┐
│         Terminal Display            │
│  ┌───────────────────────────────┐  │
│  │   UI.render()                 │  │
│  │   - 4x4 grid display          │  │
│  │   - Score and highest tile    │  │
│  │   - Game instructions         │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
            ↑            ↓
┌─────────────────────────────────────┐
│         Input Handling              │
│  ┌───────────────────────────────┐  │
│  │   UI.get_user_input()         │  │
│  │   - Arrow key detection       │  │
│  │   - Quit command ('q')        │  │
│  │   - Termios/raw mode          │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
            ↑            ↓
┌─────────────────────────────────────┐
│         Game State Messages         │
│  ┌───────────────────────────────┐  │
│  │   UI.show_game_over()         │  │
│  │   UI.show_invalid_move()      │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

## Components

### UI Class

The `UI` class provides four core methods:

#### `render(board, score, highest_tile)`
- Displays the complete game state
- Shows a 4x4 grid with visual borders
- Displays current score and highest tile
- Shows control instructions

**Implementation details:**
- Uses `board.to_string()` to get grid data
- Formats each cell with consistent width
- Uses ASCII box-drawing characters for borders
- Clears previous output implicitly (user should clear terminal before calling)

#### `get_user_input()`
- Reads single character input from stdin
- Supports arrow keys using ANSI escape sequences
- Supports 'q' or 'Q' to quit
- Uses `termios` and `tty` for raw input mode

**Arrow key detection:**
- `\x1b[A` = Up arrow
- `\x1b[B` = Down arrow  
- `\x1b[C` = Right arrow
- `\x1b[D` = Left arrow

**Error handling:**
- Saves and restores terminal settings
- Handles Ctrl+C (SIGINT) gracefully

#### `show_game_over(score, highest_tile)`
- Displays end-of-game summary
- Shows final score and highest tile achieved
- Provides closing message

#### `show_invalid_move()`
- Indicates move was not accepted
- Displays brief error message
- Used when player attempts invalid move

## Design Decisions

### 1. Terminal Input Mode
Using `termios` and `tty` to set raw mode allows immediate character reading without waiting for Enter. This provides a better user experience for arrow key input.

### 2. No External Dependencies
The module uses only Python standard library:
- `sys` - stdin handling
- `termios` - terminal control
- `tty` - raw mode setup

### 3. Pure Text Rendering
All rendering uses ASCII characters for maximum compatibility across terminals. NoANSI color codes or cursor positioning used (simple layout only).

### 4. Board Interface
The UI accepts a Board object and uses its `to_string()` method for grid display. This decouples the UI from board implementation details.

## Usage

```python
from src.ui import UI
from src.board import Board

ui = UI()
board = Board()

# Display game state
ui.render(board, score=0, highest_tile=0)

# Get user input
key = ui.get_user_input()
if key == 'up':
    # Process up arrow
elif key == 'quit':
    # Exit game

# Show messages
ui.show_invalid_move()
ui.show_game_over(score=100, highest_tile=128)
```

## Limitations

- No support for window resizing
- No persistent display updates (re-renders full screen each time)
- No color support
- Arrow key detection is platform-dependent (Unix/Linux)

## Future Enhancements

- ANSI color codes for tile values
- In-place screen updates (no clearing)
- Window resize handling
- Multi-platform input support (Windows, macOS)
- Sound effects
