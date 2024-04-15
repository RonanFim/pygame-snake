import pygame
from definitions import ConfigProp
from System.Configuration import Configuration

CONFIGFONT = "Courier New"
CONFIGSIZE = 35
STARTPOSX = 50
STARTPOSY = 50

class ConfigManager():

    def __init__(self) -> None:
        self.__configuration = Configuration()
        self.__current = 0
        self.__configs = ["Speed", "Width", "Height", "Wall Style", "EXIT"]
        self.__configPos = [(STARTPOSX,STARTPOSY),
                            (STARTPOSX,STARTPOSY+60),
                            (STARTPOSX,STARTPOSY+120),
                            (STARTPOSX,STARTPOSY+180),
                            (STARTPOSX+150,STARTPOSY+265)] 
        self.__options = [self.__configuration.speed,
                          self.__configuration.width,
                          self.__configuration.height,
                          self.__configuration.wall]
        self.__optionsPos = [(x+250,y) for (x,y) in self.__configPos]
        self.__font = pygame.font.SysFont(CONFIGFONT, CONFIGSIZE)
        self.__screen = pygame.display.set_mode((ConfigProp.SCREENWIDTH, ConfigProp.SCREENHEIGHT))
        self.__clock = pygame.time.Clock()


    def Draw(self):
        self.__screen.fill(ConfigProp.BGCOLOR)
        for idx in range(len(self.__configs) - 1):
            color = ConfigProp.SELFONTCOLOR if (idx == self.__current) else ConfigProp.CONFFONTCOLOR
            confTxt = self.__font.render(self.__configs[idx], False, color)
            optTxt = self.__font.render(self.__options[idx].name, False, ConfigProp.OPTFONTCOLOR)
            self.__screen.blit(confTxt, self.__configPos[idx])
            self.__screen.blit(optTxt, self.__optionsPos[idx])
        color = ConfigProp.SELFONTCOLOR if (self.__current == len(self.__configs)-1) else ConfigProp.CONFFONTCOLOR
        exitTxt = self.__font.render(self.__configs[-1], False, color)
        self.__screen.blit(exitTxt, self.__configPos[-1])
    
    def Run(self):
        while 42:
            self.__clock.tick(10)   # 10 fps

            for event in pygame.event.get():
                # The close button was clicked?
                if event.type == pygame.QUIT:
                    return
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_RETURN):  # ENTER key
                        if (self.__current >= (len(self.__configs) - 1)):
                            self.__configuration.speed = self.__options[0]
                            self.__configuration.width = self.__options[1]
                            self.__configuration.height = self.__options[2]
                            self.__configuration.wall = self.__options[3]
                            return self.__configuration
                    elif (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
                        if self.__current < (len(self.__configs) - 1):
                            self.__current += 1
                    elif (event.key == pygame.K_UP) or (event.key == pygame.K_w):
                        if self.__current > 0:
                            self.__current -= 1
                    elif (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                        self.__options[self.__current] = self.__configuration.GetNextValue(self.__options[self.__current])
                    elif (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                        self.__options[self.__current] = self.__configuration.GetPreviousValue(self.__options[self.__current])
            
            self.Draw()
            pygame.display.update()
