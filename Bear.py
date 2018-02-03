from Animal import Animal

class Bear(Animal):
	def __init__(self, world):
		Animal.__init__(self, world)
		self.wturtle.shape("Bear.gif")
                self.animal = "Bear"

	def breed(self):
		loc = self.breedLocation()
		if loc is None:
			return
		b = Bear(self.world)
		self.world.addThing(b, loc[0], loc[1])

	def liveALittle(self):
                a = [-1, 0, 1]
                b = [-1, 0, 1]
                for i in a:
                        for j in b:
                                if i == j:
                                        continue
                                nx = self.xpos + i
                                ny = self.ypos + j
                                if nx < 0 or nx >= self.world.maxX / 2:
                                        continue
                                if ny < 0 or ny >= self.world.maxY * 2:
                                        continue
                                if self.world.grid[ny][nx] is None:
                                        continue
                                if self.world.grid[ny][nx].animal == "Fish":
                                        self.world.delThing(self.world.grid[ny][nx])
                                        self.energy += 100
                                        if self.energy > Animal.MAX_ENERGY:
                                                self.energy = Animal.MAX_ENERGY
                                        return
                                
                self.update()
