import pygame
from System.MenuManager import MenuManager
from System.GameManager import GameManager
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
        # Menu screen
        menu = MenuManager()
        optSelected = menu.Run()
        del(menu)
        
        if optSelected == Screens.GAME:
            game = GameManager()
            game.Start()
            del(game)

        # Quit window
        pygame.quit()
        