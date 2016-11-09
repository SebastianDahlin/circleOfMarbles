## A band of moving marbles

#Import pygame and math
import pygame
import math
import time
import random
import sys

### Start the program
if __name__ == "__main__":
    #-----------Set this to something fun----------------#
    #Set the circRadius of the circle
    circRadius = 150
    #Set the circRadius of the marbles
    marbR = 15
    #Amount of marbles
    amount = 15
    #Screen height and width
    screenHeight = 800
    screenWidth = 400
    #----------------------------------------------------#
    
    #Define a screen
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    #Set a new windows title
    pygame.display.set_caption("Circle of marbles")
    #Decide a middle point
    middle = (int(screenWidth/2),int(screenHeight/2))
    #Create a list for the marbles
    marbList = []
    ##Get the "spread", ie the amount of degrees between each marble, in order to not make them collide when plotting them for the first time
    spreader = math.degrees(2*math.sin(marbR/circRadius))
    print(spreader)
    #Create x amount of marbles in the list with the distance equal to its eqlidical distance between each other along a cirlce of circRadius Y
    for i in range(0,amount):
        #Create an empty list of marbles
        marble = []
        #Set the first position of the list to contain the degree of the marble
        marble.append(i*spreader)
        #Get a random rgb color
        color =((random.randint(0, 255)),(random.randint(0, 255)),(random.randint(0, 255)))
        #Set the color to the second position in the list
        marble.append(color)
        #Append the marble to the marbel list
        marbList.append(marble)
        
        
    #Give the marbles different starting points on a line along the circle
    def get_pos(marble):
        marbList = []
        marbList.append(int(middle[0] + circRadius*math.sin(math.radians(marble))))
        marbList.append(int(middle[1] - circRadius*math.cos(math.radians(marble))))
        return(marbList)
    
    #Starting a display loop
    z = ""
    count = 0
    while __name__=="__main__":
        #Render a white background
        screen.fill((255,255,255))
        #Draw a circle that the marbles will travel along
        pygame.draw.circle(screen, (0,0,0),middle,circRadius,1)
        #Draw the list of marbles
        for marble in marbList:
            posList = get_pos(marble[0])
            pygame.draw.circle(screen, marble[1],(posList[0],posList[1]),marbR)
        #Flip the screen
        pygame.display.flip()
        #Set the speed depending on the count
        speed = 0.2*math.sin(count/10000)
        #This is the speed for the last marble in the list
        marbList[-1][0] += abs(speed)
        #This is the speed for every marble including the last marble in the list
        for marble in marbList:
            marble[0] -= speed
        #Increase the count by one
        count += 1
        ##Calculate the euclidian distance between the first and the last marble in the list
        #Get the position of the first marble in the list
        posFirst = get_pos(marbList[0][0])
        #Get the position of the last marble in the list
        posLast = get_pos(marbList[-1][0])
        #Calculate the distance between the first and the last marble in the list 
        eucDistance = math.sqrt(math.pow(posFirst[0]-posLast[0],2)+math.pow(posFirst[1]-posLast[1],2))
        #If euclidian distance is equal or less than two radians, change the last marble to be the first
        if int(eucDistance) <= marbR*2:
            marbList.insert(0, marbList.pop())
        #keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #Escape will quit the program
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
