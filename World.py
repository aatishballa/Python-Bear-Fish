import turtle
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
		self.wscreen.setworldcoordinates(0,0,self.maxX-1, self.maxY-1)
		self.wscreen.addshape("Bear.gif") 
		self.wscreen.addshape("Fish.gif")
		
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

		self.wscreen.tracer(1)
			
	def freezeWorld(self):
		self.wscreen.exitonclick()
	
	def addThing(self, athing, x, y):
		athing.setX(x)
		aThing.setY(y)
		self.grid[y][x] = athing
		aThing.setWorld(self)
		self.thingList.append(aThing)
		aThing.appear()
		
	def delThing(self,athing):
		aThing.hide()
		self.grid[aThing.getY()][aThing.getX()]=None
		self.thingList.remove(aThing)
	
	def moveThing(self, oldx, oldy, newx, newy):
		self.grid[newy][newx] = self.grid[oldy][oldx]
		self.grid[oldy][oldx] = self.grid [oldy] [oldx]
		self.grid [oldy][oldx]= None
	
	def getMaxX(self):
		return self.max;
		
	
	def getMaxY(self):
		return self.maxY
		
	def liveALittle(self):
		if self.thingList !=[]:
			aThing= random.randrange(len(self.thingList))
			randomthing = self.thingList[aThing]
			randomthing.liveALittle()
	
	def emptyLocation(self,x,y):
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

main()
                          
