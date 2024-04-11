import pygame
from definitions import *

class Wall():

    def __init__(self) -> None:
        self.__wall = []
        for i in range(0, GameProp.SCREENWIDTH, 10):
            self.__wall.append((i, 0))
            self.__wall.append((i, GameProp.SCREENHEIGHT - 10))
        for i in range(0, GameProp.SCREENHEIGHT, 10):
            self.__wall.append((0, i))
            self.__wall.append((GameProp.SCREENWIDTH - 10, i))
        self.__OpenWall()
        self.wallSprite = pygame.Surface((10, 10))
        self.wallSprite.fill(WallProp.COLOR)
    
    def __OpenWall(self):
        middleWidth = GameProp.SCREENWIDTH//20 * 10
        middleHeight = GameProp.SCREENHEIGHT//20 * 10
        self.__wall.remove((0, middleHeight - 30))
        self.__wall.remove((0, middleHeight - 20))
        self.__wall.remove((0, middleHeight - 10))
        self.__wall.remove((0, middleHeight))
        self.__wall.remove((0, middleHeight + 10))
        self.__wall.remove((0, middleHeight + 20))
        self.__wall.remove((0, middleHeight + 30))
        self.__wall.remove((GameProp.SCREENWIDTH - 10, middleHeight - 30))
        self.__wall.remove((GameProp.SCREENWIDTH - 10, middleHeight - 20))
        self.__wall.remove((GameProp.SCREENWIDTH - 10, middleHeight - 10))
        self.__wall.remove((GameProp.SCREENWIDTH - 10, middleHeight))
        self.__wall.remove((GameProp.SCREENWIDTH - 10, middleHeight + 10))
        self.__wall.remove((GameProp.SCREENWIDTH - 10, middleHeight + 20))
        self.__wall.remove((GameProp.SCREENWIDTH - 10, middleHeight + 30))
        self.__wall.remove((middleWidth - 30, 0))
        self.__wall.remove((middleWidth - 20, 0))
        self.__wall.remove((middleWidth - 10, 0))
        self.__wall.remove((middleWidth, 0))
        self.__wall.remove((middleWidth + 10, 0))
        self.__wall.remove((middleWidth + 20, 0))
        self.__wall.remove((middleWidth + 30, 0))
        self.__wall.remove((middleWidth - 30, GameProp.SCREENHEIGHT - 10))
        self.__wall.remove((middleWidth - 20, GameProp.SCREENHEIGHT - 10))
        self.__wall.remove((middleWidth - 10, GameProp.SCREENHEIGHT - 10))
        self.__wall.remove((middleWidth, GameProp.SCREENHEIGHT - 10))
        self.__wall.remove((middleWidth + 10, GameProp.SCREENHEIGHT - 10))
        self.__wall.remove((middleWidth + 20, GameProp.SCREENHEIGHT - 10))
        self.__wall.remove((middleWidth + 30, GameProp.SCREENHEIGHT - 10))
    

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