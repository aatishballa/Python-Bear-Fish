import turtle, random
class World():
	grid = []
	def __init__(self,mx,my):
		self.maxX=mx
		self.maxY=my
		self.thingList=[]
		
		for arow in range(self.maxY):
			row=[]
			for acol in range(self.maxY):
				row.append(None)
			self.grid.append(row)
			
		self.wturtle = turtle.Turtle()
		self.wturtle.hideturtle()		
		self.wscreen = turtle.Screen()
		self.wscreen.onkey(lambda: self.increaseSpeed(), "Up")
		self.wscreen.onkey(lambda: self.decreaseSpeed(), "Down")
		self.simspeed = 1
		self.wscreen.listen()
		self.wscreen.setworldcoordinates(0,0,self.maxX-1, self.maxY-1)
		self.wscreen.addshape("Bear.gif") 
		self.wscreen.addshape("Fish.gif")
		
	def increaseSpeed(self):
		self.simspeed += 10
		for i in self.thingList:
			i.simulationSpeed += 10

	def decreaseSpeed(self):
		self.simspeed -= 10
		if self.simspeed < 1:
			self.simspeed = 1
			return

		for i in self.thingList:
			i.simulationSpeed -= 10

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
		athing.setWorld(self)
		self.thingList.append(athing)
		athing.appear()
		
	def delThing(self,athing):
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
		if y >= len(self.grid) or x >= len(self.grid[0]) or y < 0 or x < 0: 
			return False
		if self.grid[y][x] == None:
			return True
		else:
			return False
	
	def lookAtLocation(self, x, y):
		return self.grid[y][x]
			
			
#testing	
def main():
    worldWidth = 50
    worldHeight = 25
    myworld = World(worldWidth,worldHeight)      
    myworld.draw()
    return myworld

#main()
                          
