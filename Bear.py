class Bear:
    
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.up()
        self.turtle.hideturtle()
        self.turtle.shape("Bear.gif")

        self.xpos = 0
        self.ypos = 0
        self.world = None                 
        
        self.breedTick = 0

    def setX(self,newx):
        self.xpos = newx
        
    
    def setY(self,newy):
        self.ypos = newy
    
    def getX(self):
        return self.xpos
    
    def getY(self):
        return self.ypos
    
    def setWorld(self,aworld):
        self.world = aworld

    def move(self,newx,newy):
        return

    def hide(self):
        return
