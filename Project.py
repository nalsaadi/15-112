import pygame
from pygame.locals import *
import socket
pygame.init()


 
class Window(): 
    def __init__(self):
        
        self.MenuScreen()
        #self.levelOne()
        #self.LevelTwo()
        #self.LevelThree()
        pygame.display.update()
        
        
        
        
# This determines how fast the screen updates:
        clock = pygame.time.Clock()

    def condition(self):
        window = True
        while window:
            pygame.time.delay(100)
            self.mainWindow.fill((255,255,255))
            self.mainWindow.blit(text, textRect) 
            
            
        #If the user clicked the close button on the screen, it will close
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window = False

                pygame.display.flip()
        
        
        

    def condition1(self):
        #Blue circles are postioned:
        blueCircles=BlueCircles(self.mainWindow, 432, 237, 30, 194, 237, 30)
        #Green circles are positioned:
        greenCircles=GreenCircles(self.mainWindow, 115,237,30,352,158,30)
        #Red circles are positioned:
        redCircles= RedCircles(self.mainWindow, 432, 158, 30, 115, 80, 30)
        #Yellow circles are positioned:
        yellowCircles= YellowCircles(self.mainWindow, 352,315,30,115,395,30)
        #Orange circles are positioned:
        orangeCircles= OrangeCircles(self.mainWindow, 432,315,30,194,395,30)

        pygame.display.update()
        
        #This is the main loop of the program:
        color= (0,0,0)
        Red = (255,0,0)
        Blue= (0,0,255)
        Green = (86, 176, 0)
        Yellow= (255,255,0)
        Orange= (255,140,0)
        Black= (0,0,0)

        #Create lists for each circle to determine their position in the screen:
        red1 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        red2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
        blue1 = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        blue2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
        green1 = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
        green2 = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
        yellow1 = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        yellow2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
        orange1 = [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        orange2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
        
        #Create lists for the midpoints of the x and y values of the circles:
        middleX = [80,158,237,315,395]
        middleY = [115,194,273,352,43]

        Xbgn= [42,118,196,276,354]
        Xend= [118,196,276,354,435]
        Ybgn= [76, 154,234,314,341]
        Yend= [154,234,314,341,474]
       

        #Create an empty list that will add the circle getting selected in the screen by the user:
        selectedcircles = []
        
        CR_list = []
        
        window = True
        circle_selected = False
        
        while window:
            pygame.time.delay(100)
            
        #If the user clicked the close button on the screen, it will close
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window = False
                #If the user clicked on one of the circles using the mouse:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Then it will get the position where the user clicked:
                    pos= pygame.mouse.get_pos()
                    print(pos)
                    
                    #The color at that current postion (pos) will be collected:
                    color= self.mainWindow.get_at(pos)
                    
                    #The postion of the selected circle gets collected:
                    pos_r= pygame.mouse.get_pos(red1)
                    
                    #A condition is made to make sure that the line is drawn in the middle of each gridbox.
                    if abs(pos[0] - pos_r[0]) <= 38 and abs(pos[1] - pos_r[1] <= 38):
                        #This condition is made to make sure that only by selecting circles the colored lines will be drawn:
                        #And that the circle is already not present in the "selectedcircles" list:
                        if (color == Red or color == Blue or color == Green or color == Yellow or color == Orange)\
                        and not (red1 or red2 or blue1 or blue2 or green1 or green2 or yellow1 or yellow2 or orange1 or orange2) in selectedcircles :
                            circle_selected = True
                            selectedcircles.append(red1 or red2 or blue1 or blue2 or green1 or green2 or yellow1 or yellow2 or orange1 or orange2)
                            
                        elif (color == Red or color == Blue or color == Green or color == Yellow or color == Orange)\
                             and (red1 or red2 or blue1 or blue2 or green1 or green2 or yellow1 or yellow2 or orange1 or orange2) in selectedcircles:
                            selectedcircles.remove(red1 or red2 or blue1 or blue2 or green1 or green2 or yellow1 or yellow2 or orange1 or orange2)
                            
                        else:
                            circle_selected = False
                        
                    if circle_selected:
                        for i in (red1 or red2 or blue1 or blue2 or green1 or green2 or yellow1 or yellow2 or orange1 or orange2):
                            if i == 1:
                                choosing = True
                                #A loop is created for when the user does clock on one of the circles:
                                #While the condition is True:
                                while choosing:
                                    #If the user quits the game then the window will close:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            window = False
                                            choosing = False
                                    #If the user clicks the mouse:
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            #Get the position of the mouse (x,y) values:
                                            pos2= pygame.mouse.get_pos()
                                            x= pos_r[0]
                                            y= pos_r[1]
                                            x2= pos2[0]
                                            y2= pos2[1]
                                            column1 = x//76
                                            
                                            row1 = y//76
                                            column2 = x2//76
                                            row2 = y2//76
                                            
                                            columns = column2 - column1
                                            rows= row2 - row1

                                            cr = (columns, rows)

                                            
                                            #This condition is made so that lines do not get drawn outside of the boundaries:
                                            if pos_r[0] >= 42 and pos_r[0] <= 435 and pos_r[1] >= 76 and pos_r[1] <= 474:
                                                #Get the color of the second position:
                                                color1= self.mainWindow.get_at(pos2)
                                                
                                                #Conditions are made based on the where the final position is pressed by the user:

                                                #If the final position occured at column 0 and row 0:
                                                if columns == 0 and rows == 0:
                                                    return None

                                                
                                                #If the final position occured when column is between -5 to 0 and row is 0:
                                                if columns < 0 and columns >= -5 and rows == 0:
                                                    #A new postion variable is created:
                                                    #It sums the value of the columns moved from the initial column value to the final column value:
                                                    new_pos= pos_r[0] + (74*columns)
                                                    #A line is drawn from the initial point to the new postion.
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r),(new_pos, pos_r[1]) , 25)
                                                        
                                                #If the final position occured when column is between 0 to 5 and row is 0:
                                                elif columns > 0 and columns <= 5 and rows == 0:
                                                    #A new postion variable is created:
                                                    #It sums the value of the columns moved from the initial column value to the final column value:
                                                    new_pos= pos_r[0] + (74*columns)
                                                    #A line is drawn from the initial point to the new postion.
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r),(new_pos, pos_r[1]) , 25)

                                                #If the final position occured when column is 0 and row is between -5 to 0:
                                                elif columns == 0 and rows < 0 and rows >= -5:
                                                    #A new postion variable is created:
                                                    #It sums the value of the rows moved from the initial row value to the final row value:
                                                    new_pos= pos_r[1] + (78*rows)

                                                    #A line is drawn from the initial point to the new postion.
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r),(pos_r[0], new_pos) , 25)

                                                #If the final position occured when column is 0 and row is between 0 to 5:
                                                elif columns == 0 and rows > 0  and rows <= 5:
                                                    #A new postion variable is created:
                                                    #It sums the value of the rows moved from the initial row value to the final row value:
                                                        
                                                    new_pos= pos_r[1] + (80*rows)

                                                    #A line is drawn from the initial point to the new postion.
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r),(pos_r[0], new_pos) , 25)

                                                #If the final position occured when column is between 0 to 5 and row is between 0 to 5:
                                                elif columns > 0 and columns <= 5 and rows > 0 and rows <= 5:
                                                    #Two new postion variables are created:
                                                    #The first one sums the value of the columns moved from the initial column value to the final column value:
                                                    new_pos1= pos_r[0] + (74*columns)
                                                    #The second one sums the value of the rows moved from the initial column row to the final row value:
                                                    new_pos2= pos_r[1] + (74*rows)

                                                    #Two lines are drawn to connect the initial value to the final value:
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r),(pos_r[0], new_pos2) , 25)
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r[0], new_pos2),(new_pos1, new_pos2) , 25)
                                                    
                                                #If the final position occured when column is between 0 to 5 and row is between -5 to 0:
                                                elif columns > 0 and columns <= 5 and rows < 0 and rows >= -5:
                                                    #Two new postion variables are created:
                                                    #The first one sums the value of the columns moved from the initial column value to the final column value:
                                                    new_pos1= pos_r[0] + (74*columns)
                                                    #The second one sums the value of the rows moved from the initial column row to the final row value:
                                                    new_pos2= pos_r[1] + (74*rows)
                                                    #Two lines are drawn to connect the initial value to the final value:
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r),(pos_r[0], new_pos2) , 25)
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r[0], new_pos2),(new_pos1, new_pos2) , 25)

                                                #If the final position occured when column is between -5 to 0 and row is between 0 to 5:        
                                                elif columns < 0 and columns >= -5 and rows > 0 and rows <= 5:
                                                    #Two new postion variables are created:
                                                    #The first one sums the value of the columns moved from the initial column value to the final column value:
                                                    new_pos1= pos_r[0] + (74*columns)
                                                    #The second one sums the value of the rows moved from the initial column row to the final row value:
                                                    new_pos2= pos_r[1] + (74*rows)

                                                    #Two lines are drawn to connect the initial value to the final value:
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r),(pos_r[0], new_pos2) , 25)
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r[0], new_pos2),(new_pos1, new_pos2) , 25)

                                                #If the final position occured when column is between -5 to 0 and row is between -5 to 0:
                                                elif columns < 0 and columns >= -5 and rows < 0 and rows >= -5:
                                                    #Two new postion variables are created:
                                                    #The first one sums the value of the columns moved from the initial column value to the final column value:
                                                    new_pos1= pos_r[0] + (74*columns)
                                                    #The second one sums the value of the rows moved from the initial column row to the final row value:
                                                    new_pos2= pos_r[1] + (74*rows)

                                                    #Two lines are drawn to connect the initial value to the final value:
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r),(pos_r[0], new_pos2) , 25)
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r[0], new_pos2),(new_pos1, new_pos2) , 25)

                                                    
                                            choosing = False
                                            cirlce_selected = False
                            pygame.display.flip()

    def condition2(self):
        #Blue circles are postioned:
        blueCircles=BlueCircles(self.mainWindow, 352, 158, 30, 194, 237, 30)
        #Green circles are positioned:
        greenCircles=GreenCircles(self.mainWindow, 194,78,30,352,315,30)
        #Red circles are positioned:
        redCircles= RedCircles(self.mainWindow, 194, 315, 30, 113, 78, 30)
        #Yellow circles are positioned:
        yellowCircles= YellowCircles(self.mainWindow, 434,395,30,113,237,30)

        pygame.display.update()

        #This is the main loop of the program:
        color= (0,0,0)
        Red = (255,0,0)
        Blue= (0,0,255)
        Green = (86, 176, 0)
        Yellow= (255,255,0)
        Orange= (255,140,0)
        Black= (0,0,0)

        #Create lists for each circle to determine their position in the screen:
        red1 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        red2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
        blue1 = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        blue2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
        green1 = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
        green2 = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
        yellow1 = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        yellow2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
        orange1 = [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        orange2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
        
        #Create lists for the midpoints of the x and y values of the circles:
        middleX = [80,158,237,315,395]
        middleY = [115,194,273,352,43]

        Xbgn= [42,118,196,276,354]
        Xend= [118,196,276,354,435]
        Ybgn= [76, 154,234,314,341]
        Yend= [154,234,314,341,474]
       

        #Create an empty list that will add the circle getting selected in the screen by the user:
        selectedcircles = []
        DrawnLines= []

        window = True
        circle_selected = False
        
        while window:
            pygame.time.delay(100)
            
        #If the user clicked the close button on the screen, it will close
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window = False
                #If the user clicked on one of the circles using the mouse:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Then it will get the position where the user clicked:
                    pos= pygame.mouse.get_pos()
                    print(pos)
                    """print(pos)
                    print("MOUSEBUTTONDOWN")"""
                    #The color at that current postion (pos) will be collected:
                    color= self.mainWindow.get_at(pos)
                    """print(color)"""

                    #The postion of the selected circle gets collected:
                    pos_r= pygame.mouse.get_pos(red1)
                    
                    #A condition is made to make sure that the line is drawn in the middle of each gridbox.
                    if abs(pos[0] - pos_r[0]) <= 38 and abs(pos[1] - pos_r[1] <= 38):
                        #This condition is made to make sure that only by selecting circles the colored lines will be drawn:
                        #And that the circle is already not present in the "selectedcircles" list:
                        if (color == Red or color == Blue or color == Green or color == Yellow or color == Orange)\
                        and not (red1 or red2 or blue1 or blue2 or green1 or green2 or yellow1 or yellow2 or orange1 or orange2) in selectedcircles :
                            circle_selected = True
                            selectedcircles.append(red1 or red2 or blue1 or blue2 or green1 or green2 or yellow1 or yellow2 or orange1 or orange2)
                            
                        elif (color == Red or color == Blue or color == Green or color == Yellow or color == Orange)\
                             and (red1 or red2 or blue1 or blue2 or green1 or green2 or yellow1 or yellow2 or orange1 or orange2) in selectedcircles:
                            selectedcircles.remove(red1 or red2 or blue1 or blue2 or green1 or green2 or yellow1 or yellow2 or orange1 or orange2)
                            
                        else:
                            circle_selected = False
                        
                    if circle_selected:
                        for i in (red1 or red2 or blue1 or blue2 or green1 or green2 or yellow1 or yellow2 or orange1 or orange2):
                            if i == 1:
                                choosing = True
                                #A loop is created for when the user does clock on one of the circles:
                                #While the condition is True:
                                while choosing:
                                    #If the user quits the game then the window will close:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            window = False
                                            choosing = False
                                    #If the user clicks the mouse:
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            #Get the position of the mouse (x,y) values:
                                            pos2= pygame.mouse.get_pos()
                                            x= pos_r[0]
                                            y= pos_r[1]
                                            x2= pos2[0]
                                            y2= pos2[1]
                                            column1 = x//76
                                            
                                            row1 = y//76
                                            column2 = x2//76
                                            row2 = y2//76
                                            
                                            columns = column2 - column1
                                            rows= row2 - row1

                                            #This condition is made so that lines do not get drawn outside of the boundaries:
                                            if pos_r[0] >= 42 and pos_r[0] <= 435 and pos_r[1] >= 76 and pos_r[1] <= 474:
                                                #Get the color of the second position:
                                                color1= self.mainWindow.get_at(pos2)
                                                
                                                #Conditions are made based on the where the final position is pressed by the user:

                                                #If the final position occured at column 0 and row 0:
                                                if columns == 0 and rows == 0:
                                                    return None

                                                
                                                #If the final position occured when column is between -5 to 0 and row is 0:
                                                if columns < 0 and columns >= -5 and rows == 0:
                                                    #A new postion variable is created:
                                                    #It sums the value of the columns moved from the initial column value to the final column value:
                                                    new_pos= pos_r[0] + (76*columns)
                                                    #A line is drawn from the initial point to the new postion.
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r),(new_pos, pos_r[1]) , 25)
                                                    
                                                        
                                                #If the final position occured when column is between 0 to 5 and row is 0:
                                                elif columns > 0 and columns <= 5 and rows == 0:
                                                    #A new postion variable is created:
                                                    #It sums the value of the columns moved from the initial column value to the final column value:
                                                    new_pos= pos_r[0] + (76*columns)
                                                    #A line is drawn from the initial point to the new postion.
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r),(new_pos, pos_r[1]) , 25)


                                                #If the final position occured when column is 0 and row is between -5 to 0:
                                                elif columns == 0 and rows < 0 and rows >= -5:
                                                    #A new postion variable is created:
                                                    #It sums the value of the rows moved from the initial row value to the final row value:
                                                    new_pos= pos_r[1] + (78*rows)

                                                    #A line is drawn from the initial point to the new postion.
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r),(pos_r[0], new_pos) , 25)


                                                #If the final position occured when column is 0 and row is between 0 to 5:
                                                elif columns == 0 and rows > 0  and rows <= 5:
                                                    #A new postion variable is created:
                                                    #It sums the value of the rows moved from the initial row value to the final row value:
                                                        
                                                    new_pos= pos_r[1] + (80*rows)

                                                    #A line is drawn from the initial point to the new postion.
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r),(pos_r[0], new_pos) , 25)


                                                #If the final position occured when column is between 0 to 5 and row is between 0 to 5:
                                                elif columns > 0 and columns <= 5 and rows > 0 and rows <= 5:
                                                    #Two new postion variables are created:
                                                    #The first one sums the value of the columns moved from the initial column value to the final column value:
                                                    new_pos1= pos_r[0] + (76*columns)
                                                    #The second one sums the value of the rows moved from the initial column row to the final row value:
                                                    new_pos2= pos_r[1] + (76*rows)

                                                    #Two lines are drawn to connect the initial value to the final value:
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r),(pos_r[0], new_pos2) , 25)
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r[0], new_pos2),(new_pos1, new_pos2) , 25)


                                                #If the final position occured when column is between 0 to 5 and row is between -5 to 0:
                                                elif columns > 0 and columns <= 5 and rows < 0 and rows >= -5:
                                                    #Two new postion variables are created:
                                                    #The first one sums the value of the columns moved from the initial column value to the final column value:
                                                    new_pos1= pos_r[0] + (76*columns)
                                                    #The second one sums the value of the rows moved from the initial column row to the final row value:
                                                    new_pos2= pos_r[1] + (76*rows)
                                                    #Two lines are drawn to connect the initial value to the final value:
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r),(pos_r[0], new_pos2) , 25)
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r[0], new_pos2),(new_pos1, new_pos2) , 25)

                                                
                                                #If the final position occured when column is between -5 to 0 and row is between 0 to 5:        
                                                elif columns < 0 and columns >= -5 and rows > 0 and rows <= 5:
                                                    #Two new postion variables are created:
                                                    #The first one sums the value of the columns moved from the initial column value to the final column value:
                                                    new_pos1= pos_r[0] + (76*columns)
                                                    #The second one sums the value of the rows moved from the initial column row to the final row value:
                                                    new_pos2= pos_r[1] + (76*rows)

                                                    #Two lines are drawn to connect the initial value to the final value:
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r),(pos_r[0], new_pos2) , 25)
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r[0], new_pos2),(new_pos1, new_pos2) , 25)


                                                #If the final position occured when column is between -5 to 0 and row is between -5 to 0:
                                                elif columns < 0 and columns >= -5 and rows < 0 and rows >= -5:
                                                    #Two new postion variables are created:
                                                    #The first one sums the value of the columns moved from the initial column value to the final column value:
                                                    new_pos1= pos_r[0] + (76*columns)
                                                    #The second one sums the value of the rows moved from the initial column row to the final row value:
                                                    new_pos2= pos_r[1] + (76*rows)

                                                    #Two lines are drawn to connect the initial value to the final value:
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r),(pos_r[0], new_pos2) , 25)
                                                    line= pygame.draw.line(self.mainWindow, color, (pos_r[0], new_pos2),(new_pos1, new_pos2) , 25)

                                                    
                                            #print(DrawnLines)
                                            choosing = False
                                            cirlce_selected = False
                                #print(line)
                            pygame.display.flip()

    def MenuScreen(self):
        #Level one main window is opened:
        self.mainWindow= pygame.display.set_mode((470,600))
        X= 470
        Y= 300
        Pink= (199,21,133)
        #Caption of the window name:
        self.display = pygame.display.set_caption("Flow Free")
        #Background image of window gets set and displayed:
        self.windowBackground= pygame.image.load("image.jpg")
        self.mainWindow.blit(self.windowBackground, (40,0))
        self.wnd1= self.mainWindow
        font = pygame.font.Font('freesansbold.ttf', 80)
        text = font.render('flow', True, Pink)
        
        textRect = text.get_rect()
        
        textRect.center = (X // 2, Y // 2)
    
        
        pygame.display.flip()

        window = True
        while window:
            pygame.time.delay(100)
            self.mainWindow.blit(text, textRect) 
            
            
        #If the user clicked the close button on the screen, it will close
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window = False

                

                pygame.display.flip()
                                        
    def levelOne(self):
        #Level one main window is opened:
        self.mainWindow= pygame.display.set_mode((470,600))
        #Caption of the window name:
        self.display = pygame.display.set_caption("Flow Free")
        #Background image of window gets set and displayed:
        self.windowBackground= pygame.image.load("image.jpeg")
        self.mainWindow.blit(self.windowBackground, (40,0))
        self.wnd1= self.mainWindow
                
        self.condition1()

        
        
    def LevelTwo(self):
        #Level two main window is opened:
        self.mainWindow= pygame.display.set_mode((470,600))
        #Caption of the window name:
        self.display = pygame.display.set_caption("Flow Free")
        #Background image of window gets set and displayed:
        self.windowBackground= pygame.image.load("image2.png")
        self.mainWindow.blit(self.windowBackground, (40,0))
        
        self.condition2()

    def LevelThree(self):
        #Level two main window is opened:
        self.mainWindow= pygame.display.set_mode((470,600))
        #Caption of the window name:
        self.display = pygame.display.set_caption("Flow Free")
        #Background image of window gets set and displayed:
        self.windowBackground= pygame.image.load("image3.png")
        self.mainWindow.blit(self.windowBackground, (40,0))
        #Blue circles are postioned:
        blueCircles=BlueCircles(self.mainWindow, 213, 105, 25, 379, 171, 25)
        #Green circles are positioned:
        greenCircles=GreenCircles(self.mainWindow, 413, 235 ,25, 278,360 ,25)
        #Red circles are positioned:
        redCircles= RedCircles(self.mainWindow, 314, 170, 25, 146, 232, 25)
        #Yellow circles are positioned:
        yellowCircles= YellowCircles(self.mainWindow, 180,296 ,25,281,233,25)
        #Orange circles are positioned:
        orangeCircles= OrangeCircles(self.mainWindow, 211,360,25,347, 235,25)

    #def isValid():
        
                
class BlueCircles():
    #This function is used to create the two blue circles presented on the grid:
    def __init__(self,mainWindow, heightB1, widthB1, radiusB1, heightB2, widthB2, radiusB2):
        #The size measurements for the first circle are assigned to attributes:
        self.heightB1= heightB1
        self.widthB1= widthB1
        self.radiusB1= radiusB1

        #The size measurements for the second circle are assigned to attributes:
        self.heightB2= heightB2
        self.widthB2= widthB2
        self.radiusB2= radiusB2
        
        self.mainWindow = mainWindow
        #The method used to create the first circle gets called:
        self.circleB1(self.widthB1, self.heightB1, self.radiusB1, self.mainWindow)
        #The method used to create the second circle gets called:
        self.circleB2(self.widthB2, self.heightB2, self.radiusB2, self.mainWindow)

        pos= pygame.mouse.get_pos()
        self.event = pygame.event.poll()        

    def circleB1(self, width, height, radius, mainWindow):
        #Assign the color of the circle to an attribute:
        self.blue= (0,0,255)
        #Draw the circle by using the measurements defined and the color:
        self.circle= pygame.draw.circle(self.mainWindow,self.blue, (self.widthB1,self.heightB1), self.radiusB1)

    def circleB2(self, width, height, radius, mainWindow):
        #Assign the color of the circle to an attribute:
        self.blue= (0,0,255)
        #Draw the circle by using the measurements defined and the color:
        self.circle= pygame.draw.circle(self.mainWindow,self.blue, (self.widthB2,self.heightB2), self.radiusB2)
        

class GreenCircles():
    #This function is used to create the two green circles presented on the grid:
    def __init__(self,mainWindow, heightG1, widthG1, radiusG1, heightG2, widthG2, radiusG2):
        #The size measurements for the first circle are assigned to attributes:
        self.heightG1= heightG1
        self.widthG1= widthG1
        self.radiusG1= radiusG1

        #The size measurements for the second circle are assigned to attributes:
        self.heightG2= heightG2
        self.widthG2= widthG2
        self.radiusG2= radiusG2
        
        self.mainWindow = mainWindow
        #The method used to create the first circle gets called:
        self.circleG1(self.widthG1, self.heightG1, self.radiusG1, self.mainWindow)
        #The method used to create the second circle gets called:
        self.circleG2(self.widthG2, self.heightG2, self.radiusG2, self.mainWindow)
        

    def circleG1(self, width, height, radius, mainWindow):
        #Assign the color of the circle to an attribute:
        self.green= (86, 176, 0)
        #Draw the circle by using the measurements defined and the color:
        self.circle= pygame.draw.circle(self.mainWindow,self.green, (self.widthG1,self.heightG1), self.radiusG1)

    def circleG2(self, width, height, radius, mainWindow):
        #Assign the color of the circle to an attribute:
        self.green= (86, 176, 0)
        #Draw the circle by using the measurements defined and the color:
        self.circle= pygame.draw.circle(self.mainWindow,self.green, (self.widthG2,self.heightG2), self.radiusG2)



class RedCircles():
    #This function is used to create the two red circles presented on the grid:
    def __init__(self,mainWindow, heightR1, widthR1, radiusR1, heightR2, widthR2, radiusR2):
        #The size measurements for the first circle are assigned to attributes:
        self.heightR1= heightR1
        self.widthR1= widthR1
        self.radiusR1= radiusR1

        #The size measurements for the second circle are assigned to attributes:
        self.heightR2= heightR2
        self.widthR2= widthR2
        self.radiusR2= radiusR2
        
        self.mainWindow = mainWindow
        #The method used to create the first circle gets called:
        self.circleR1(self.widthR1, self.heightR1, self.radiusR1, self.mainWindow)
        #The method used to create the second circle gets called:
        self.circleR2(self.widthR2, self.heightR2, self.radiusR2, self.mainWindow)
        

    def circleR1(self, width, height, radius, mainWindow):
        #Assign the color of the circle to an attribute:
        self.red= (255,0,0)
        #Draw the circle by using the measurements defined and the color:
        self.circle= pygame.draw.circle(self.mainWindow,self.red, (self.widthR1,self.heightR1), self.radiusR1)

    def circleR2(self, width, height, radius, mainWindow):
        #Assign the color of the circle to an attribute:
        self.red= (255,0,0)
        #Draw the circle by using the measurements defined and the color:
        self.circle= pygame.draw.circle(self.mainWindow,self.red, (self.widthR2,self.heightR2), self.radiusR2)


class YellowCircles():
    #This function is used to create the two yellow circles presented on the grid:
    def __init__(self,mainWindow, heightY1, widthY1, radiusY1, heightY2, widthY2, radiusY2):
        #The size measurements for the first circle are assigned to attributes:
        self.heightY1= heightY1
        self.widthY1= widthY1
        self.radiusY1= radiusY1

        #The size measurements for the second circle are assigned to attributes:
        self.heightY2= heightY2
        self.widthY2= widthY2
        self.radiusY2= radiusY2
        
        self.mainWindow = mainWindow
        #The method used to create the first circle gets called:
        self.circleY1(self.widthY1, self.heightY1, self.radiusY1, self.mainWindow)
        #The method used to create the second circle gets called:
        self.circleY2(self.widthY2, self.heightY2, self.radiusY2, self.mainWindow)
        

    def circleY1(self, width, height, radius, mainWindow):
        #Assign the color of the circle to an attribute:
        self.yellow= (255,255,0)
        #Draw the circle by using the measurements defined and the color:
        self.circle= pygame.draw.circle(self.mainWindow,self.yellow, (self.widthY1,self.heightY1), self.radiusY1)

    def circleY2(self, width, height, radius, mainWindow):
        #Assign the color of the circle to an attribute:
        self.yellow= (255,255,0)
        #Draw the circle by using the measurements defined and the color:
        self.circle= pygame.draw.circle(self.mainWindow,self.yellow, (self.widthY2,self.heightY2), self.radiusY2)


class OrangeCircles():
    #This function is used to create the two orange circles presented on the grid:
    def __init__(self,mainWindow, heightO1, widthO1, radiusO1, heightO2, widthO2, radiusO2):
        #The size measurements for the first circle are assigned to attributes:
        self.heightO1= heightO1
        self.widthO1= widthO1
        self.radiusO1= radiusO1 

        #The size measurements for the second circle are assigned to attributes:
        self.heightO2= heightO2
        self.widthO2= widthO2
        self.radiusO2= radiusO2
        
        self.mainWindow = mainWindow
        #The method used to create the first circle gets called:
        self.circleO1(self.widthO1, self.heightO1, self.radiusO1, self.mainWindow)
        #The method used to create the second circle gets called:
        self.circleO2(self.widthO2, self.heightO2, self.radiusO2, self.mainWindow)

    def circleO1(self, width, height, radius, mainWindow):
        #Assign the color of the circle to an attribute:
        self.orange= (255,140,0)
        #Draw the circle by using the measurements defined and the color:
        self.circle= pygame.draw.circle(self.mainWindow,self.orange, (self.widthO1,self.heightO1), self.radiusO1)

    def circleO2(self, width, height, radius, mainWindow):
        #Assign the color of the circle to an attribute:
        self.orange= (255,140,0)
        #Draw the circle by using the measurements defined and the color:
        self.circle= pygame.draw.circle(self.mainWindow,self.orange, (self.widthO2,self.heightO2), self.radiusO2)


#The server connection to make it online:
def StartConnection(IPAddress,PortNumber):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    s.connect((IPAddress,PortNumber))
        
    return s

def block(username,password, challenge):
    block= ""
    n= len(password)
    
    block= block + str(password)
    
    m= len(challenge)
    
    block= block + str(challenge)
    
    message = str ( n + m)
    
    msg= len(message)
    
    block= block + str(msg)

    length= n + m + msg
    block_length = 512
    total_length= (block_length - length) - 1
    msgresult = password+challenge+"1"+"0"*total_length+message
    
    return msgresult

#The block is brokend down into chunks of 32 characters:
def chunk_list(b):
    M = []
    x = 0
    for i in range (0, len(b),32):
        m = b[i:i+32]
        x = 0
        for y in range(0,len(m)):
            x = x + ord(m[y])  
        M.append(x)
    return M
        
#The chunks are processed:

def chunkProcess(s,M):
    S=[]
    K=[]
    S[0:15] = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22]
    S[16:31] = [5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20]
    S[32:47] = [4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23]
    S[48:63] = [6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]
    K[0:3] = [ 0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee ]
    K[4:7] = [ 0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501 ]
    K[8:11] = [ 0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be ]
    K[12:15] = [ 0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821 ]
    K[16:19] = [ 0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa ]
    K[20:23] = [ 0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8 ]
    K[24:27] = [ 0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed ]
    K[28:31] = [ 0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a ]
    K[32:35] = [ 0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c ]
    K[36:39] = [ 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70 ]
    K[40:43] = [ 0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05 ]
    K[44:47] = [ 0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665 ]
    K[48:51] = [ 0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039 ]
    K[52:55] = [ 0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1 ]
    K[56:59] = [ 0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1 ]
    K[60:63] = [ 0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391 ]

    #Initialize variables:
    a0 = 0x67452301   #A
    b0 = 0xefcdab89   #B
    c0 = 0x98badcfe   #C
    d0 = 0x10325476   #D
    A = a0
    B = b0
    C = c0
    D = d0
