import turtle

TICK_UPDATE = 100

class Animal:
	def __init__(self, world):
		self.world = world
		self.wturtle = turtle.Turtle()
		self.wturtle.up()
		self.wturtle.hideturtle()
		self.living = True
		self.simulationSpeed = 1 
		self.tick = 0
		self.breedtick = 0
		self.breedRate = 10

	def liveALittle(self):
		pass

	def breed(self):
		pass

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

	def breedLocation(self):
		for i in range(self.world.maxX):
			for j in range(self.world.maxY):
				if self.world.emptyLocation(i, j):
					return (i, j)	
	
	def update(self):
		self.tick += simulationSpeed
		if self.tick >= TICK_UPDATE:
			self.breedtick += 1
			if(self.breedtick >= self.breedRate):
				self.breed()

			self.tick = 0
			
