import random


class Game:
    """Manages the game loop, input handling, and state persistence."""

    def __init__(self):
        """Initialize game with board and track running state."""
        from src.board import Board
        self._board = Board()
        self._running = True
        self._last_move_had_empty = False

    def start(self):
        """Start the game loop, handling input until game over."""
        from src.ui import UI
        ui = UI()

        while self._running:
            # Display current state
            ui.render(
                self._board,
                self._board.get_score(),
                self._board.get_highest_tile()
            )

            # Get user input
            key = ui.get_user_input()

            # Handle input
            if key == 'quit':
                self._running = False
            elif key in ('up', 'down', 'left', 'right'):
                changed = self._board.move(key)
                if changed:
                    self._add_random_tile()
                    if self._board.is_game_over():
                        ui.render(
                            self._board,
                            self._board.get_score(),
                            self._board.get_highest_tile()
                        )
                        ui.show_game_over(
                            self._board.get_score(),
                            self._board.get_highest_tile()
                        )
                        self._running = False
                else:
                    ui.show_invalid_move()

    def _add_random_tile(self):
        """Add a random 2 or 4 tile to an empty cell."""
        empty = self._board._get_empty_cells()
        if empty:
            row, col = random.choice(empty)
            value = 2 if random.random() < 0.9 else 4
            self._board.grid[row][col] = value

    def get_status(self):
        """Return current game status dict."""
        return {
            'score': self._board.get_score(),
            'highest_tile': self._board.get_highest_tile(),
            'running': self._running
        }

    def is_running(self):
        """Return True if game is still active."""
        return self._running
