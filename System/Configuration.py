from enum import IntEnum

class Configuration():
    
    class Speed(IntEnum):   # frames by step
        SLOW = 4,
        NORMAL = 3,
        FAST = 2
    
    class ScreenSize(IntEnum):
        px200 = 200,
        px300 = 300,
        px400 = 400,
        px500 = 500,
        px600 = 600,
        px700 = 700,
        px800 = 800
    
    class WallStyle(IntEnum):
        NONE = 0,
        OPEN = 1,
        SOLID = 2
    
    def __init__(self) -> None:
        self.speed = self.Speed.NORMAL
        self.width = self.ScreenSize.px600
        self.height = self.ScreenSize.px400
        self.wall = self.WallStyle.OPEN
    
    def GetNextValue(self, obj):
        objClass = obj.__class__
        objLst = list(objClass)
        idx = objLst.index(obj)
        if idx >= (len(objLst) - 1):
            return obj
        else:
            return objLst[idx+1]

    def GetPreviousValue(self, obj):
        objClass = obj.__class__
        objLst = list(objClass)
        idx = objLst.index(obj)
        if idx <= 0:
            return obj
        else:
            return objLst[idx-1]