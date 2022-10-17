from threading import Timer
from tracemalloc import start
import pygame

pygame.init() # a must thing

# set the size of display
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# title set
pygame.display.set_caption('Hello Daeyoung')

# setting the background
background = pygame.image.load('D:\\Python\\Nado_Coding\\pygame_basic\\background.png')
# open that image file and right click, copy path and paste
# to make the python determine \, add additional \. like \\, / is possible instead.


# creating character

character = pygame.image.load('D:\\Python\\Nado_Coding\\pygame_basic\\character.png')
character_size = character.get_rect().size # get the size of original image. rectangle
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/3*1.3
character_y_pos = screen_height/2*1.6

# location to move
to_x = 0
to_y = 0


# event roop - to keep the display up there
running = True # to check if the game is running

while running :
    for event in pygame.event.get() : # to make a roop, this is a must thing to set up
        if event.type == pygame.QUIT : # to check if the window is closed
            running = False
        
        if event.type == pygame.KEYDOWN : # to check if the key is pressed
            if event.key == pygame.K_LEFT : # to move the character to the left
                to_x -= .5
            elif event.key == pygame.K_RIGHT : # to move the character to the right
                to_x += .5
            elif event.key == pygame.K_UP : # to move the character toward up
                to_y -= .5
            elif event.key == pygame.K_DOWN : # to move the character toward down
                to_y += .5
        
        if event.type == pygame.KEYUP : # to check if the key is not pressed
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # set a limit of movement on X position.
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width
    # set a limit of movement on Y position.
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height :
        character_y_pos = screen_height-character_height
 
    screen.blit(background,(0,0)) # add background information
    
    screen.blit(character, (character_x_pos,character_y_pos)) # character create 
        screen.blit(character, (character_x_pos,character_y_pos)) # character create 
    screen.blit(character, (character_x_pos,character_y_pos)) # character create 
    
    
    
    pygame.display.update() # to update the display on every single frame.
# exit pygame

pygame.quit()