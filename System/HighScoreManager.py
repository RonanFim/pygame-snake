import pygame
import shelve
from datetime import datetime
from System.Configuration import Configuration
from definitions import HighScoresProp

class HighScoreManager():

    def __init__(self, configs: Configuration) -> None:
        self.__conf = configs
        self.__params = self.__conf.height.name + self.__conf.width.name + self.__conf.wall.name + self.__conf.speed.name

    def SaveScore(self, score):
        scoreFile = shelve.open(HighScoresProp.HIGHSCOREFILE)
        date = datetime.today()
        scoreFile[self.__params] = [(score, "Ronan", date),(score, "Paula", date)]
        scoreFile.close()
    
    def ReadScore(self):
        scoreFile = shelve.open(HighScoresProp.HIGHSCOREFILE)
        score = scoreFile[self.__params]
        scoreFile.close()
        return score