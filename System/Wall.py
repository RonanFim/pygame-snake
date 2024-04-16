import pygame
from System.Configuration import Configuration
from definitions import *

class Wall():

    def __init__(self, configs: Configuration) -> None:
        self.__screenWidth = configs.width.value
        self.__screenHeight = configs.height.value
        self.__wall = []
        for i in range(0, self.__screenWidth, 10):
            self.__wall.append((i, 0))
            self.__wall.append((i, self.__screenHeight - 10))
        for i in range(0, self.__screenHeight, 10):
            self.__wall.append((0, i))
            self.__wall.append((self.__screenWidth - 10, i))
        self.__OpenWall()
        self.wallSprite = pygame.Surface((10, 10))
        self.wallSprite.fill(WallProp.COLOR)
    
    def __OpenWall(self):
        middleWidth = self.__screenWidth//20 * 10
        middleHeight = self.__screenHeight//20 * 10
        self.__wall.remove((0, middleHeight - 30))
        self.__wall.remove((0, middleHeight - 20))
        self.__wall.remove((0, middleHeight - 10))
        self.__wall.remove((0, middleHeight))
        self.__wall.remove((0, middleHeight + 10))
        self.__wall.remove((0, middleHeight + 20))
        self.__wall.remove((0, middleHeight + 30))
        self.__wall.remove((self.__screenWidth - 10, middleHeight - 30))
        self.__wall.remove((self.__screenWidth - 10, middleHeight - 20))
        self.__wall.remove((self.__screenWidth - 10, middleHeight - 10))
        self.__wall.remove((self.__screenWidth - 10, middleHeight))
        self.__wall.remove((self.__screenWidth - 10, middleHeight + 10))
        self.__wall.remove((self.__screenWidth - 10, middleHeight + 20))
        self.__wall.remove((self.__screenWidth - 10, middleHeight + 30))
        self.__wall.remove((middleWidth - 30, 0))
        self.__wall.remove((middleWidth - 20, 0))
        self.__wall.remove((middleWidth - 10, 0))
        self.__wall.remove((middleWidth, 0))
        self.__wall.remove((middleWidth + 10, 0))
        self.__wall.remove((middleWidth + 20, 0))
        self.__wall.remove((middleWidth + 30, 0))
        self.__wall.remove((middleWidth - 30, self.__screenHeight - 10))
        self.__wall.remove((middleWidth - 20, self.__screenHeight - 10))
        self.__wall.remove((middleWidth - 10, self.__screenHeight - 10))
        self.__wall.remove((middleWidth, self.__screenHeight - 10))
        self.__wall.remove((middleWidth + 10, self.__screenHeight - 10))
        self.__wall.remove((middleWidth + 20, self.__screenHeight - 10))
        self.__wall.remove((middleWidth + 30, self.__screenHeight - 10))
    

    def IsColliding(self, coordLst: list) -> bool:
        retValue = False
        for coord in coordLst:
            if coord in self.__wall:
                retValue = True
        return retValue

    def GetWall(self) -> list:
        return self.__wall

    def Draw(self, screen: pygame.Surface):
        for pos in self.GetWall():
            screen.blit(self.wallSprite, pos)