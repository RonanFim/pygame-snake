from enum import Enum

class Configuration():
    
    class Speed(Enum):
        SLOW = 0,
        NORMAL = 1,
        FAST = 2
    
    class ScreenSize(Enum):
        px200 = 200,
        px300 = 300,
        px400 = 400,
        px500 = 500,
        px600 = 600,
        px700 = 700,
        px800 = 800
    
    class WallStyle(Enum):
        NONE = 0,
        OPEN = 1,
        SOLID = 2
    
    def __init__(self) -> None:
        self.speed = self.Speed.NORMAL
        self.width = self.ScreenSize.px600
        self.height = self.ScreenSize.px400
        self.wall = self.WallStyle.OPEN
    
    def GetNextValue(self, obj):
        objLst = list(obj.__class__)
        idx = objLst.index(obj)
        if idx >= (len(objLst) - 1):
            return obj
        else:
            return objLst[idx+1]

    def GetPreviousValue(self, obj):
        objLst = list(obj.__class__)
        idx = objLst.index(obj)
        if idx <= 0:
            return obj
        else:
            return objLst[idx-1]