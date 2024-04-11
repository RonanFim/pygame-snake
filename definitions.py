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
    SCREENWIDTH = 600
    SCREENHEIGHT = 400
    BGCOLOR = (0, 0, 0)

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
