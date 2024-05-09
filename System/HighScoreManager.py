import pygame
import shelve
from datetime import datetime
from System.Configuration import Configuration
from System.NewHighScore import NewHighScore
from definitions import HighScoresProp

class HighScoreManager():

    def __init__(self, configs: Configuration) -> None:
        self.__conf = configs
        self.__params = self.__conf.height.name + self.__conf.width.name + self.__conf.wall.name + self.__conf.speed.name

    def SaveScore(self, score):
        scoreFile = shelve.open(HighScoresProp.HIGHSCOREFILE)
        try:
            oldScore = scoreFile[self.__params]["score"]
        except KeyError:
            oldScore = 0
        if score > oldScore:
            newHS = NewHighScore()
            name = newHS.Run()
            date = datetime.today()
            # scoreFile[self.__params] = (score, name, date)
            scoreFile[self.__params] = {"score": score, "name": name, "date": date}
        scoreFile.close()
    
    def ReadScore(self):
        scoreFile = shelve.open(HighScoresProp.HIGHSCOREFILE)
        try:
            score = scoreFile[self.__params]
        except KeyError:
            score = {"score": 0, "name": "", "date": ""}
        scoreFile.close()
        return score