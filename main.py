import pygame
import time

pygame.init()

screen_width = 1000
screen_height = 700  
win = pygame.display.set_mode((screen_width, screen_height))

startTime = time.time()
deltaTime = 0
running = True

while running:
  if (newTime - startTime) >= 1 / FPS:
        deltaTime = (newTime - startTime)
        startTime = newTime

        heldKeys = pygame.key.get_pressed()

        if heldKeys[pygame.K_w]: #move up
            if playerY < 0:
                playerY = screen_height # if top side is hit player moves through the bottom side
            playerY -= vel * deltaTime
    
        if heldKeys[pygame.K_s]: #move down
            if playerY > screen_height:
                playerY = 0 #if bottom side is hit player moves through the top side
            playerY += vel * deltaTime

        if heldKeys[pygame.K_a]: # move left
            if playerX < 0:
                playerX = screen_width # when player hits the left side of the screen the move to the right
            playerX -= vel * deltaTime
        
        if heldKeys[pygame.K_d]: #move right
            if playerX > screen_width:
                playerX = 0 # when player hits the edge of the screen on the right they move to the left hand side
            playerX += vel * deltaTime
     
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
          
