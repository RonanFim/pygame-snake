from enum import Enum

class GeneralProp():
    CAPTION = 'Snake'

class Screens(Enum):
    NONE = 0,
    MENU = 1,
    CONFIG = 2,
    HIGHSCORE = 3,
    GAME = 4

class GameProp():
    BGCOLOR = (0, 0, 0)
    FPS = 30

class SnakeProp():
    BODYCOLOR = (0, 153, 0)
    HEADCOLOR = (255, 255, 255)

class AppleProp():
    COLOR = (255, 0, 0)

class WallProp():
    COLOR = (120, 120, 120)

class ScoreProp():
    COLOR = (255, 255, 255)
    FONT = "Courier New"
    SIZE = 15
    POSITION = (20, 20)

class MenuProp():
    FONTCOLOR = (255, 255, 255)
    SELECTCOLOR = (0, 255, 0)
    SCREENWIDTH = 400
    SCREENHEIGHT = 500

class GameOverProp():
    FONTCOLOR = (255, 255, 255)
    SCREENWIDTH = 400
    SCREENHEIGHT = 500

class ConfigProp():
    BGCOLOR = (0, 0, 0)
    CONFFONTCOLOR = (255, 255, 255)
    OPTFONTCOLOR = (0, 0, 255)
    SELFONTCOLOR = (0, 255, 0)
    SCREENWIDTH = 480
    SCREENHEIGHT = 400
