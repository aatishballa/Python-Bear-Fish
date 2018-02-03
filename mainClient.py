from World import World
from Fish import Fish
from Bear import Bear
import random, turtle

def onkey():
    print("key pressed")

def mainSimulation():
    numberOfBears = 2
    numberOfFish = 10
    worldLifeTime = 100000000
    worldWidth = 20
    worldHeight = 10
    
    myworld = World(worldWidth,worldHeight)      
    myworld.draw()                               

    for i in range(numberOfFish):  
        newfish = Fish(myworld)
        x = random.randrange(myworld.getMaxX())
        y = random.randrange(myworld.getMaxY())

        while not myworld.emptyLocation(x,y):
            x = random.randrange(myworld.getMaxX())
            y = random.randrange(myworld.getMaxY())
        myworld.addThing(newfish,x,y)        

    for i in range(numberOfBears):   
        newbear = Bear(myworld)
        x = random.randrange(myworld.getMaxX())
        y = random.randrange(myworld.getMaxY())

        while not myworld.emptyLocation(x,y):   
            x = random.randrange(myworld.getMaxX())
            y = random.randrange(myworld.getMaxY())
        myworld.addThing(newbear,x,y)     
    
    for i in range(worldLifeTime):     
        myworld.liveALittle()          
    
    myworld.freezeWorld() 
         
mainSimulation()

	
