class BaseButton(object):
    def __init__(self, x, y, w, h, background_color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.background_color = background_color

    def display():
        fill(self.background_color)
        noStroke()
        rect(self.x, self.y, self.w, self.h)
    
    def isHovering():
        return mouseX >= self.x and mouseX < self.x + self.w and mouseY >= self.y and mouseY < self.y + self.h
    
    def getX():
        return self.x
    
    def getY():
        return self.y
    
    def getW():
        return self.w
    
    def getH():
        return self.h
    
    def getBGColor():
        return self.background_color
