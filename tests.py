import spaceship, obstacle, resup
import pygame

def getPos(mything): # possibly add this to each class
    return (mything.getX(),mything.getY())

def main():
    # Initializing pygame:
    pygame.init()
    pygame.key.set_repeat(1,500)

    print("########## Testing spaceship model ##########")

    # Initialize our spaceship:
    ship = spaceship.SpaceShip(500,1000)
    startPos = getPos(ship)

    print("Start position: ",startPos)

    print("========== Standard Input Test ==========")

    ship.move(pygame.K_UP)
    pos = getPos(ship)
    print("UP:", pos)

    ship.move(pygame.K_DOWN)
    pos = getPos(ship)
    print("DOWN:", pos)

    ship.move(pygame.K_LEFT)
    pos = getPos(ship)
    print("LEFT:", pos)

    ship.move(pygame.K_RIGHT)
    pos = getPos(ship)
    print("RIGHT:", pos)

    print("========== User Input Test ==========")
    print("~~~~~~~~~~ Press q to continue ~~~~~~~~~~")

    stop = False
    while(stop != True):
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    ship.move(event.key)
                    pos = getPos(ship)
                    print(pos)
                    if(event.key==pygame.K_q):
                        stop = True

    print("########## Testing obstacle model ##########")
    print("~~~~~~~~~~ Press q to continue ~~~~~~~~~~")

    direction = input("Type direction (up,down,left,right): ")

    obst = obstacle.Obstacle(400,500,5000,10000, direction)
    startPos = getPos(obst)
    print("Start position: ",startPos)

    maxX = obst.getX()
    minX = obst.getX()
    maxY = obst.getY()
    minY = obst.getY()

    stop = False
    while(stop != True):
        obst.move()
        obst.change_dir()
        pos = getPos(obst)

        if obst.getX() > maxX:
            maxX = obst.getX()
        if obst.getX() < minX:
            minX = obst.getX()
        if obst.getY() > maxY:
            maxY = obst.getY()
        if obst.getY() < minY:
            minY = obst.getY()

        #print(pos)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if(event.key==pygame.K_q):
                    stop = True
    print("Min X: ", minX)
    print("Max X: ", maxX)
    print("Min Y: ", minY)
    print("Max Y: ", maxY)
    '''
    print("########## Testing y obstacle model ##########")
    print("~~~~~~~~~~ Press q to continue ~~~~~~~~~~")

    obst = obstacle.Obstacle(400,500,5000,10000,'down')
    startPos = getPos(obst)
    print("Start position: ",startPos)

    maxY = obst.getY()
    minY = obst.getY()

    stop = False
    while(stop != True):
        #for event in pygame.event.get():
        obst.move()
        obst.change_dir()
        pos = getPos(obst)
        #print(pos)

        if obst.getY() > maxY:
            maxY = obst.getY()
        if obst.getY() < minY:
            minY = obst.getY()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if(event.key==pygame.K_q):
                    stop = True

    print("Min Y: ", minY)
    print("Max Y: ", maxY)
    '''

    print("########## Testing resup model ##########")

    station = resup.Resup(50,50)
    print(getPos(station))

########################################################

    print("######### Changing Speed Testing ########")

    print("########## Testing spaceship model ##########")
    print("~~~~~~~~~~ Press q to continue ~~~~~~~~~~")

    sp = int(input("Input speed test: "))

    ship = spaceship.SpaceShip(500,1000,sp)
    startPos = getPos(ship)

    print("Start position: ",startPos)

    print("========== Standard Input Test ==========")

    ship.move(pygame.K_UP)
    pos = getPos(ship)
    print("UP:", pos)

    ship.move(pygame.K_DOWN)
    pos = getPos(ship)
    print("DOWN:", pos)

    ship.move(pygame.K_LEFT)
    pos = getPos(ship)
    print("LEFT:", pos)

    ship.move(pygame.K_RIGHT)
    pos = getPos(ship)
    print("RIGHT:", pos)

    print("========== User Input Test ==========")
    print("~~~~~~~~~~ Press q to continue ~~~~~~~~~~")

    stop = False
    while(stop != True):
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    ship.move(event.key)
                    pos = getPos(ship)
                    print(pos)
                    if(event.key==pygame.K_q):
                        stop = True

    print("########## Testing obstacle model ##########")
    print("~~~~~~~~~~ Press q to continue ~~~~~~~~~~")

    direction = input("Type direction (up,down,left,right): ")
    sp = int(input("Input speed test: "))

    obst = obstacle.Obstacle(400,500,5000,10000,direction,sp)
    startPos = getPos(obst)
    print("Start position: ",startPos)

    maxX = obst.getX()
    minX = obst.getX()
    maxY = obst.getY()
    minY = obst.getY()

    stop = False
    while(stop != True):
        #for event in pygame.event.get():
        obst.move()
        obst.change_dir()
        pos = getPos(obst)

        if obst.getX() > maxX:
            maxX = obst.getX()
        if obst.getX() < minX:
            minX = obst.getX()
        if obst.getY() > maxY:
            maxY = obst.getY()
        if obst.getY() < minY:
            minY = obst.getY()

        #print(pos)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if(event.key==pygame.K_q):
                    stop = True
    print("Min X: ", minX)
    print("Max X: ", maxX)
    print("Min Y: ", minY)
    print("Max Y: ", maxY)
    '''
    print("########## Testing y obstacle model ##########")
    print("~~~~~~~~~~ Press q to continue ~~~~~~~~~~")

    sp = int(input("Input speed test: "))

    obst = obstacle.Obstacle(400,500,5000,10000,'down',sp)
    startPos = getPos(obst)
    print("Start position: ",startPos)

    maxY = obst.getY()
    minY = obst.getY()

    stop = False
    while(stop != True):
        obst.move()
        obst.change_dir()
        pos = getPos(obst)
        #print(pos)

        if obst.getY() > maxY:
            maxY = obst.getY()
        if obst.getY() < minY:
            minY = obst.getY()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if(event.key==pygame.K_q):
                    stop = True

    print("Min Y: ", minY)
    print("Max Y: ", maxY)
    '''
main()
