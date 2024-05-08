import pygame
from definitions import HighScoresProp

NEWFONT = "Courier New"
NEWSIZE = 50
ENTERFONT = "Courier New"
ENTERSIZE = 30
NAMEFONT = "Courier New"
NAMESIZE = 30

NEWTXTPOS = (100,20)
ENTERTXTPOS = (20,110)
NAMETXTPOS = (320,110)

class NewHighScore():

    def __init__(self) -> None:
        self.__screen = pygame.display.set_mode((HighScoresProp.SCREENWIDTH, HighScoresProp.SCREENHEIGHT))
        self.__clock = pygame.time.Clock()
        self.__font = pygame.font.SysFont(NEWFONT, NEWSIZE)
        self.__TxtNew = self.__font.render("NEW HIGH SCORE!!", False, HighScoresProp.FONTCOLOR)
        self.__font = pygame.font.SysFont(ENTERFONT, ENTERSIZE)
        self.__TxtEnter = self.__font.render("Enter your name:", False, HighScoresProp.FONTCOLOR)
        self.__font = pygame.font.SysFont(NAMEFONT, NAMESIZE)
        self.__nameStr = ""
    
    def Draw(self):
        self.__screen.fill(HighScoresProp.BGCOLOR)
        self.__screen.blit(self.__TxtNew, NEWTXTPOS)
        self.__screen.blit(self.__TxtEnter, ENTERTXTPOS)
        self.__TxtName = self.__font.render(self.__nameStr, False, HighScoresProp.NAMECOLOR)
        self.__screen.blit(self.__TxtName, NAMETXTPOS)
    
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
                    if event.key == pygame.K_RETURN:
                        return self.__nameStr
                    elif event.key == pygame.K_BACKSPACE:
                        self.__nameStr = self.__nameStr[:-1]
                        self.Draw()
                        pygame.display.update()
                    else:
                        keyCode = event.key
                        if (keyCode >= 32) and (keyCode <= 126):    # printable char
                            if len(self.__nameStr) < HighScoresProp.NAMESIZELIM:
                                self.__nameStr += chr(keyCode).upper()
                                self.Draw()
                                pygame.display.update()
        