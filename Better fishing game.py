import pygame
import random
from pygame.math import Vector2
pygame.init()
pygame.display.set_caption("Fishing Game")
screen = pygame.display.set_mode((900,900)) 
clock = pygame.time.Clock()
timer = 0
doExit = False

vx = 0
vy = 0
xpos = 400
ypos = 400
pos = Vector2(xpos,ypos)

moveDown = False
moveUp = False

score = 0

class Fish():
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos,ypos)
        self.vy = 0

    def move(self):
        self.movement = random.randrange(0, 50)

        if self.movement >=25:
            self.vy += 0.5

        else:
            self.vy -= 0.5

        self.pos.y += self.vy

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 255), (self.pos.x, self.pos.y, 20, 20), 1)


    def collision(self):
        if self.pos.y < 100:
            self.vy *= -1

        elif self.pos.y > 800:
            self.vy *= -1



fish = Fish(400, 500)

while True:
    clock.tick(60)
    timer+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
      
     
        if event.type == pygame.KEYDOWN: #keyboard input

            if event.key == pygame.K_UP:
                moveUp = True
                
            if event.key == pygame.K_DOWN:
                moveDown = True

        elif event.type == pygame.KEYUP: #keyboard input

            if event.key == pygame.K_UP:
                moveUp = False
                
            if event.key == pygame.K_DOWN:
                moveDown = False

            
        if moveUp == True:
            vy -=15

        elif moveDown == True:
            vy +=15

        else:
            vy = 0

    if pos.y < 100:
        vy *= -1

    elif pos.y > 800:
        vy *= -1


    pos.x += vx
    pos.y += vy


    if fish.pos.y == pos.y:
        score += 1

    print(score)

       
    fish.move()
    fish.collision()




    screen.fill((0,0,0))
    fish.draw()
       
    pygame.draw.rect(screen, (255, 255, 255), (pos.x, pos.y, 20, 100), 1)

    
    pygame.display.flip()
pygame.quit()











    