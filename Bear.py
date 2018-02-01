from World import World
class Bear(World):
    
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

    def appear(self):
        if (self.turtle.isVisible != True):  
            self.turtle.showturtle()  #makes current turtle object visible       

    def hide(self):
        self.turtle.hideturtle()  #makes current turtle object invisible

    def move(self,newx,newy):
        return
    
