import pygame
from definitions import ConfigProp

CONFIGFONT = "Courier New"
CONFIGSIZE = 35
STARTPOSX = 50
STARTPOSY = 50

class ConfigManager():

    def __init__(self) -> None:
        speed = ["SLOW", "NORMAL", "FAST"]
        width = [str(num) for num in range(200,900,100)]
        height = [str(num) for num in range(200,900,100)]
        wall = ["NONE", "OPEN", "SOLID"]
        self.__selected = [1, 4, 2, 1]
        self.__current = 0
        self.__configs = ["Speed", "Width", "Height", "Wall Style", "EXIT"]
        self.__configPos = [(STARTPOSX,STARTPOSY),
                            (STARTPOSX,STARTPOSY+60),
                            (STARTPOSX,STARTPOSY+120),
                            (STARTPOSX,STARTPOSY+180),
                            (STARTPOSX+150,STARTPOSY+265)]
        self.__options = [speed, width, height, wall]
        self.__optionsPos = [(x+250,y) for (x,y) in self.__configPos]
        self.__font = pygame.font.SysFont(CONFIGFONT, CONFIGSIZE)
        self.__screen = pygame.display.set_mode((ConfigProp.SCREENWIDTH, ConfigProp.SCREENHEIGHT))
        self.__clock = pygame.time.Clock()


    def Draw(self):
        self.__screen.fill(ConfigProp.BGCOLOR)
        for idx, value in enumerate(self.__selected):
            color = ConfigProp.SELFONTCOLOR if (idx == self.__current) else ConfigProp.CONFFONTCOLOR
            confTxt = self.__font.render(self.__configs[idx], False, color)
            optTxt = self.__font.render(self.__options[idx][value], False, ConfigProp.OPTFONTCOLOR)
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
                            return
                    elif (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
                        if self.__current < (len(self.__configs) - 1):
                            self.__current += 1
                    elif (event.key == pygame.K_UP) or (event.key == pygame.K_w):
                        if self.__current > 0:
                            self.__current -= 1
                    elif (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                        curr = self.__selected[self.__current]
                        if (curr < (len(self.__options[self.__current]) - 1)):
                            self.__selected[self.__current] += 1
                    elif (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                        curr = self.__selected[self.__current]
                        if (curr > 0):
                            self.__selected[self.__current] -= 1
            
            self.Draw()
            pygame.display.update()
