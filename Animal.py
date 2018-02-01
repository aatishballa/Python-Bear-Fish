TICK_UPDATE = 100

class Animal:
	def __init__(self, world):
		self.world = world
		self.wturtle = turtle.Turtle()
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
	
	def update(self):
		self.tick += simulationSpeed
		if self.tick >= TICK_UPDATE:
			self.breedtick += 1
			if(self.breedtick >= self.breedRate):
				pass #breed

			self.tick = 0
			
