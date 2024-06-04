import pygame
import random
import time
import sys
#==========================================================================================#
#                                   Constants Used                                         #  
#==========================================================================================#
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

#Below we define the number of rooms with the following: Arrows, Bats, and Pits
NUM_BATS = 2
NUM_PITS = 2
NUM_ARROWS = 0

player_pos = 1 #Which room we are in
wumpus_pos = 0 #Wumpus Location
num_arrows = 1 #Arrows we have
mobile_wumpus = False #If False, Wumpus stays put otherwise moves
wumpus_move_chance = 50 #50-50 probability that wumpus moves

#Constants for Direction for sake of simplicity 
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

#Defined Colors for Game
BLUE = 0,0,225
WHITE = 255, 255, 255
RED = 138, 7, 7

#Cave System (0 represents no path)
cave = {1 : [0, 8, 2, 5], 2 : [0, 10, 3, 1], 3 : [0, 12, 4, 2], 4 : [0, 14, 5, 3], 5 : [0, 6, 1, 4],
        6 : [5, 0, 7, 15], 7 : [0, 17, 8, 6], 8 : [1, 0, 9, 7], 9 : [0, 18, 10, 8], 10 : [2, 0, 11, 9],
        11 : [0, 19, 12, 10], 12 : [3, 0, 13, 11], 13 : [0, 20, 14, 12], 14 :[4, 0, 15, 13], 15 : [0, 16, 6, 14],
        16 : [15, 0, 17, 20], 17 : [7, 0, 18, 16], 18 : [9, 0, 19, 17], 19 : [11, 0, 20, 18], 20 : [13, 0, 16, 19]}

#Mobs and Arrow Locations
bats_list = []
pits_list = []
arrows_list = []

#==========================================================================================#
#                                    Methods Used                                          #  
#==========================================================================================#

#room creation in background process
def draw_room(pos, screen):
        x = 0
        y= 1
        exits = cave[player_pos]
        screen.fill((0,0,0)) #paint black background
        
        #draw a room circle in White
        circleRadius = int((SCREEN_WIDTH//2) * 0.75)
        pygame.draw.circle(screen, WHITE, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), circleRadius, 0)
        
        #draw exits from room
        if exits[LEFT] > 0:
                left = 0
                top = SCREEN_HEIGHT//2-40
                pygame.draw.rect(screen, WHITE, ((left, top), (SCREEN_WIDTH//4, 80)), 0)

        if exits[RIGHT] > 0:
                left = SCREEN_WIDTH-(SCREEN_WIDTH//4)
                top = SCREEN_HEIGHT//2-40
                pygame.draw.rect(screen, WHITE, ((left, top), (SCREEN_WIDTH//4, 80)), 0)
        if exits[UP] > 0:
                left = SCREEN_HEIGHT//2-40
                top = 0
                pygame.draw.rect(screen, WHITE, ((left, top), (80, SCREEN_WIDTH//4)), 0)
        if exits[DOWN] > 0:
                left = SCREEN_HEIGHT//2-40
                top = SCREEN_WIDTH-(SCREEN_WIDTH//4)
                pygame.draw.rect(screen, WHITE, ((left, top), (80, SCREEN_WIDTH//4)), 0)
        #draw text
        
        

def printInstructions():
        print(
    '''
        Quest of the Crystal Caverns
        
        [I too lazy to add instructions]
        ''')

def resetGame():
        global num_arrows
        #populateCave()
        num_arrows = 1
def checkPygameEvents():
        global player_pos
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_LEFT:
                        if cave[player_pos][LEFT] > 0:
                                player_pos = cave[player_pos][LEFT]
                elif event.key == pygame.K_RIGHT:
                        if cave[player_pos][RIGHT] > 0:
                                player_pos = cave[player_pos][RIGHT]
                elif event.key == pygame.K_UP:
                        if cave[player_pos][UP] > 0:
                                player_pos = cave[player_pos][UP]
                elif event.key == pygame.K_DOWN:
                        if cave[player_pos][DOWN] > 0:
                                player_pos = cave[player_pos][DOWN]
                

#==========================================================================================#
#                                   Initialization                                         #  
#==========================================================================================#
printInstructions()
input("Press Enter")

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption("Hunt the Wumpus")

#set up our font
font = pygame.font.Font(None, 36)
resetGame()


#==========================================================================================#
#                        Main Game Loop                                                    #
#==========================================================================================#
while True:
        checkPygameEvents()
        draw_room(player_pos, screen)
        pygame.display.flip()
