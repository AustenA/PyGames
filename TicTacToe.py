import pygame
pygame.init()

screenHeight = 500
screenWidth = 500

turn = -1

o = [0,0,0,
     0,0,0,
     0,0,0]

x = [0,0,0,
     0,0,0,
     0,0,0]

win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Tic Tac Toe")

running = True

def checkO():
    
    #Check Blue Rows
    for x in [0,3,6]:  
        if o[x] == 1 and o[x + 1] == 1 and o[x + 2] == 1:
            blueWin()
    for x in [0,1,2]:
        if o[x] == 1 and o[x + 3] == 1 and o[x + 6] == 1:
            blueWin()
    if o[0] == 1 and o[4] == 1 and o[8] == 1:
        blueWin()
    if o[2] == 1 and o[4] == 1 and o[6] == 1:
        blueWin()

def checkX():

    #Check Yellow Rows
    for o in [0,3,6]:  
        if x[o] == 1 and x[o + 1] == 1 and x[o + 2] == 1:
            yellowWin()
    for o in [0,1,2]:
        if x[o] == 1 and x[o + 3] == 1 and x[o + 6] == 1:
            yellowWin()
    if x[0] == 1 and x[4] == 1 and x[8] == 1:
        yellowWin()
    if x[2] == 1 and x[4] == 1 and x[6] == 1:
        yellowWin()

def blueWin():
    print("Blue O Wins")
    exit()

def yellowWin():
    print("Yellow O Wins")
    exit()

pygame.display.update()

while running:
    pygame.time.delay(60)
    checkO()
    checkX()

    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:

            if turn == -1:
                if pos[0] <= 170:
                    if pos[1] <= 170:
                        #print("Top Left")
                        if o[0] == 1 or x[0] == 1:
                            continue
                        x[0] = 1
                    if pos[1] >= 330:
                        #print("Bottom Left")
                        if o[6] == 1 or x[6] == 1:
                            continue
                        x[6] = 1
                    if pos[1] >= 170 and pos[1] <= 330:
                        #print("Mid Left")
                        if o[3] == 1 or x[3] == 1:
                            continue
                        x[3] = 1

                if pos[0] >= 330:
                    if pos[1] <= 170:
                        #print("Top Right")
                        if o[2] == 1 or x[2] == 1:
                            continue
                        x[2] = 1
                    if pos[1] >= 330:
                        #print("Bottom Right")
                        if o[8] == 1 or x[8] == 1:
                            continue
                        x[8] = 1
                    if pos[1] >= 170 and pos[1] <= 330:
                        #print("Mid Right")
                        if o[5] == 1 or x[5] == 1:
                            continue
                        x[5] = 1

                if pos[0] > 170 and pos[0] < 330:
                    if pos[1] <= 170:
                        #print("Top Mid")
                        if o[1] == 1 or x[1] == 1:
                            continue
                        x[1] = 1
                    if pos[1] >= 330:
                        #print("Bottom Mid")
                        if o[7] == 1 or x[7] == 1:
                            continue
                        x[7] = 1
                    if pos[1] >= 170 and pos[1] <= 330:
                        #print("Mid Mid")
                        if o[4] == 1 or x[4] == 1:
                            continue
                        x[4] = 1

            if turn == 1:
                if pos[0] <= 170:
                    if pos[1] <= 170:
                        #print("Top Left")
                        if x[0] == 1 or o[0] == 1:
                            continue
                        o[0] = 1
                    if pos[1] >= 330:
                        #print("Bottom Left")
                        if x[6] == 1 or o[6] == 1:
                            continue
                        o[6] = 1
                    if pos[1] >= 170 and pos[1] <= 330:
                        #print("Mid Left")
                        if x[3] == 1 or o[3] == 1:
                            continue
                        o[3] = 1

                if pos[0] >= 330:
                    if pos[1] <= 170:
                        #print("Top Right")
                        if x[2] == 1 or o[2] == 1:
                            continue
                        o[2] = 1
                    if pos[1] >= 330:
                        #print("Bottom Right")
                        if x[8] == 1 or o[8] == 1:
                            continue
                        o[8] = 1
                    if pos[1] >= 170 and pos[1] <= 330:
                        #print("Mid Right")
                        if x[5] == 1 or o[5] == 1:
                            continue
                        o[5] = 1

                if pos[0] > 170 and pos[0] < 330:
                    if pos[1] <= 170:
                        #print("Top Mid")
                        if x[1] == 1 or o[1] == 1:
                            continue
                        o[1] = 1
                    if pos[1] >= 330:
                        #print("Bottom Mid")
                        if x[7] == 1 or o[7] == 1:
                            continue
                        o[7] = 1
                    if pos[1] >= 170 and pos[1] <= 330:
                        #print("Mid Mid")
                        if x[4] == 1 or o[4] == 1:
                            continue
                        o[4] = 1

            turn = turn * -1



    win.fill((0,0,0))

    
    
    pygame.draw.line(win, (255,255,255), (170,50), (170,450), 8)
    pygame.draw.line(win, (255,255,255), (330,50), (330,450), 8)
    pygame.draw.line(win, (255,255,255), (60,170), (440,170), 8)
    pygame.draw.line(win, (255,255,255), (60,330), (440,330), 8)


    if o[0] == 1:
        pygame.draw.circle(win, (0,0,255), (105,105), 50, 4)
    if o[1] == 1:
       pygame.draw.circle(win, (0,0,255), (250,100), 50, 4)
    if o[2] == 1:
       pygame.draw.circle(win, (0,0,255), (400,100), 50, 4)
    if o[3] == 1:
       pygame.draw.circle(win, (0,0,255), (105,250), 50, 4)
    if o[4] == 1:
       pygame.draw.circle(win, (0,0,255), (255,245), 50, 4)
    if o[5] == 1:
       pygame.draw.circle(win, (0,0,255), (400,250), 50, 4)
    if o[6] == 1:
       pygame.draw.circle(win, (0,0,255), (105,395), 50, 4)
    if o[7] == 1:
       pygame.draw.circle(win, (0,0,255), (250,395), 50, 4)
    if o[8] == 1:
       pygame.draw.circle(win, (0,0,255), (400,395), 50, 4)

    if x[0] == 1:
        pygame.draw.circle(win, (255,255,0), (105,105), 50, 4)
    if x[1] == 1:
       pygame.draw.circle(win, (255,255,0), (250,100), 50, 4)
    if x[2] == 1:
       pygame.draw.circle(win, (255,255,0), (400,100), 50, 4)
    if x[3] == 1:
       pygame.draw.circle(win, (255,255,0), (105,250), 50, 4)
    if x[4] == 1:
       pygame.draw.circle(win, (255,255,0), (255,245), 50, 4)
    if x[5] == 1:
       pygame.draw.circle(win, (255,255,0), (400,250), 50, 4)
    if x[6] == 1:
       pygame.draw.circle(win, (255,255,0), (105,395), 50, 4)
    if x[7] == 1:
       pygame.draw.circle(win, (255,255,0), (250,395), 50, 4)
    if x[8] == 1:
       pygame.draw.circle(win, (255,255,0), (400,395), 50, 4)



    if turn == -1:
        pygame.draw.circle(win, (255,255,0), pos, 50, 4)
    if turn == 1:
        pygame.draw.circle(win, (0,0,255), pos, 50, 4)

    pygame.display.update()