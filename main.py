import pygame
import os
import random
# from function import gravity

pygame.init() 
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

# creating our main character

character = pygame.image.load(os.path.join(game_dir, "character.png")).convert()
character_size = character.get_rect().size # get the size of original image. rectangle
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/3*1.3
character_y_pos = screen_height/2*1.75

# location to move our main character
to_x = 0
to_y = 0

# salad object 1

salad = pygame.image.load(os.path.join(game_dir, "salad.png")).convert()
salad_size = salad.get_rect().size # get the size of original image. rectangle
salad_width = salad_size[0]
salad_height = salad_size[1]
salad_x_pos = random.randint(0,screen_width-salad_width)
salad_y_pos = 0
salad_new_y_pos = 0

# salad object 2

salad2 = pygame.image.load(os.path.join(game_dir, "salad.png")).convert()
salad2_size = salad2.get_rect().size # get the size of original image. rectangle
salad2_width = salad2_size[0]
salad2_height = salad2_size[1]
salad2_x_pos = random.randint(0,screen_width-salad2_width)
salad2_y_pos = 0
salad2_new_y_pos = 0

# chicken object 1

chicken_breast = pygame.image.load(os.path.join(game_dir, "chickenBreast.png")).convert()
chicken_breast_size = chicken_breast.get_rect().size # get the size of original image. rectangle
chicken_breast_width = chicken_breast_size[0]
chicken_breast_height = chicken_breast_size[1]
chicken_breast_x_pos = random.randint(0,screen_width-chicken_breast_width)
chicken_breast_y_pos = 0
chicken_breast_new_y_pos = 0

# chicken object 2

chicken_breast2 = pygame.image.load(os.path.join(game_dir, "chickenBreast.png")).convert()
chicken_breast2_size = chicken_breast2.get_rect().size # get the size of original image. rectangle
chicken_breast2_width = chicken_breast2_size[0]
chicken_breast2_height = chicken_breast2_size[1]
chicken_breast2_x_pos = random.randint(0,screen_width-salad_width)
chicken_breast2_y_pos = 0
chicken_breast2_new_y_pos = 0

# cake object

cake = pygame.image.load(os.path.join(game_dir, "cake.png")).convert()
cake_size = cake.get_rect().size # get the size of original image. rectangle
cake_width = cake_size[0]
cake_height = cake_size[1]
cake_x_pos = random.randint(0,screen_width - cake_width)
cake_y_pos = 0
cake_new_y_pos = 0

# icecream object

icecream =  pygame.image.load(os.path.join(game_dir, "icecream.png")).convert()
icecream_size = icecream.get_rect().size # get the size of original image. rectangle
icecream_width = icecream_size[0]
icecream_height = icecream_size[1]
icecream_x_pos = random.randint(0,screen_width - icecream_width)
icecream_y_pos = 0
icecream_new_y_pos = 0


default_speed = 0.6
main_char_coefficient = .5
clock = pygame.time.Clock()

# font information
game_font = pygame.font.Font(None, 40) # font ojbect (font, size)

# start time record
start_ticks = pygame.time.get_ticks() # in ms (1 sec = 1000 ms)

running = True 
while running :
    
    if main_char_coefficient < 0:
        running = False

    dt = clock.tick(60)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : # to check if the window is closed
            running = False
        
        if event.type == pygame.KEYDOWN : # to check if the key is pressed
            if event.key == pygame.K_LEFT : # to move the character to the left
                to_x -= default_speed * main_char_coefficient
            elif event.key == pygame.K_RIGHT : # to move the character to the right
                to_x += default_speed * main_char_coefficient
        
        if event.type == pygame.KEYUP : # to check if the key is not pressed
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    salad_new_y_pos += default_speed*5
    chicken_breast_new_y_pos += default_speed*7
    cake_new_y_pos += default_speed*6
    icecream_new_y_pos += default_speed*7

    # updating main character's actual position
    character_position = character.get_rect()
    character_position.left = character_x_pos
    character_position.top = character_y_pos

    # updating salad's actual position
    salad_position = salad.get_rect()
    salad_position.left = salad_x_pos
    salad_position.top = salad_new_y_pos

    # updating chicken breast's actual position
    chicken_breast_position = chicken_breast.get_rect()
    chicken_breast_position.left = chicken_breast_x_pos
    chicken_breast_position.top = chicken_breast_new_y_pos

    # updating cake's actual position
    cake_position = cake.get_rect()
    cake_position.left = cake_x_pos
    cake_position.top = cake_new_y_pos

    # updating icecream's actual position
    icecream_position = icecream.get_rect()
    icecream_position.left = icecream_x_pos
    icecream_position.top = icecream_new_y_pos

    # collsion event
    if salad_position.colliderect(character_position):
        print("Yummy!")
        main_char_coefficient += 0.1
        salad_new_y_pos = 640
    if chicken_breast_position.colliderect(character_position):
        print("Yum! Yummy!")
        main_char_coefficient += 0.2
        chicken_breast_new_y_pos = 640
    if cake_position.colliderect(character_position):
        print("Even more yummy!!")
        main_char_coefficient -= 0.2    
        cake_new_y_pos = 640
    if icecream_position.colliderect(character_position):
        print("Omg I love it!")
        main_char_coefficient -= 0.15    
        icecream_new_y_pos = 640

    # salad_new_y_pos = gravity(salad_new_y_pos)
    if(salad_new_y_pos >= 640):
        salad_new_y_pos = 0
        salad_x_pos = random.randint(0,screen_width-salad_width)

    if(chicken_breast_new_y_pos >= 640):
        chicken_breast_new_y_pos = 0
        chicken_breast_x_pos = random.randint(0,screen_width- chicken_breast_width)

    if(cake_new_y_pos >= 640):
        cake_new_y_pos = 0
        cake_x_pos = random.randint(0,screen_width - cake_width)

    if(icecream_new_y_pos >= 640):
        icecream_new_y_pos = 0
        icecream_x_pos = random.randint(0,screen_width - icecream_width)

    # set a limit of movement on X position.
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width


    screen.blit(background,(0,0)) # add background information
    
    screen.blit(salad, (salad_x_pos,salad_new_y_pos))
    screen.blit(chicken_breast, (chicken_breast_x_pos,chicken_breast_new_y_pos))
    screen.blit(cake, (cake_x_pos,cake_new_y_pos))
    screen.blit(icecream, (icecream_x_pos, icecream_new_y_pos))
    screen.blit(character, (character_x_pos,character_y_pos)) # character create 
    
    
    pygame.display.update() # to update the display on every single frame.
# exit pygame

pygame.quit()