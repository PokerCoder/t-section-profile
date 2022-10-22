class Profile:

    def __init__(self, a, b, c, d, y=0):

        self.a = a / 1000
        self.b = b / 1000
        self.c = c / 1000
        self.d = d / 1000
        self.y = y / 1000

    def upperArea(self):

        if self.y <= self.d:
            return self.a * self.c
        else:
            return self.a * (self.c + self.d - self.y)

    def lowerArea(self):

        if self.y <= self.d:
            return self.b * (self.d - self.y)
        else:
            return 0

    def totalArea(self):

        return self.lowerArea() + self.upperArea()

    def lowerCenter(self):

        if self.y <= self.d:
            return (self.d + self.y) / 2
        else:
            return 0

    def upperCenter(self):

        if self.y <= self.d:
            return self.d + self.c / 2
        else:
            return (self.d + self.c + self.y) / 2

    def totalCenter(self):
        
        if self.y == self.c + self.d:
            
            return self.y

        la = self.lowerArea()
        ua = self.upperArea()
        lc = self.lowerCenter()
        uc = self.upperCenter()

        return (ua * uc + la * lc) / (la + ua)
    
    def crop(self, length):
        
        self.y = length
    
    # TODO: change this function!
    
    def getT(self):
        
        if self.y <= self.d:
            
            return 15
        
        else:
            
            return 300
        
    def getResult(self):
        
        return (self.totalArea() * self.totalCenter() * 80) / (0.000156 * self.getT())