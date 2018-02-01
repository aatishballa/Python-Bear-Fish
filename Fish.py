from Bear import Bear 
class Fish(Bear):
    def __init__(self, world):
        Bear.__init__(self, world)
        self.wturtle.shape("Fish.gif")

    def breed(self):
        loc = self.breedLocation()
        if loc is None:
             return
        b = Fish(self.world)
        self.world.addThing(b, loc[0], loc[1])
	
