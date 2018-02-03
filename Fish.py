from Animal import Animal

class Fish(Animal):
    def __init__(self, world):
        Animal.__init__(self, world)
        self.wturtle.shape("Fish.gif")
        self.breedRate = 33
        self.animal = "Fish"

    def breed(self):
        loc = self.breedLocation()
        if loc is None:
             return
        b = Fish(self.world)
        self.world.addThing(b, loc[0], loc[1])
	
    def liveALittle(self):
        self.update()
