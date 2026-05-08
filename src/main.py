from src.game import Game
from src.ui import UI


def main():
    """Main entry point for the 2048 game."""
    ui = UI()
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
