import turtle, random

class Animal:
        TICK_UPDATE = 100
        BREED_UPDATE = 1000
        MAX_ENERGY = 200
        MIN_ENERGY_TO_BREED = 10
        MIN_ENERGY_TO_MOVE = 1

        def __init__(self, world):
                self.world = world
                self.wturtle = turtle.Turtle()
                self.wturtle.up()
                self.wturtle.hideturtle()
                self.living = True
                self.simulationSpeed = 1 
                self.tick = 0
                self.breedtick = random.random() * self.BREED_UPDATE 
                self.breedRate = 1
                self.xpos = 0
                self.ypos = 0
                self.energy = self.MAX_ENERGY
                self.animal = ""

        def liveALittle(self):
                pass
        
        def breed(self):
                pass

        def appear(self):
                if (self.wturtle.isvisible() != True):  
                        self.wturtle.showturtle()

        def hide(self):
                self.wturtle.hideturtle()  #makes current turtle object invisible


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
                                if i == j:
                                        continue
                                if self.world.emptyLocation(self.xpos + i, self.ypos + j):
                                        self.world.moveThing(self, self.xpos + i, self.ypos + j)
                                        return
                                
        def die(self):
                self.world.delThing(self)
                                
        def update(self):
                if self.energy <= 0:
                        self.die()
                        return
                        
                self.wturtle.goto(self.ypos, self.xpos)
                self.tick += self.simulationSpeed
                if self.tick >= self.TICK_UPDATE:
                        self.breedtick += self.breedRate
                        if(self.breedtick >= self.BREED_UPDATE and self.energy >= self.MIN_ENERGY_TO_BREED):
                                self.energy -= self.MIN_ENERGY_TO_BREED
                                self.breed()

                        self.tick = 0
                        self.move()
                        self.energy -= self.MIN_ENERGY_TO_MOVE
