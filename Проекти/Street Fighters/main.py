
import pygame
import os
import player_standing
import player_crouch
import player_forward
import player_jump
import player_punching
import player_kicking

HEIGHT = 550
WIDTH = 1200
FPS = 60

# SCREEEN___________________________________________________________________________________________________________________________________________

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("STREET FIGHTERS")

# ICON______________________________________________________________________________________________________________________________________________

ICON = pygame.image.load(os.path.join("Assets", "logo2.png"))
pygame.display.set_icon(ICON)

# BACKGROUND________________________________________________________________________________________________________________________________________

BACKGROUND = pygame.image.load(os.path.join("Assets", "background.jpg"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (1200, 600))

x_1 = 142
y_1 = 350

x_2 = 950
y_2 = 350

vel = 5

isJump = False
isCrouch = False
isPunch = False
isKick = False
jumpCount = 10

width = 142
height = 149

left = False
right = False
walkCount = 0

# PLAYER_1__________________________________________________________________________________________________________________________________________

Standing_1 = pygame.image.load(os.path.join(
    "Assets", "StreetFighter.png")).convert_alpha()
Standing_1 = pygame.transform.scale(Standing_1, (940, 1515))

Forward_1 = pygame.image.load(os.path.join(
    "Assets", "StreetFighter.png")).convert_alpha()
Forward_1 = pygame.transform.scale(Forward_1, (940, 1494))

Left_1 = pygame.image.load(os.path.join(
    "Assets", "StreetFighter_2.png")).convert_alpha()
Left_1 = pygame.transform.scale(Left_1, (950, 1494))

Crouch_1 = pygame.image.load(os.path.join(
    "Assets", "StreetFighter.png")).convert_alpha()
Crouch_1 = pygame.transform.scale(Crouch_1, (940, 1488))

Jump_1 = pygame.image.load(os.path.join(
    "Assets", "StreetFighter.png")).convert_alpha()
Jump_1 = pygame.transform.scale(Jump_1, (940, 1490))

Punch_1 = pygame.image.load(os.path.join(
    "Assets", "StreetFighter.png")).convert_alpha()
Punch_1 = pygame.transform.scale(Punch_1, (940, 1505))

Kick_1 = pygame.image.load(os.path.join(
    "Assets", "StreetFighter.png")).convert_alpha()
Kick_1 = pygame.transform.scale(Kick_1, (970, 1490))

#PLAYER_2___________________________________________________________________________________________________________________________________________

Standing_2 = pygame.image.load(os.path.join(
    "Assets", "StreetFighter_2.png")).convert_alpha()
Standing_2 = pygame.transform.scale(Standing_2, (950, 1515))

Forward_2 = pygame.image.load(os.path.join(
    "Assets", "StreetFighter_2.png")).convert_alpha()
Forward_2 = pygame.transform.scale(Forward_2, (950, 1494))

Crouch_2 = pygame.image.load(os.path.join(
    "Assets", "StreetFighter_2.png")).convert_alpha()
Crouch_2 = pygame.transform.scale(Crouch_2, (950, 1488))

Jump_2 = pygame.image.load(os.path.join(
    "Assets", "StreetFighter_2.png")).convert_alpha()
Jump_2 = pygame.transform.scale(Jump_2, (944, 1490))


# SPRITE_MOVEMENTS__________________________________________________________________________________________________________________________________

Sprite_player_1_1 = player_standing.SpriteSheet_1(Standing_1)
Sprite_player_1_2 = player_forward.SpriteSheet_2(Forward_1)
Sprite_player_1_3 = player_forward.SpriteSheet_6(Left_1)
Sprite_player_1_4 = player_crouch.SpriteSheet_3(Crouch_1)
Sprite_player_1_5 = player_jump.SpriteSheet_4(Jump_1)
Sprite_player_1_6 = player_punching.SpriteSheet_9(Punch_1)
Sprite_player_1_7 = player_kicking.SpriteSheet_11(Kick_1)

Sprite_player_2_1 = player_standing.SpriteSheet_5(Standing_2)
Sprite_player_2_2 = player_forward.SpriteSheet_6(Forward_2)
Sprite_player_2_3 = player_crouch.SpriteSheet_7(Crouch_2)
Sprite_player_2_4 = player_jump.SpriteSheet_8(Jump_2)

BLACK = (0, 0, 0)

animation_list = []

animation_steps = [4, 3, 3, 1, 7, 3, 5]
action = 0

animation_cooldown = 75
frame = 0

step_counter = 0
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
counter_6 = 0
counter_7 = 0

clock = pygame.time.Clock()
last_update_1 = pygame.time.get_ticks()
last_update_2 = pygame.time.get_ticks()
last_update_3 = pygame.time.get_ticks()
last_update_4 = pygame.time.get_ticks()
last_update_5 = pygame.time.get_ticks()
last_update_6 = pygame.time.get_ticks()
last_update_7 = pygame.time.get_ticks()

animation_list_standing = []
animation_list_right = []
animation_list_left = []
animation_list_crouch = []
animation_list_jump = []
animation_list_punch = []
animation_list_kick = []

for animation in animation_steps:

    step_counter = 0
    for _ in range(0 , 4):
        animation_list_standing.append(Sprite_player_1_1.Animation_Player_One_First(step_counter, width, height, BLACK))
        step_counter += 1

    step_counter = 0  
    for _ in range(0, 3):
        animation_list_right.append(Sprite_player_1_2.Animation_Player_One_Second(step_counter, width, height, BLACK))
        step_counter += 1

    step_counter = 0   
    for _ in range(0, 4):
        animation_list_left.append(Sprite_player_1_3.Animation_Player_Two_Second(step_counter, width, height, BLACK))
        step_counter += 1

    step_counter = 0   
    for _ in range(animation):
        animation_list_crouch.append(Sprite_player_1_4.Animation_Player_One_Third(step_counter, width, height, BLACK))
        step_counter += 1

    step_counter = 0 
    for _ in range(animation):
        animation_list_jump.append(Sprite_player_1_5.Animation_Player_One_Forth(step_counter, width, height, BLACK))
        step_counter += 1

    step_counter = 0 
    for _ in range(0 , 3):
        animation_list_punch.append(Sprite_player_1_6.Animation_Player_One_Fifth(step_counter, width, height, BLACK))
        step_counter += 1

    step_counter = 0 
    for _ in range(0 , 5):
        animation_list_kick.append(Sprite_player_1_7.Animation_Player_One_Sixth(step_counter, width, height, BLACK))
        step_counter += 1

    animation_list.append(animation_list_standing)
    animation_list.append(animation_list_right)
    animation_list.append(animation_list_left)
    animation_list.append(animation_list_crouch)
    animation_list.append(animation_list_jump)
    animation_list.append(animation_list_punch)
    animation_list.append(animation_list_kick)

def redrawGameWindow(counter_1, counter_2, counter_3, counter_4, counter_5, counter_6, counter_7, x_1, y_1):
    global walkCount

    SCREEN.blit(BACKGROUND, (0, 0))
        
    if left:
        SCREEN.blit(animation_list_left[counter_3], (x_1, y_1))

    elif right:
        SCREEN.blit(animation_list_right[counter_2], (x_1, y_1))

    elif isCrouch:
        SCREEN.blit(animation_list_crouch[counter_4], (x_1, y_1))

    elif isJump:
        SCREEN.blit(animation_list_jump[counter_5], (x_1, y_1))

    elif isPunch:
        SCREEN.blit(animation_list_punch[counter_6], (x_1, y_1))

    elif isKick:
        SCREEN.blit(animation_list_kick[counter_7], (x_1, y_1))

    else:
        SCREEN.blit(animation_list_standing[counter_1], (x_1, y_1))


    pygame.display.update()

run = True
while run:
    clock.tick(FPS)
    
    # update_animation_1____________________________________________________________________________________________
    current_time = pygame.time.get_ticks()
    
    if current_time - last_update_1 >= animation_cooldown:
        counter_1 += 1
        last_update_1 = current_time
        if counter_1 >= len(animation_list_standing):
            counter_1 = 0

    if current_time - last_update_2 >= animation_cooldown:
        counter_2 += 1
        last_update_2 = current_time
        if counter_2 >= len(animation_list_right):
            counter_2 = 0

    if current_time - last_update_3 >= animation_cooldown:
        counter_3 += 1
        last_update_3 = current_time
        if counter_3 >= len(animation_list_left):
            counter_3 = 0

    if current_time - last_update_5 >= animation_cooldown:
        counter_5 += 1
        last_update_5 = current_time
        if counter_5 >= len(animation_list_jump):
            counter_5 = 0
   
    if current_time - last_update_6 >= animation_cooldown:
        counter_6 += 1
        last_update_6 = current_time
        if counter_6 >= len(animation_list_punch):
            counter_6 = 0

    if current_time - last_update_7 >= animation_cooldown:
        counter_7 += 1
        last_update_7 = current_time
        if counter_7 >= len(animation_list_kick):
            counter_7 = 0
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and x_1 > vel: 
        x_1 -= vel
        left = True
        right = False

    elif keys[pygame.K_d] and x_1 < 1250 - vel - width:  
        x_1 += vel
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0
    
    if keys[pygame.K_s]:  
        left = False
        right = False
        isCrouch = True
        walkCount = 0
    else:
        isCrouch = False
        walkCount = 0

    if keys[pygame.K_f]:  
        left = False
        right = False
        isPunch = True
        walkCount = 0
    else:
        isPunch = False     
        walkCount = 0
    
    if keys[pygame.K_q]:  
        left = False
        right = False
        isKick = True
        walkCount = 0
    else:
        isKick = False     
        walkCount = 0
        
    if not(isJump): 
        if keys[pygame.K_w]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= - 10:
            y_1 -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1

        else: 
            jumpCount = 10
            isJump = False

    redrawGameWindow(counter_1, counter_2, counter_3, counter_4, counter_5, counter_6, counter_7, x_1, y_1) 
        
    pygame.display.update()
pygame.quit()
