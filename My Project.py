import pygame
from pygame.locals import *
pygame.init()

class Window(object):
    def __init__(self):
        self.mainWindow= pygame.display.set_mode((500,600))

        self.display = pygame.display.set_caption("Flow Free")

        #self.windowBackground= pygame.image.load("images.jpg")

        #self.mainWindow.blit(self.windowBackground, (40,0))

        #self.gridlines()

        #self.circles(50, 50, 3)

        #pygame loop.

    def circles(self, x, y, radius):
        self.x = x
        self.y = y
        
        self.r = radius
        self.window = True
        while self.window:
            self.delay= pygame.time.delay(100)
            self.event= pygame.event.get()
            for event in self.event:
                if event.type == pygame.QUIT:
                    window = False
            pygame.draw.circle(self.mainWindow, (255,0,0), (self.x,self.y), self.r)
        


    def gridlines(self):
        self.width = 30
        self.height= 30
        self.margin = 3

        self.grids= []
        for row in range(5):
            self.grids.append([])
            #print(self.grids)
            for column in range(5):
                self.grids.append(row)
                self.grids.append(0)
        self.grids[1][5] = 1
        


        self.done = True
        while self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.position= pygame.mouse.get_pos()

                    column = self.postion[0]// (self.width + self.margin)
                    row = self.postion[1]// (self.height + self.margin)
                    self.grids[row][column] = 1

        pygame.display.flip()

wnd= Window()
pygame.display.update()

#pygame.quit()

