import pygame
import random as r
import time

pygame.init()
clock = pygame.time.Clock()

#Set screen size and creates it
screenSize = 600
win = pygame.display.set_mode((screenSize,screenSize))

pygame.display.set_caption("Snake!")

#Size of Snake
square = 20

xHead = (screenSize - square)/2
yHead = (screenSize - square)/2

xSnake = [xHead]
ySnake = [yHead]

turned = 0 

xVel = 0
yVel = 25


FoodPickedUp = False
FoodPickedUp2 = False
 


#Sets location for foodpellot
def CreateFoodPellet():
    global foodX
    foodX = r.randrange(0, screenSize, square)
    global foodY
    foodY = r.randrange(0, screenSize, square)

#GG Mate Lol
def Ded():
    #Set for GG
    font = pygame.font.Font('freesansbold.ttf', 32) 
    x = str(len(xSnake))
    words = ('Game Over --' + " Score: " + x)
    text = font.render(words, True, (0,0,0), (255,0,0)) 
    textRect = text.get_rect()  
    textRect.center = (screenSize // 2, screenSize // 2)
    
    win.fill((255,0,0))
    win.blit(text, textRect) 
    pygame.display.update()  
    global run

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

time.sleep(3)

CreateFoodPellet()

run = True
while run:

    #Delay
    pygame.time.delay(100)


    #Event Kill 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Get Key
    keys = pygame.key.get_pressed()
    #Arrow Keys control head
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and turned == 0:
        if yVel != 25:
            yVel = -25
            xVel = 0
            turned = 1
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and turned == 0:
        if yVel != -25:    
            yVel = 25
            xVel = 0
            turned = 1

    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and turned == 0:
        if xVel != 25:
            xVel = -25
            yVel = 0
            turned = 1
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and turned == 0:
       if xVel != -25:
            xVel = 25
            yVel = 0
            turned = 1

    #Food pickup manual
    if keys[pygame.K_f]:
        FoodPickedUp = True
    
    #Set background
    win.fill((0,0,0))

    #Crash into Wall
    for m in range(len(xSnake)):
        if ((xSnake[m] <= -15 or screenSize + 15 <= xSnake[m] + square)):
            Ded()
    for m in range(len(ySnake)):
        if ((ySnake[m] <= -15 or screenSize +15 <= ySnake[m] + square)):
            Ded()

    #Crash into Self
    for a in range(len(xSnake)):
        for b in range(len(xSnake)):
            if a != b:
                if (xSnake[a] == xSnake[b]):
                    if (ySnake[a] == ySnake[b]):
                        Ded()

    #Pick up food pellet 
    for b in range(len(xSnake)):
        if ((xSnake[b] <= foodX <= xSnake[b] + square) or (xSnake[b] <= foodX + square <= xSnake[b] + square)):
            if ((ySnake[b] <= foodY <= ySnake[b] + square) or (ySnake[b] <= foodY + square <= ySnake[b] + square)):
                FoodPickedUp = True


    #First half of food pickup to save last body position
    if FoodPickedUp == True:
        xSet = xSnake[-1]
        ySet = ySnake[-1]
        FoodPickedUp2 = True
        FoodPickedUp = False

    #Move Body
    i = len(xSnake)
    while i > 0:
        if i-1 > 0:
            xSnake[i-1] = xSnake[i-2]
            ySnake[i-1] = ySnake[i-2] 
            pygame.draw.rect(win, (0,0,255), (xSnake[i-1],ySnake[i-1],square,square), 0)
        i-=1

    #Second Half of Food Pick up to set last square back
    if FoodPickedUp2 == True:
        xSnake.append(xSet)
        ySnake.append(ySet)
        pygame.draw.rect(win, (0,0,255), (xSnake[-1],ySnake[-1],square,square), 0)
        CreateFoodPellet()
        FoodPickedUp2 = False
        
    #Move Head
    xSnake[0] += xVel
    ySnake[0] += yVel
    pygame.draw.rect(win, (0,0,255), (xSnake[0],ySnake[0],square,square), 0)

    pygame.draw.rect(win, (255,0,0), (foodX,foodY,square,square), 0)
    
    #Reset Turn Lock
    turned = 0

    #Refresh
    pygame.display.update()