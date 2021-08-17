

import pygame
import sys
import random

pygame.init()

'''
initialize a screen-object
set screen-size for the game terminal in pixel x pixel
'''
screen_width = 800
screen_height = 600

# Player configs
player_size = 50
player_color = (255,0,0)

# In pygame world extreme top left pixel is (0,0)
# we define player position keeping that in mind
player_pos = [screen_width/2,screen_height-(2*player_size)]

# enemy configs
enemy_size = 50
enemy_color = (0,0,255)

# for falling random blocks, should start at a random position at the top
enemy_pos = [random.randint(0,screen_width-enemy_size),10]
speed = 10

#black as color
background_color = (0,0,0)

# Screen just pops-up and disappears
screen = pygame.display.set_mode((screen_width,screen_height))

#pygame is event based library
#therefore we need events to keep the game running with loops
def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
            return True
    return False

game_over = False

'''
while not(game_over):

    # pygame events capture all events like mouse movements, keystrokes etc.
    # un-comment just the print and infinite while statements to observe
    # Tools -> Cancel Build to kill the infinite loop
    # An infinite loop implies the game display screen is always open, capturing events.
    #sys.exit() needs to be configured to give user the control to shut the game by closing the display window

    for event in pygame.event.get():
        print(event)

'''

while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos[0] -= 10

            if event.key == pygame.K_RIGHT:
                player_pos[0] += 10


    # remember to reset the screen everytime the player moves else, it keeps drawing recatangles at new positions
    # while retaining the rectangles in old positions.

    screen.fill(background_color)

    # Simulate the continuously falling enemy block from random x-positions
    '''
    logic:
    once enemy is available in any random position it should keep falling down
    the block keeps falling very fast without the clock.tick()
    '''
    if enemy_pos[1] >=0 and enemy_pos[1] <= screen_height:
        enemy_pos[1]+=speed# Higher value => moves higher paces in a single move
    else:
        # reset the block back up again at a different x position
        enemy_pos[0] = random.randint(0,screen_width-enemy_size)
        enemy_pos[1] = 0



    #pygame.draw.rec(surface=screen object on which we draw, (R,G,B), left position, right position, width, height of the rect player)
    pygame.draw.rect(screen,player_color,(player_pos[0],player_pos[1],player_size,player_size))
    pygame.draw.rect(screen,enemy_color,(enemy_pos[0],enemy_pos[1],enemy_size,enemy_size))

    if detect_collision(player_pos, enemy_pos):
        game_over = True
        break


    # slow the block falling down.
    # Higher the fps, faster it is
    fps = 30
    clock = pygame.time.Clock()
    clock.tick(fps)

    #commit to screen
    pygame.display.update()