#Main loop:
    for i in range(0,64):
        if 0 <= i <= 15:
            F = (B & C) | ((~ B) & D)
            F = F & 0xFFFFFFFF
            g = i
        elif 16 <= i<= 31:
            F = (D & B) | ((~ D) & C)
            F = F & 0xFFFFFFFF
            g = (5*i + 1) % 16
        elif 32 <= i <= 47:
            F = B ^ C ^ D
            F = F & 0xFFFFFFFF
            g = (3*i + 5) % 16
        elif 48 <= i <= 63:
            F = C ^ (B | (~ D))
            F = F & 0xFFFFFFFF
            g = (7*i) % 16

        dTemp = D
        D = C
        C = B
        B = B + leftrotate((A + F + K[i] + M[g]), S[i])
        B = B & 0xFFFFFFFF
        A = dTemp
      
  #Add this chunk's hash to result:
    a0 = (a0 + A) & 0xFFFFFFFF
    b0 = (b0 + B) & 0xFFFFFFFF
    c0 = (c0 + C) & 0xFFFFFFFF
    d0 = (d0 + D) & 0xFFFFFFFF
    result= str(a0) + str(b0) + str(c0) + str(d0)
    return result
    


  #leftrotate function definition
def leftrotate (x, c):
    return (x << c)&0xFFFFFFFF | (x >> (32-c)&0x7FFFFFFF>>(32-c))


