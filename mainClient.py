def mainSimulation():
    numberOfBears = 10
    numberOfFish = 10
    worldLifeTime = 1000
    worldWidth = 50
    worldHeight = 25
    
    myworld = World(worldWidth,worldHeight)      
    myworld.draw()                               

    for i in range(numberOfFish):  
        newfish = Fish()
        x = random.randrange(myworld.getMaxX())
        y = random.randrange(myworld.getMaxY())
        while not myworld.emptyLocation(x,y):
            x = random.randrange(myworld.getMaxX())
            y = random.randrange(myworld.getMaxY())
        myworld.addThing(newfish,x,y)        

    for i in range(numberOfBears):   
        newbear = Bear()
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

	