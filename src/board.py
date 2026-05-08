import random


class Board:
    def __init__(self):
        self.grid = [[0] * 4 for _ in range(4)]
        self.score = 0
        self._highest_tile = 0
        self._init_tiles()

    def _init_tiles(self):
        empty = self._get_empty_cells()
        for _ in range(2):
            if empty:
                row, col = empty.pop(random.randint(0, len(empty) - 1))
                self.grid[row][col] = 2
                if self._highest_tile < 2:
                    self._highest_tile = 2

    def clone(self):
        new_board = Board.__new__(Board)
        new_board.grid = [row[:] for row in self.grid]
        new_board.score = self.score
        new_board._highest_tile = self._highest_tile
        return new_board

    def _get_empty_cells(self):
        return [(r, c) for r in range(4) for c in range(4) if self.grid[r][c] == 0]

    def move(self, direction):
        if direction == "left":
            return self._move_left()
        elif direction == "right":
            return self._move_right()
        elif direction == "up":
            return self._move_up()
        elif direction == "down":
            return self._move_down()
        return False

    def _move_left(self):
        changed = False
        for row in range(4):
            line = [self.grid[row][c] for c in range(4) if self.grid[row][c] != 0]
            merged = []
            i = 0
            while i < len(line):
                if i + 1 < len(line) and line[i] == line[i + 1]:
                    new_val = line[i] * 2
                    merged.append(new_val)
                    self.score += new_val
                    if new_val > self._highest_tile:
                        self._highest_tile = new_val
                    i += 2
                else:
                    merged.append(line[i])
                    i += 1
            merged.extend([0] * (4 - len(merged)))
            for col in range(4):
                if self.grid[row][col] != merged[col]:
                    changed = True
                self.grid[row][col] = merged[col]
        return changed

    def _move_right(self):
        changed = False
        for row in range(4):
            line = [self.grid[row][c] for c in range(4) if self.grid[row][c] != 0]
            merged = []
            i = len(line) - 1
            while i >= 0:
                if i - 1 >= 0 and line[i] == line[i - 1]:
                    new_val = line[i] * 2
                    merged.insert(0, new_val)
                    self.score += new_val
                    if new_val > self._highest_tile:
                        self._highest_tile = new_val
                    i -= 2
                else:
                    merged.insert(0, line[i])
                    i -= 1
            merged = [0] * (4 - len(merged)) + merged
            for col in range(4):
                if self.grid[row][col] != merged[col]:
                    changed = True
                self.grid[row][col] = merged[col]
        return changed

    def _move_up(self):
        changed = False
        for col in range(4):
            line = [self.grid[r][col] for r in range(4) if self.grid[r][col] != 0]
            merged = []
            i = 0
            while i < len(line):
                if i + 1 < len(line) and line[i] == line[i + 1]:
                    new_val = line[i] * 2
                    merged.append(new_val)
                    self.score += new_val
                    i += 2
                else:
                    merged.append(line[i])
                    i += 1
            merged.extend([0] * (4 - len(merged)))
            for row in range(4):
                if self.grid[row][col] != merged[row]:
                    changed = True
                self.grid[row][col] = merged[row]
        return changed

    def _move_down(self):
        changed = False
        for col in range(4):
            line = [self.grid[r][col] for r in range(4) if self.grid[r][col] != 0]
            merged = []
            i = len(line) - 1
            while i >= 0:
                if i - 1 >= 0 and line[i] == line[i - 1]:
                    new_val = line[i] * 2
                    merged.insert(0, new_val)
                    self.score += new_val
                    i -= 2
                else:
                    merged.insert(0, line[i])
                    i -= 1
            merged = [0] * (4 - len(merged)) + merged
            for row in range(4):
                if self.grid[row][col] != merged[row]:
                    changed = True
                self.grid[row][col] = merged[row]
        return changed

    def get_score(self):
        return self.score

    def get_highest_tile(self):
        return max(max(row) for row in self.grid)

    def is_game_over(self):
        if self._get_empty_cells():
            return False
        for row in range(4):
            for col in range(4):
                val = self.grid[row][col]
                if col < 3 and val == self.grid[row][col + 1]:
                    return False
                if row < 3 and val == self.grid[row + 1][col]:
                    return False
        return True

    def to_string(self):
        return "\n".join(
            " ".join(str(c) if c != 0 else "0" for c in row)
            for row in self.grid
        )
