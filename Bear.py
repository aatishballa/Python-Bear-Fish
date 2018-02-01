from Animal import Animal

class Bear(Animal):
	def __init__(self, world):
		Animal.__init__(self, world)
		self.wturtle.shape("Bear.gif")

	def appear(self):
		if (self.wturtle.isvisible() != True):  
 			self.wturtle.showturtle()

	def hide(self):
		self.wturtle.hideturtle()  #makes current turtle object invisible

	def breed(self):
		loc = self.breedLocation()
		if loc is None:
			return
		b = Bear(self.world)
		self.world.addThing(b, loc[0], loc[1])

	def liveALittle(self):
  		self.update()
		#todo: maybe hunt fish
