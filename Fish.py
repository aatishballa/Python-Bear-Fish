import turtle
class Fish(World):
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.up()
        self.turtle.hideturtle()
        self.turtle.shape("Fish.gif")

        self.xpos = 0
        self.ypos = 0
        self.world = None                 
        
        self.breedTick = 0

    def setX(self,newx):
        # set obj's x position
        self.xpos = newx
        
    
    def setY(self,newy):
        # set obj's y position
        self.ypos = newy
    
    def getX(self):
        # return obj's x position
        return self.xpos
    
    def getY(self):
        # set obj's y position
        return self.ypos
    
    def setWorld(self,aworld):
        # set obj's world reference
        self.world = aworld

    
    def appear(self):
        # send instance turtle to correct coordinates
        # unhide turtle

        #
        

    def hide(self):
        # hide turtle
        self.turtle.hideturtle()  #makes current turtle object invisible

    
    def move(self,newx,newy):
        '''
        ask world's moveThing() to update obj's location in grid to new coordinates
        update Fish object's instance-coordinates
        move object's instance-Turtle to new coordinates'''
        
    def liveALittle(self):
        
        offsetList = [(-1,1) ,(0,1) ,(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]     

        adjfish = 0                                  
        for offset in offsetList:                    
            newx = self.xpos + offset[0]             
            newy = self.ypos + offset[1]
            if 0 <= newx < self.world.getMaxX()  and
               0 <= newy < self.world.getMaxY():          
                if (not self.world.emptyLocation(newx,newy)) and isinstance(self.world.lookAtLocation(newx,newy),Fish):
                    adjfish = adjfish + 1   
         
        if adjfish >= 2:                   
            self.world.delThing(self)      
        else:
            self.breedTick = self.breedTick + 1
            if self.breedTick >= 12:
                self.tryToBreed()

            self.tryToMove()
	
	
	
