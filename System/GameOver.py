import pygame
from definitions import GameOverProp

GAMEOVERFONT = "Courier New"
GAMEOVERSIZE = 60
SCOREFONT = "Courier New"
SCORESIZE = 40
PRESSFONT = "Courier New"
PRESSSIZE = 20

GAMETXTPOS = (120,90)
OVERTXTPOS = (120,150)
SCORETXTPOS = (90,300)
PRESSTXTPOS = (40,400)

class GameOver():

    def __init__(self, score: int) -> None:
        self.__screen = pygame.display.set_mode((GameOverProp.SCREENWIDTH, GameOverProp.SCREENHEIGHT))
        self.__clock = pygame.time.Clock()
        self.__font = pygame.font.SysFont(GAMEOVERFONT, GAMEOVERSIZE)
        self.__TxtGame = self.__font.render("GAME", False, GameOverProp.FONTCOLOR)
        self.__TxtOver = self.__font.render("OVER", False, GameOverProp.FONTCOLOR)
        scoreStr = "Score: " + str(score)
        self.__font = pygame.font.SysFont(SCOREFONT, SCORESIZE)
        self.__TxtScore = self.__font.render(scoreStr, False, GameOverProp.FONTCOLOR)
        self.__font = pygame.font.SysFont(PRESSFONT, PRESSSIZE)
        self.__TxtPress = self.__font.render("Press any key to continue...", False, GameOverProp.FONTCOLOR)
    
    def Draw(self):
        self.__screen.blit(self.__TxtGame, GAMETXTPOS)
        self.__screen.blit(self.__TxtOver, OVERTXTPOS)
        self.__screen.blit(self.__TxtScore, SCORETXTPOS)
        self.__screen.blit(self.__TxtPress, PRESSTXTPOS)
    
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
        