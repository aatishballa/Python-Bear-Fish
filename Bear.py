from Animal import Animal

class Bear(Animal):
	def __init__(self, world):
		Animal.__init__(self, world)
		self.wturtle.shape("Bear.gif")

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

	def appear(self):
		if (self.wturtle.isvisible() != True):  
 			self.wturtle.showturtle()

	def hide(self):
		self.wturtle.hideturtle()  #makes current turtle object invisible

	def breed(self):
		loc = self.breedLocation()
		self.world.grid[loc[0]][loc[1]] = Bear()

	def liveALittle(self):
  		self.update()
