import pygame
from definitions import *

class Wall():

    def __init__(self) -> None:
        self.__wall = []
        for i in range(0, Screen.WIDTH, 10):
            self.__wall.append((i, 0))
            self.__wall.append((i, Screen.HEIGHT - 10))
        for i in range(0, Screen.HEIGHT, 10):
            self.__wall.append((0, i))
            self.__wall.append((Screen.WIDTH - 10, i))
        self.__OpenWall()
        self.wallSprite = pygame.Surface((10, 10))
        self.wallSprite.fill(WALLCOLOR)
    
    def __OpenWall(self):
        middleWidth = Screen.WIDTH//20 * 10
        middleHeight = Screen.HEIGHT//20 * 10
        self.__wall.remove((0, middleHeight - 30))
        self.__wall.remove((0, middleHeight - 20))
        self.__wall.remove((0, middleHeight - 10))
        self.__wall.remove((0, middleHeight))
        self.__wall.remove((0, middleHeight + 10))
        self.__wall.remove((0, middleHeight + 20))
        self.__wall.remove((0, middleHeight + 30))
        self.__wall.remove((Screen.WIDTH - 10, middleHeight - 30))
        self.__wall.remove((Screen.WIDTH - 10, middleHeight - 20))
        self.__wall.remove((Screen.WIDTH - 10, middleHeight - 10))
        self.__wall.remove((Screen.WIDTH - 10, middleHeight))
        self.__wall.remove((Screen.WIDTH - 10, middleHeight + 10))
        self.__wall.remove((Screen.WIDTH - 10, middleHeight + 20))
        self.__wall.remove((Screen.WIDTH - 10, middleHeight + 30))
        self.__wall.remove((middleWidth - 30, 0))
        self.__wall.remove((middleWidth - 20, 0))
        self.__wall.remove((middleWidth - 10, 0))
        self.__wall.remove((middleWidth, 0))
        self.__wall.remove((middleWidth + 10, 0))
        self.__wall.remove((middleWidth + 20, 0))
        self.__wall.remove((middleWidth + 30, 0))
        self.__wall.remove((middleWidth - 30, Screen.HEIGHT - 10))
        self.__wall.remove((middleWidth - 20, Screen.HEIGHT - 10))
        self.__wall.remove((middleWidth - 10, Screen.HEIGHT - 10))
        self.__wall.remove((middleWidth, Screen.HEIGHT - 10))
        self.__wall.remove((middleWidth + 10, Screen.HEIGHT - 10))
        self.__wall.remove((middleWidth + 20, Screen.HEIGHT - 10))
        self.__wall.remove((middleWidth + 30, Screen.HEIGHT - 10))
    

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