def message_digest(s, username, password, challenge):
    b= block(username,password, challenge)
    M=chunk_list(b)
    return M

def login(s, username, password):
    
    send = s.send(b"LOGIN " +bytes(username,"utf-8") + b"\n")
    
    msg = s.recv(512)
    
    msg = str(msg, 'utf-8')

    challenge = msg.split()[2]

    M = message_digest(s, username, password, challenge)
    
    send = s.send(b"LOGIN " +bytes(username ,"utf-8")+b" "+ bytes(chunkProcess(s, M),"utf-8")+b"\n")
    
    receive = s.recv(512).decode("utf-8")


    if "Login Successful" in receive:
        return True
    else:
        return False

def getUsers(s):
    s.send(b"@users\n")
    var= s.recv(512).decode("utf-8")
    var = var.split("@")
    return var[4:]

def getFriends(s):
    s.send(b"@friends")
    var= s.recv(512).decode("utf-8")
    var= var.split("@")
    return var[4:]

def getRequests(s):
    s.send(b"@rxrqst")
    var= str(s.recv(512).decode("utf-8"))
    var= var.split("@")
    return var[3:]


def sendFriendRequest(s, friend):
    size=str(22+len(friend))
    while len(size) < 5:
        size= "0" + size
       
    request= b"@"+str(size).encode()+b"@request@friend@"+str(friend).encode()+b"\n"
    
    s.send(request)
    
    r= s.recv(512).decode("utf-8")

    if "@ok" in r:
        return True
    else:
        return False


