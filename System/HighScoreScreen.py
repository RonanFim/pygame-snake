import pygame
from System.Configuration import Configuration
from System.HighScoreManager import HighScoreManager
from definitions import HighScoresProp


TXTSIZEPOS = (10,10)
VALUESIZEPOS = (80,10)
TXTSPEEDPOS = (10,32)
VALUESPEEDPOS = (82,32)
TXTSTYLEPOS = (11,54)
VALUESTYLEPOS = (82,54)

SCOREPOSY = 120
NAMEPOSY = 300
DATEPOS = (70,380)

class HighScoreScreen():

    def __init__(self, config: Configuration) -> None:
        self.__screen = pygame.display.set_mode((HighScoresProp.ReadScreen.SCREENWIDTH, HighScoresProp.ReadScreen.SCREENHEIGHT))
        self.__clock = pygame.time.Clock()
        self.__font = pygame.font.SysFont(HighScoresProp.ReadScreen.CONFIGFONT, HighScoresProp.ReadScreen.CONFIGSIZE)
        self.__TxtSize = self.__font.render("Size:", False, HighScoresProp.ReadScreen.CONFIGNAMECOLOR)
        sizeValue = str(config.width.value) + "x" + str(config.height.value)
        self.__ValueSize = self.__font.render(sizeValue, False, HighScoresProp.ReadScreen.CONFIGVALUECOLOR)
        self.__TxtSpeed = self.__font.render("Speed:", False, HighScoresProp.ReadScreen.CONFIGNAMECOLOR)
        self.__ValueSpeed = self.__font.render(config.speed.name, False, HighScoresProp.ReadScreen.CONFIGVALUECOLOR)
        self.__TxtStyle = self.__font.render("Wall:", False, HighScoresProp.ReadScreen.CONFIGNAMECOLOR)
        self.__ValueStyle = self.__font.render(config.wall.name, False, HighScoresProp.ReadScreen.CONFIGVALUECOLOR)

        HSManager = HighScoreManager(config)
        highScore = HSManager.ReadScore()
        self.__font = pygame.font.SysFont(HighScoresProp.ReadScreen.SCOREFONT, HighScoresProp.ReadScreen.SCORESIZE)
        scoreStr = str(highScore["score"])
        self.__ValueScore = self.__font.render(scoreStr, False, HighScoresProp.ReadScreen.SCORECOLOR)
        self.__font = pygame.font.SysFont(HighScoresProp.ReadScreen.NAMEFONT, HighScoresProp.ReadScreen.NAMESIZE)
        self.__Name = self.__font.render(highScore["name"], False, HighScoresProp.ReadScreen.NAMECOLOR)
        self.__font = pygame.font.SysFont(HighScoresProp.ReadScreen.DATEFONT, HighScoresProp.ReadScreen.DATESIZE)
        self.__Date = self.__font.render(str(highScore["date"])[:16], False, HighScoresProp.ReadScreen.DATECOLOR)
        self.__scorePosX = 210 - 42*len(scoreStr)
        self.__namePosX = 210 - 15*len(highScore["name"])

    
    def Draw(self):
        self.__screen.fill(HighScoresProp.ReadScreen.BGCOLOR)
        self.__screen.blit(self.__TxtSize, TXTSIZEPOS)
        self.__screen.blit(self.__ValueSize, VALUESIZEPOS)
        self.__screen.blit(self.__TxtSpeed, TXTSPEEDPOS)
        self.__screen.blit(self.__ValueSpeed, VALUESPEEDPOS)
        self.__screen.blit(self.__TxtStyle, TXTSTYLEPOS)
        self.__screen.blit(self.__ValueStyle, VALUESTYLEPOS)
        self.__screen.blit(self.__ValueScore, (self.__scorePosX, SCOREPOSY))
        self.__screen.blit(self.__Name, (self.__namePosX, NAMEPOSY))
        self.__screen.blit(self.__Date, DATEPOS)

    
    def Run(self):
        self.Draw()
        pygame.display.update()

        while 42:
            self.__clock.tick(10)   # 10 fps

            for event in pygame.event.get():
                # The close button was clicked?
                if event.type == pygame.QUIT:
                    pygame.quit()
                if (event.type == pygame.KEYDOWN):
                    return
        