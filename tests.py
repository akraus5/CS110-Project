import spaceship, obstacle, resup
import pygame

def getPos(myThing): # possibly add this to each class
    '''
        Gets x and y cooridnate of an object
        args: myThing: an object (spaceship, obstacle, resup)
        return: tuple (X coordinate,Y coordinate)
    '''
    return (myThing.getX(),myThing.getY())

def testMinMax(myThing):
    '''
        Used to get minimum and maximum X and Y coordinates of a moving object
        args: myThing: an object (spaceship, obstacle, resup)
        return: None
    '''
    clock = pygame.time.Clock()

    maxX = myThing.getX()
    minX = myThing.getX()
    maxY = myThing.getY()
    minY = myThing.getY()

    stop = False
    while(stop != True):
        clock.tick(60)
        myThing.update()
        #note that this also tests change_dir() in both obstacle and resup
        pos = getPos(myThing)

        if myThing.getX() > maxX:
            maxX = myThing.getX()
        if myThing.getX() < minX:
            minX = myThing.getX()
        if myThing.getY() > maxY:
            maxY = myThing.getY()
        if myThing.getY() < minY:
            minY = myThing.getY()

        #print(pos)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if(event.key==pygame.K_q):
                    stop = True
    print("Min X: ", minX)
    print("Max X: ", maxX)
    print("Min Y: ", minY)
    print("Max Y: ", maxY)

def main():
    '''
        Testing all methods of spaceship, obstacle, and resup
        args: None
        return: None
    '''
    # Initializing pygame:
    pygame.init()
    pygame.key.set_repeat(1,50)
    clock = pygame.time.Clock()
    width = 500
    height = 700

    print("########## Testing spaceship model ##########")

    # Initialize our spaceship:
    ship = spaceship.SpaceShip(width,height)
    startPos = getPos(ship)

    print("Start position: ",startPos)
    print("========== Testing Spaceship Update ==========")
    print("~~~~~~~~~~ Press q to continue ~~~~~~~~~~")

    stop = False
    while(stop != True):
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if(event.key==pygame.K_q):
                        stop = True
        ship.update()
        pos = getPos(ship)
        print(pos)

    print("========== Testing Spaceship Lucid & Update ==========")
    print("~~~~~~~~~~ Press q to continue ~~~~~~~~~~")

    ship.change_lucid(False)

    stop = False
    while(stop != True):
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if(event.key==pygame.K_q):
                        stop = True
        ship.update()
        pos = getPos(ship)
        print(pos)

    print("========== Testing spaceship speed ==========")
    print("~~~~~~~~~~ Press q to continue ~~~~~~~~~~")

    sp = int(input("Input speed: "))
    lu = input("Input lucid (True/False): ")

    ship = spaceship.SpaceShip(width,height,lu,sp)
    startPos = getPos(ship)

    print("Start position: ",startPos)

    stop = False
    while(stop != True):
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if(event.key==pygame.K_q):
                        stop = True
        ship.update()
        pos = getPos(ship)
        print(pos)

    print("########## Testing obstacle model ##########")
    print("~~~~~~~~~~ Press q to continue ~~~~~~~~~~")

    xdirection = input("Input x direction (left,right): ")
    ydirection = input("Input y direction (up,down): ")
    speed = int(input("Input speed: "))

    obst = obstacle.Obstacle(width/2,height/2,width,height,xdirection,ydirection,speed)
    startPos = getPos(obst)
    print("Start position: ",startPos)

    testMinMax(obst)

    print("========== Testing obstacle setx and sety ==========")

    obst = obstacle.Obstacle(width/2,height/2,width,height)
    print("Position: ", getPos(obst))

    newx = int(input("Input new x: "))
    newy = int(input("Input new y: "))

    obst.setX(newx)
    obst.setY(newy)

    print("New Position: ", getPos(obst))

    print("########## Testing resup model ##########")
    print("========== Testing stationary resup ==========")
    print("~~~~~~~~~~ Press q to continue ~~~~~~~~~~")

    station = resup.Resup(width/2,height/2,width,height)
    testMinMax(station)

    print("========== Testing moving resup ==========")
    print("~~~~~~~~~~ Press q to continue ~~~~~~~~~~")

    direction = input("Input direction (left/right): ")
    speed = int(input("Input speed: "))

    station = resup.Resup(width/2,height/2,width,height,'moon',True,direction,speed)
    testMinMax(station)

main()
