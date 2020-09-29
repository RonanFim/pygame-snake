
from System.Game import Game
from definitions import Screen


def main():
    game = Game(Screen.WIDTH, Screen.HEIGHT, Screen.CAPTION)
    game.start()
    return 0


if __name__ == '__main__':
    main()
