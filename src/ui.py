import sys
import termios
import tty


class UI:
    """Handles terminal rendering and user input for the 2048 game."""

    def render(self, board, score, highest_tile):
        """Displays game state with a 4x4 grid, score, and highest tile."""
        grid_str = board.to_string()
        cells = grid_str.split("\n")
        
        print("=" * 29)
        print("|       2048 GAME       |")
        print("=" * 29)
        print()
        
        for row in cells:
            print("|", end="")
            values = row.split()
            for i in range(4):
                value = values[i] if i < len(values) else "0"
                if value == "0" or value == ".":
                    print("    -    ", end="")
                else:
                    print(f" {int(value):^7} ", end="")
                if i < 3:
                    print("|", end="")
            print("|")
            print()
        
        print("=" * 29)
        print(f"| Score: {score:<15} |")
        print(f"| Highest Tile: {highest_tile:<8} |")
        print("=" * 29)
        print()
        print("Use arrow keys to move. Press 'q' to quit.")
        print()

    def get_user_input(self):
        """Reads arrow key input or quit command."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            
            if ch == '\x1b':
                ch = sys.stdin.read(2)
                if ch == '[A':
                    return 'up'
                elif ch == '[B':
                    return 'down'
                elif ch == '[C':
                    return 'right'
                elif ch == '[D':
                    return 'left'
            elif ch == 'q' or ch == 'Q':
                return 'quit'
            elif ord(ch) == 3:
                return 'quit'
            
            return None
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    def show_game_over(self, score, highest_tile):
        """Displays final score and highest tile reached."""
        print()
        print("=" * 29)
        print("|       GAME OVER!      |")
        print("=" * 29)
        print()
        print(f"Final Score: {score}")
        print(f"Highest Tile: {highest_tile}")
        print()
        print("Thanks for playing 2048!")
        print()

    def show_invalid_move(self):
        """Indicates an invalid move was attempted."""
        print()
        print("Invalid move! Try a different direction.")
        print()
