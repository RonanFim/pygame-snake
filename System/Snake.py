from definitions import *
from System.Direction import Direction
import pygame

class Snake():

    def __init__(self) -> None:
        posX = Screen.WIDTH//20 * 10
        posY = Screen.HEIGHT//20 * 10
        self.__snakePos = [(posX + 20, posY), (posX + 10, posY), (posX, posY)]
        self.bodySprite = pygame.Surface((10, 10))
        self.bodySprite.fill(BODYCOLOR)
        self.headSprite = pygame.Surface((10, 10))
        self.headSprite.fill(HEADCOLOR)
    
    def Grow(self, dir):
        self.__snakePos = [self.__snakePos[0]] + self.__snakePos
        self.__snakePos[0] = self.__RefreshPos(self.__snakePos[0], dir)
    
    def RemoveLast(self):
        self.__snakePos.pop()
    
    def IsColliding(self, coordLst: list) -> bool:
        retValue = False
        for coord in coordLst:
            if coord in self.__snakePos:
                retValue = True
        return retValue

    def SelfCollision(self) -> bool:
        return self.__snakePos[0] in self.__snakePos[1:]

    def GetHeadPos(self) -> tuple:
        return self.__snakePos[0]
    
    def GetBodyPos(self) -> list:
        return self.__snakePos[1:]
    
    def __RefreshPos(self, pos, direction):
        if direction == Direction.UP:
            newPos = [pos[0], pos[1] - 10]
            if newPos[1] < 0:
                newPos[1] = Screen.HEIGHT - 10
        elif direction == Direction.DOWN:
            newPos = [pos[0], pos[1] + 10]
            if newPos[1] >= Screen.HEIGHT:
                newPos[1] = 0
        elif direction == Direction.RIGHT:
            newPos = [pos[0] + 10, pos[1]]
            if newPos[0] >= Screen.WIDTH:
                newPos[0] = 0
        elif direction == Direction.LEFT:
            newPos = [pos[0] - 10, pos[1]]
            if newPos[0] < 0:
                newPos[0] = Screen.WIDTH - 10
        else:
            return pos
        # Modified position
        return tuple(newPos)

    def Draw(self, screen: pygame.Surface):
        screen.blit(self.headSprite, self.GetHeadPos())
        for pos in self.GetBodyPos():
            screen.blit(self.bodySprite, pos)