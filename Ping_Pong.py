import pygame 
import random 

pygame.init()

red = [255,0,0]
lBlue = [153,204,255]
kollane = [255,255,10]
punane = [255,0,0]
hall = [200,200,200]
roosa = [255,150,255]
roheline = [100,255,100]

screenX = 650
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Klaviatur juhtimine")
screen.fill(lBlue)
clock = pygame.time.Clock()

posX, posY = screenX/2, screenY/2
speedX, speedY = 0,0

pilt = pygame.image.load("zz.png")
screen.blit(pilt,(120,260))

gameover = False
while not gameover:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speedX = -3
            elif event.key == pygame.K_RIGHT:

                speedX = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speedX = 0
            

    posX += speedX
    posY += speedY
    ruut = pygame.draw.rect(screen, red, [posX, posY, 60, 30])
    pygame.display.flip()
    screen.fill(lBlue)

pygame.quit()
