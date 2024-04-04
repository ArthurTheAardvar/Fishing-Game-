import pygame
import random
from pygame.math import Vector2
pygame.init()
pygame.display.set_caption("Fishing Game")
screen = pygame.display.set_mode((900,900)) 
clock = pygame.time.Clock()
doExit = False

class Player():

    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos,ypos)
        self.vx = 0
        self.vy = 0

    def movement(self):
        for event in pygame.event.get(): #quit game if x is pressed in top corner
     
            if event.type == pygame.KEYDOWN: #keyboard input

                if event.key == pygame.K_UP:
                    self.vy -= 1
                
                if event.key == pygame.K_DOWN:
                    self.vy += 1

            self.pos.x += self.vx
            self.pos.y += self.vy


    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.pos.x, self.pos.y, 20, 100), 1)


player = Player(400,400)


while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True


        player.movement()





        screen.fill((0,0,0))
        player.draw()

        pygame.display.flip()
pygame.quit()





















    