import turtle, random

TICK_UPDATE = 100
BREED_UPDATE = 100

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
		self.breedRate = 1
		self.xpos = 0
		self.ypos = 0

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
	
	def move(self):
		a = [-1, 0, 1]
		b = [-1, 0, 1]
		random.shuffle(a)
		random.shuffle(b)
		for i in a:
			for j in b:
				if self.world.emptyLocation(self.xpos + i, self.ypos + j):
					self.world.moveThing(self, self.xpos + i, self.ypos + j)
					return

	def update(self):
		self.wturtle.goto(self.ypos, self.xpos)
		self.tick += self.simulationSpeed
		if self.tick >= TICK_UPDATE:
			self.breedtick += self.breedRate
			if(self.breedtick >= BREED_UPDATE):
				self.breed()

			self.tick = 0
		
			self.move()
