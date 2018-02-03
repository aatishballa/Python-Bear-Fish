from Animal import Animal

class Bear(Animal):
	def __init__(self, world):
		Animal.__init__(self, world)
		self.wturtle.shape("Bear.gif")

	def breed(self):
		loc = self.breedLocation()
		if loc is None:
			return
		b = Bear(self.world)
		self.world.addThing(b, loc[0], loc[1])

	def liveALittle(self):
  		self.update()
		#todo: maybe hunt fish
