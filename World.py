import turtle, random, sys

class World():
        def __init__(self,mx,my):
                self.grid = []
                self.maxX = mx
                self.maxY = my
                self.thingList = []

                self.bearBreedRate = 1
                self.fishBreedRate = 20
                self.bearCount = 0
                self.fishCount = 0

                for arow in range(self.maxY * 2):
                        row=[]
                        for acol in range(self.maxX):
                                row.append(None)

                        self.grid.append(row)
			
                self.wturtle = turtle.Turtle()
                self.wturtle.hideturtle()		
                self.wscreen = turtle.Screen()

                self.wscreen.onkey(lambda: self.term(), "t")
                self.wscreen.onkey(lambda: self.increaseSpeed(), "Up")
                self.wscreen.onkey(lambda: self.decreaseSpeed(), "Down")
                self.wscreen.onkey(lambda: self.incBreed(), "z")
                self.wscreen.onkey(lambda: self.decBreed(), "x")
                self.wscreen.onkey(lambda: self.incBearBreed(), "a")
                self.wscreen.onkey(lambda: self.decBearBreed(), "s")
                self.wscreen.onkey(lambda: self.incFishBreed(), "q")
                self.wscreen.onkey(lambda: self.decFishBreed(), "w")
                
                
                self.simspeed = 1
                self.setTitle()
                self.wscreen.listen()
                self.wscreen.setworldcoordinates(0,0,self.maxX - 1, self.maxY - 1)
                self.wscreen.addshape("Bear.gif") 
                self.wscreen.addshape("Fish.gif")

        def term(self):
                self.wscreen.bye()
                sys.exit()
                
        def setTitle(self):
                pre = "Python-Turtle-Bear Simulation | Simspeed: "
                self.wscreen.title(pre + str(self.simspeed * 100) + '%')
                
        def increaseSpeed(self):
                self.simspeed += 10
                for i in self.thingList:
                        i.simulationSpeed += 10

                self.setTitle()

        def decreaseSpeed(self):
       	        self.simspeed -= 10
                if self.simspeed < 1:
                        self.simspeed = 1
                        return

                for i in self.thingList:
                        i.simulationSpeed -= 10

                self.setTitle()

        def setBreed(self):
                for i in self.thingList:
                        if i is None:
                                continue
                        if i.animal == "Fish":
                                i.breedRate = self.fishBreedRate
                        else:
                                i.breedRate = self.bearBreedRate

        def incFishBreed(self):
                self.fishBreedRate += 1
                self.setBreed()
                
        def incBearBreed(self):
                self.bearBreedRate += 1
                self.setBreed()
                
        def decFishBreed(self):
                self.fishBreedRate -= 1
                self.setBreed()
                
        def decBearBreed(self):
                self.bearBreedRate -= 1
                self.setBreed()
                
        def incBreed(self):
                self.fishBreedRate += 1
                self.bearBreedRate += 1
                self.setBreed()

        def decBreed(self):
                self.fishBreedRate -= 1
                self.bearBreedRate -= 1
                self.setBreed()
                
        def draw(self):
       	        #world box drawn
                self.wscreen.tracer(0)
                self.wturtle.forward(self.maxX-1)
                self.wturtle.left(90)
                self.wturtle.forward(self.maxY-1)
                self.wturtle.left(90)
                self.wturtle.forward(self.maxX-1)
                self.wturtle.left(90)
                self.wturtle.forward(self.maxY-1)
                self.wturtle.left(90)
		
                cellWidth = 1
                cellHeight = 1

                #horizontal lines
                for i in range(self.maxY-1):
                        self.wturtle.forward(self.maxX-1)
                        self.wturtle.backward(self.maxX-1)
                        self.wturtle.left(90)
                        self.wturtle.forward(1)
                        self.wturtle.right(90)
	                
                self.wturtle.forward(1)
                self.wturtle.right(90)	
                for i in range(self.maxX - 2):
                        self.wturtle.forward(self.maxY-1)
                        self.wturtle.backward(self.maxY-1)
                        self.wturtle.left(90)
                        self.wturtle.forward(1)
                        self.wturtle.right(90)	

                self.wscreen.tracer(1, 0)
		
        def freezeWorld(self):
                self.wscreen.exitonclick()
	        
        def addThing(self, athing, x, y):
                athing.setX(x)
                athing.setY(y)
                self.grid[y][x] = athing
                athing.simulationSpeed = self.simspeed
                if athing.animal == "Fish":
                        self.fishCount += 1
                        athing.breedrate = self.fishBreedRate
                else:
                        self.bearCount += 1
                        athing.breedrate = self.bearBreedRate
                        
                athing.setWorld(self)
                self.thingList.append(athing)
                athing.appear()
		
        def delThing(self,athing):
                if(athing.animal == "Fish"):
                        self.fishCount -= 1
                else:
                        self.bearCount -= 1
                        
                athing.hide()
                self.grid[athing.getY()][athing.getX()]=None
                self.thingList.remove(athing)
	        
        def moveThing(self, thing, newx, newy):
                oldx = thing.xpos
                oldy = thing.ypos
                thing.xpos = newx
                thing.ypos = newy
                self.grid[newy][newx] = self.grid[oldy][oldx]
                self.grid[oldy][oldx] = None
	        
        def getMaxX(self):
                return self.maxX
        
        def getMaxY(self):
                return self.maxY

        def liveALittle(self):
                if self.thingList !=[]:
                        aThing= random.randrange(len(self.thingList))
                        randomthing = self.thingList[aThing]
                        randomthing.liveALittle()
	                
        def emptyLocation(self,x,y):
                if y >= self.maxY * 2 or x >= self.maxX / 2 or y < 0 or x < 0: 
                        return False
                
                if self.grid[y][x] == None:
                        return True
       	        else:
                        return False
	        
        def lookAtLocation(self, x, y):
                return self.grid[y][x]
	
			
#testing	
def main():
        worldWidth = 10
        worldHeight = 10
        myworld = World(worldWidth,worldHeight)      
        myworld.draw()
        return myworld

#main()
                          
