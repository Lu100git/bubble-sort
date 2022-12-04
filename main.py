import pygame
from random import randint
from time import sleep
pygame.init()
window = pygame.display.set_mode((640,480))

class Line:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = int(h)
        self.shape = pygame.Surface((self.w,self.h))
        self.shape.fill((255,255,255))
    def draw(self, window):
        self.scaledShape = pygame.transform.scale(self.shape, (self.w, self.h))
        window.blit(self.scaledShape, (self.x, self.y))



linesArray = []
amount = 80

for i in range(amount):
    line = Line(i * 8, 100, 5, randint(1, 350))
    linesArray.append(line)

window.fill(0)
for i in range(amount - 1):
    linesArray[i].draw(window)
    pygame.display.update()
    sleep(0.05)


for x in range(amount):
    for i in range(amount - 1):
        window.fill(0)
        if linesArray[i].h > linesArray[i+1].h:
            aux = linesArray[i].h
            linesArray[i].h = linesArray[i+1].h
            linesArray[i+1].h = aux
        for j in range(amount - 1):
            linesArray[j].draw(window)
        pygame.display.update()
        #sleep(10/1000)