def acceptFriendRequest(s, friend):
    size=str(21+len(friend))
    while len(size) < 5:
        size= "0" + size
    accept= b"@"+str(size).encode()+b"@accept@friend@"+str(friend).encode()+b"\n"
    s.send(accept)
    r= s.recv(512).decode("utf-8")
    
    if "@ok" in r:
        return True
    else:
        return False


def sendMessage(s, friend, message):
    size=str(16+len(friend)+len(message))
    while len(size) < 5:
        size= "0" + size
    sendmsg= ("@"+str(size)+"@sendmsg@"+str(friend) +"@"+ message + "\n").encode()

    s.send(sendmsg)
    r= s.recv(512).decode("utf-8")

    if "@ok" in r:
        return True
    else:
        return False

def getMail(s):
    texts = []
    files = []
    s.send(b"@rxmsg")
    r= str(s.recv(4096).decode("utf-8"))
    r = r.split("@")
    for i in range(len(r)):
        if r[i] == "msg":
            texts.append((r[i+1],r[i+2]))
            i= i + 3
        if i<len(r) and r[i] == "file":
            files.append((r[i+1],r[i+2]))
            a=open(r[i+2],"w")
            a.write(r[i+3])
            a.close()
            i=i+4                   
    return (texts,files)

s= StartConnection("86.36.46.10", 15112)
wnd = Window()
pygame.display.update()
pygame.init()
pygame.quit()
