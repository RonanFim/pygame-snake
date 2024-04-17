import pygame
from System.MenuManager import MenuManager
from System.GameManager import GameManager
from System.GameOver import GameOver
from System.ConfigManager import ConfigManager
from System.HighScoreManager import HighScoreManager
from System.Configuration import Configuration
from definitions import Screens, GeneralProp

class Game:

    def __init__(self) -> None:
        # Initialize pygame library
        pygame.init()
        # Initialize font module
        pygame.font.init()
        # Set window caption
        pygame.display.set_caption(GeneralProp.CAPTION)
    
    def Start(self) -> None:
        optSelected = Screens.MENU
        configuration = Configuration()

        while optSelected != Screens.NONE:
            # Menu screen
            menu = MenuManager()
            optSelected = menu.Run()
            del(menu)
            
            if optSelected == Screens.GAME:
                game = GameManager(configuration)
                score = game.Start()
                del(game)
                over = GameOver(score)
                over.Run()
                del(over)
                highScore = HighScoreManager(configuration)
                highScore.SaveScore(score)
                del(highScore)
            elif optSelected == Screens.CONFIG:
                configs = ConfigManager(configuration)
                configuration = configs.Run()
                del(configs)
            elif optSelected == Screens.HIGHSCORE:
                highScore = HighScoreManager(configuration)
                scor = highScore.ReadScore()
                del(highScore)
                print(scor[0])
                print(scor[1])

        # Quit window
        pygame.quit()
        