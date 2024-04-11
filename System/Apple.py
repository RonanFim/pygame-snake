from definitions import *
import pygame

class Apple():

    def __init__(self) -> None:
        self.appleSprite = pygame.Surface((10, 10))
        self.appleSprite.fill(AppleProp.COLOR)
        self.__applePos = (0, 0)
    
    def GetApplePos(self) -> tuple:
        return self.__applePos
    
    def SetApplePos(self, newPos: tuple) -> None:
        self.__applePos = newPos
    
    def Draw(self, screen: pygame.Surface):
        screen.blit(self.appleSprite, self.__applePos)