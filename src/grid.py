class Grid:
    """Manages a 4x4 grid for the 2048 game."""

    def __init__(self):
        """Creates empty 4x4 grid (all zeros)."""
        self._grid = [[0] * 4 for _ in range(4)]

    def clone(self):
        """Returns deep copy of grid state."""
        new_grid = Grid()
        new_grid._grid = [row[:] for row in self._grid]
        return new_grid

    def is_empty(self, row, col):
        """Returns True if cell is empty (value is 0)."""
        return self._grid[row][col] == 0

    def set_cell(self, row, col, value):
        """Places tile at position (0 <= row, col <= 3)."""
        self._grid[row][col] = value

    def get_cell(self, row, col):
        """Returns tile value at position."""
        return self._grid[row][col]

    def get_empty_cells(self):
        """Returns list of (row, col) tuples for empty cells."""
        return [(row, col) for row in range(4) for col in range(4) if self._grid[row][col] == 0]

    def to_string(self):
        """Returns string representation for debugging."""
        return "\n".join(" ".join(str(cell) for cell in row) for row in self._grid)
