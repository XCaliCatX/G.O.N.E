import pygame

#initialize the pygame
pygame.init()

#create the screen, widthxheight
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Cat Sharp Shooter")
#use a png, 32 pixels for icon, flaticon.com
#icon = pygame.image.load("name of image")
#pygame.display.set_icon(icon)

#player define image, and location on screen as variables, so they can be change
playerImg = pygame.image.load("cat.png")
playerX =370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerImg, (x,y))

#game loop
#create loop for event window to stay open until x is clicked
running = True
while running:
    # change screen background, R,G,B
    screen.fill((0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    #change player position
    playerX += playerX_change
    #stop player from exiting screen
    if playerX >= 736:
        playerX = 736
    elif playerX <=0:
        playerX =0
    #call player to display it. over the top of the fill, otherwise fill will be on top
    player(playerX,playerY)

    #update screen to change anything
    pygame.display.update()