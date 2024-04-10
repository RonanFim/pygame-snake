import pygame
from definitions import *

class Score():

    def __init__(self) -> None:
        self.__score = 0
        self.__font = pygame.font.SysFont(SCOREFONT, SCORESIZE)
    
    def GetScore(self) -> int:
        return self.__score
    
    def SetScore(self, num: int) -> bool:
        if num >= 0:
            self.__score = num
            return True
        else:
            return False
    
    def IncrementScore(self):
        self.__score += 1

    def Draw(self, screen: pygame.Surface):
        scoreStr = "Score: " + str(self.__score)
        scoreText = self.__font.render(scoreStr, False, SCORECOLOR)
        screen.blit(scoreText, SCOREPOS)