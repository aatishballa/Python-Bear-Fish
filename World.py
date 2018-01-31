class World():

	def __init__(self,mx,my):
		self.maxX=mx
		self.maxY=my
		self.thingList=[]
		self.grid=[]
		
		for arow in range(self.maxY):
			row=[]
			for acol in range(self.maxY):
				row.append(None)
			self.grid.append(row)
			
			
		self.wturtle=turtle.Turtle()
		self.wscreen = turtle.Screen()
		self.wscreen.setworldcoordinates(0,0,self.maxX-1,self.maxY-1)
		self.wscreen.addshape("Bear.gif")
		self.wscreen.addshape("Fish.gif")
		self.wturtle.hideturtle()
		
	def draw(self):
		self.wscreen.tracer(0)
		self.wturtle.forward(self.maxX-1)
		self.wturtle.left(90)
		self.wturtle.forward(self.maxY-1)
		self.wturtle.left(90)
		self.wturtle.forward(self.maxX-1)
		self.wturtle.left(90)
		self.wturtle.forward(self.maxY-1)
		self.wturtle.left(90)
		
		for i in range(self.maxY-1):
			self.wturtle.forward(self.maxX-1)
			self.wturtle.backward(self.maxX-1)
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
		self.grid[(aThing.getY()][aThing.getX()]=None
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
			
			
		
	
	