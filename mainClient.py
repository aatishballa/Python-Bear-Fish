from World import World
from Fish import Fish
from Bear import Bear

import random, turtle
import csv

def onkey():
    print("key pressed")

def mainSimulation():

    
    numberOfBears = 3
    numberOfFish = 10
    worldLifeTime = 10000
    worldWidth = 20
    worldHeight = 10


    
    myworld = World(worldWidth,worldHeight)      
    myworld.draw()

    counterTicks=worldLifeTime

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
    
    csvfile=open('bearFish.txt', 'w')
    column="ticks, num_bears, num_fish \n"
    csvfile.write(column)
	
    for i in range(worldLifeTime):
        counterTicks=i
        myworld.liveALittle()        
        row= str(i) + "," + str(myworld.bearCount)+ "," + str(myworld.fishCount)+"\n"
        csvfile.write(row)

    myworld.freezeWorld()
    

    
mainSimulation()

	
