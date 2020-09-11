import pygame
pygame.init()
clock = pygame.time.Clock()

screenWidth = 800
screenHeight = 500

win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Pong!")


width = 20
height = 100

score1 = 0

score2 = 0
def resetBall():
    global Ballx
    global Bally
    Ballx = (screenWidth)//2
    Bally = (screenHeight)//2

resetBall()

BallRadius = 15

paddle1x = 30
paddle1y = 10

paddle2x = screenWidth - width- 30 
paddle2y = screenHeight - height - 10

vel = 8
BallXvel = 5
BallYvel = 5

run = True
while run:
    msElapsed = clock.tick(60) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_w] and paddle1y > vel:
        paddle1y -= vel

    if keys[pygame.K_s] and paddle1y + height < screenHeight - vel:
        paddle1y += vel

    if keys[pygame.K_UP] and paddle2y > vel:
        paddle2y -= vel

    if BallXvel > 0:
        if paddle2y < Bally:
            paddle2y += vel
        if paddle2y > Bally:
            paddle2y -= vel


    if keys[pygame.K_t] and Bally - BallRadius > vel:
        Bally -= vel

    if keys[pygame.K_g] and Bally + BallRadius < screenHeight - vel:
        Bally += vel

    #if keys[pygame.K_f] and not ((Ballx - (BallRadius * 1.25) < paddle1x + width) and ((Bally < paddle1y + height) and (Bally > paddle1y))):
    #    Ballx -= vel

    #if keys[pygame.K_h] and not ((Ballx + (BallRadius * 1.25) > paddle2x ) and ((Bally < paddle2y + height) and (Bally > paddle2y))):
    #    Ballx += vel


    if ((Ballx - (BallRadius * 1.25) < paddle1x + width) and ((Bally < paddle1y + height) and (Bally > paddle1y))):
        BallXvel *= -1

    
    
    if ((Ballx + (BallRadius * 1.25) > paddle2x ) and ((Bally < paddle2y + height) and (Bally > paddle2y))):
        BallXvel *= -1
        
    if Bally - (BallRadius * 1.25) < 0 or Bally + (BallRadius * 1.25) > screenHeight:
        BallYvel *= -1


    if Ballx - (BallRadius * 1.25) < 0:
        print("Point Player 2")
        score2 += 1
        resetBall()
    
    if Ballx + (BallRadius * 1.25) > screenWidth:
        print("Point Player 1")
        score1 += 1
        resetBall()


    caption = "Pong! " + str(score1) + " - " + str(score2)
    pygame.display.set_caption(caption)

    Ballx += BallXvel
    Bally += BallYvel

    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (paddle1x,paddle1y, width, height))
    pygame.draw.rect(win, (255, 0, 0), (paddle2x,paddle2y, width, height))

    pygame.draw.rect(win, (255, 0, 0), (paddle2x,paddle2y, width, height))

    pygame.draw.circle(win, (255,0,0), (Ballx, Bally), BallRadius, 0)

    pygame.display.update()


pygame.quit()