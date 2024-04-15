import pygame
from System.MenuManager import MenuManager
from System.GameManager import GameManager
from System.GameOver import GameOver
from System.ConfigManager import ConfigManager
from definitions import Screens, GeneralProp
import time

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

        while optSelected != Screens.NONE:
            # Menu screen
            menu = MenuManager()
            optSelected = menu.Run()
            del(menu)
            
            if optSelected == Screens.GAME:
                game = GameManager()
                score = game.Start()
                del(game)
                over = GameOver(score)
                over.Run()
                del(over)
            elif optSelected == Screens.CONFIG:
                configs = ConfigManager()
                configs.Run()

        # Quit window
        pygame.quit()
        