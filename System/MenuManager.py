import pygame
from definitions import MenuProp, Screens

MENUFONT = "Courier New"
MENUSIZE = 40
STARTPOSX = 150
STARTPOSY = 200

class MenuManager:

    def __init__(self) -> None:
        self.__options = ["START", "CONFIGURATION", "HIGHSCORE", "EXIT"]
        self.__optionsPos = [(STARTPOSX,STARTPOSY),
                             (STARTPOSX-105,STARTPOSY+60),
                             (STARTPOSX-50,STARTPOSY+120),
                             (STARTPOSX+10,STARTPOSY+180)]
        self.__font = pygame.font.SysFont(MENUFONT, MENUSIZE)
        self.__option = 0
        self.__screen = pygame.display.set_mode((MenuProp.SCREENWIDTH, MenuProp.SCREENHEIGHT))
        self.__clock = pygame.time.Clock()
        self.__logo = pygame.image.load("Assets\\Logo.png").convert()
    
    def Draw(self):
        self.__texts = [self.__font.render(op, False, MenuProp.FONTCOLOR) for op in self.__options]
        self.__texts[self.__option] = self.__font.render(self.__options[self.__option], False, MenuProp.SELECTCOLOR)
        for idx, txt in enumerate(self.__texts):
            self.__screen.blit(txt, self.__optionsPos[idx])
        self.__screen.blit(self.__logo, (50,40))
    
    def Run(self):
        while 42:
            self.__clock.tick(10)   # 10 fps

            for event in pygame.event.get():
                # The close button was clicked?
                if event.type == pygame.QUIT:
                    return Screens.NONE
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_RETURN):  # ENTER key
                        if self.__option == 0:
                            return Screens.GAME
                        elif self.__option == 1:
                            return Screens.CONFIG
                        elif self.__option == 2:
                            return Screens.HIGHSCORE
                        else:
                            return Screens.NONE
                    elif (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
                        if self.__option < (len(self.__options) - 1):
                            self.__option += 1
                    elif (event.key == pygame.K_UP) or (event.key == pygame.K_w):
                        if self.__option > 0:
                            self.__option -= 1
            
            self.Draw()
            pygame.display.update()
                       