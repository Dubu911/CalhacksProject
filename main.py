import pygame
import os
import random
from function import gravity

pygame.init() # a must thing

# set the size of display
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# title set
pygame.display.set_caption('Wellcome to the weird game')

# setting the background
game_dir = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(game_dir, "background.png")).convert()
# to make the python determine \, add additional \. like \\, / is possible instead.


# creating character

character = pygame.image.load(os.path.join(game_dir, "character.png")).convert()
character_size = character.get_rect().size # get the size of original image. rectangle
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/3*1.3
character_y_pos = screen_height/2*1.75

# location to move for character
to_x = 0
to_y = 0

salad = pygame.image.load(os.path.join(game_dir, "salad.png")).convert()
salad_size = character.get_rect().size # get the size of original image. rectangle
salad_width = salad_size[0]
salad_height = salad_size[1]
salad_x_pos = random.randint(0,screen_width-salad_width)
salad_y_pos = 0
salad_new_y_pos = 0

# event roop - to keep the display up there
running = True # to check if the game is running

while running :
    for event in pygame.event.get() : # to make a roop, this is a must thing to set up
        if event.type == pygame.QUIT : # to check if the window is closed
            running = False
        
        if event.type == pygame.KEYDOWN : # to check if the key is pressed
            if event.key == pygame.K_LEFT : # to move the character to the left
                to_x -= .3
            elif event.key == pygame.K_RIGHT : # to move the character to the right
                to_x += .3
        
        if event.type == pygame.KEYUP : # to check if the key is not pressed
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            # elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
            #     to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y
    # salad_new_y_pos += gravity(salad_new_y_pos)
    salad_new_y_pos = gravity(salad_new_y_pos)
    if(salad_new_y_pos >= 640):
        salad_new_y_pos = 0
        salad_x_pos = random.randint(0,screen_width-salad_width)


    if(salad_new_y_pos + salad_height/2 == character_y_pos \
        and (salad_x_pos > character_x_pos or salad_x_pos < character_x_pos + character_width)) :
        running = False


    # set a limit of movement on X position.
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width
    

    screen.blit(background,(0,0)) # add background information
    
    screen.blit(salad, (salad_x_pos,salad_new_y_pos))
    screen.blit(character, (character_x_pos,character_y_pos)) # character create 
    
    
    pygame.display.update() # to update the display on every single frame.
# exit pygame

pygame.quit()