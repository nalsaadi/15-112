import pygame
from pygame.locals import *
from tkinter import *
import tkinter.messagebox as tm
pygame.init()

class Level1(object):
    def __init__(self):
        self.mainWindow= pygame.display.set_mode((470,600))
        self.display = pygame.display.set_caption("Flow Free")
        self.windowBackground= pygame.image.load("image.jpeg")
        self.mainWindow.blit(self.windowBackground, (40,0))
        self.wnd1= self.mainWindow
        blueCircles=BlueCircles(self.mainWindow)
        greenCircles=GreenCircles(self.mainWindow)
        redCircles= RedCircles(self.mainWindow)
        yellowCircles= YellowCircles(self.mainWindow)
        orangeCircles= OrangeCircles(self.mainWindow)
        pygame.display.update()
        
        window = True
# This determines how fast the screen updates:
        clock = pygame.time.Clock()

#This is the main loop of the program:
        while window:
            pygame.time.delay(100)
            pos= pygame.mouse.get_pos()
            self.event = pygame.event.poll()
#If the user clicked the close button on the screen, it will close
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    window = False

                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.line(self.mainWindow, (0,0,255), (237,432), (237,194), 25)
                    pygame.display.update()

                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.line(self.mainWindow, (86, 176, 0), (158,352), (158,103), 25)
                    pygame.draw.line(self.mainWindow, (86, 176, 0), (158,115), (237,115), 25)
                    pygame.display.update()

                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.line(self.mainWindow, (255,0,0), (158,432), (68,432), 25)
                    pygame.draw.line(self.mainWindow, (255,0,0), (80,432), (80,115), 25)
                    pygame.display.update()

                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.line(self.mainWindow, (255,255,0), (315,352) , (315,115), 25)
                    pygame.draw.line(self.mainWindow, (255,255,0), (303,115) , (395,115), 25)
                    pygame.display.update()

                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.line(self.mainWindow, (255,140,0), (315,432), (407,432), 25)
                    pygame.draw.line(self.mainWindow, (255,140,0), (395,432), (395,194), 25)    
                    pygame.display.update()
        
class BlueCircles():
    def __init__(self,mainWindow):
        self.heightB1= 432
        self.widthB1= 237
        self.radiusB1= 30

        self.heightB2= 194
        self.widthB2= 237
        self.radiusB2= 30
        
        self.mainWindow = mainWindow
        self.circleB1(self.widthB1, self.heightB1, self.radiusB1, self.mainWindow)
        self.circleB2(self.widthB2, self.heightB2, self.radiusB2, self.mainWindow)
        

    def circleB1(self, width, height, radius, mainWindow):
        self.blue= (0,0,255)
        self.circle= pygame.draw.circle(self.mainWindow,self.blue, (self.widthB1,self.heightB1), self.radiusB1)

    def circleB2(self, width, height, radius, mainWindow):
        self.blue= (0,0,255)
        self.circle= pygame.draw.circle(self.mainWindow,self.blue, (self.widthB2,self.heightB2), self.radiusB2)
        

class GreenCircles():
    def __init__(self,mainWindow):
        self.heightG1= 115
        self.widthG1= 237
        self.radiusG1= 30 

        self.heightG2= 352
        self.widthG2= 158
        self.radiusG2= 30
        
        self.mainWindow = mainWindow
        self.circleG1(self.widthG1, self.heightG1, self.radiusG1, self.mainWindow)
        self.circleG2(self.widthG2, self.heightG2, self.radiusG2, self.mainWindow)
        

    def circleG1(self, width, height, radius, mainWindow):
        self.green= (86, 176, 0)
        self.circle= pygame.draw.circle(self.mainWindow,self.green, (self.widthG1,self.heightG1), self.radiusG1)

    def circleG2(self, width, height, radius, mainWindow):
        self.green= (86, 176, 0)
        self.circle= pygame.draw.circle(self.mainWindow,self.green, (self.widthG2,self.heightG2), self.radiusG2)



class RedCircles():
    def __init__(self,mainWindow):
        self.heightR1= 432 
        self.widthR1= 158
        self.radiusR1= 30

        self.heightR2= 115
        self.widthR2= 80
        self.radiusR2= 30
        
        self.mainWindow = mainWindow
        self.circleR1(self.widthR1, self.heightR1, self.radiusR1, self.mainWindow)
        self.circleR2(self.widthR2, self.heightR2, self.radiusR2, self.mainWindow)
        

    def circleR1(self, width, height, radius, mainWindow):
        self.red= (255,0,0)
        self.circle= pygame.draw.circle(self.mainWindow,self.red, (self.widthR1,self.heightR1), self.radiusR1)

    def circleR2(self, width, height, radius, mainWindow):
        self.red= (255,0,0)
        self.circle= pygame.draw.circle(self.mainWindow,self.red, (self.widthR2,self.heightR2), self.radiusR2)


class YellowCircles():
    def __init__(self,mainWindow):
        self.heightY1= 352 
        self.widthY1= 315
        self.radiusY1= 30

        self.heightY2= 115
        self.widthY2= 395
        self.radiusY2= 30
        
        self.mainWindow = mainWindow
        self.circleY1(self.widthY1, self.heightY1, self.radiusY1, self.mainWindow)
        self.circleY2(self.widthY2, self.heightY2, self.radiusY2, self.mainWindow)
        

    def circleY1(self, width, height, radius, mainWindow):
        self.yellow= (255,255,0)
        self.circle= pygame.draw.circle(self.mainWindow,self.yellow, (self.widthY1,self.heightY1), self.radiusY1)

    def circleY2(self, width, height, radius, mainWindow):
        self.yellow= (255,255,0)
        self.circle= pygame.draw.circle(self.mainWindow,self.yellow, (self.widthY2,self.heightY2), self.radiusY2)


class OrangeCircles():
    def __init__(self,mainWindow):
        self.heightO1= 432
        self.widthO1= 315
        self.radiusO1= 30 

        self.heightO2= 194
        self.widthO2= 395
        self.radiusO2= 30
        
        self.mainWindow = mainWindow
        self.circleO1(self.widthO1, self.heightO1, self.radiusO1, self.mainWindow)
        self.circleO2(self.widthO2, self.heightO2, self.radiusO2, self.mainWindow)

    def circleO1(self, width, height, radius, mainWindow):
        self.orange= (255,140,0)
        self.circle= pygame.draw.circle(self.mainWindow,self.orange, (self.widthO1,self.heightO1), self.radiusO1)

    def circleO2(self, width, height, radius, mainWindow):
        self.orange= (255,140,0)
        self.circle= pygame.draw.circle(self.mainWindow,self.orange, (self.widthO2,self.heightO2), self.radiusO2) 
        

            
wnd1= Level1()
pygame.display.update()
pygame.quit()
