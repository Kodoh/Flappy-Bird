#Wings now move 
import pygame
from Classes import Bird
from Classes import FlappyBird
from Classes import pipes
from Classes import pipeBottom
from Classes import pipeTop
from Classes import floor
from Classes import Bottom 
#from Classes import BirdUp  
import random
import time


pygame.init()
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
GREY = ( 128,128,128)
DGREEN = ( 34,139,34)
YELLOW = (255,255,0)
BLUE = (100, 100, 255)
PURPLE = (255, 0, 255)


colorList = (RED, GREEN, PURPLE, YELLOW, DGREEN, BLUE, BLACK, WHITE)
font = pygame.font.Font("freesansbold.ttf",32)  
background = pygame.image.load("Background.png")
score_value = 0
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load("BirdIcon.png")
pygame.display.set_icon(icon)
carryOn = True
speed = 1.3         
all_sprites_list = pygame.sprite.Group() 
PlayerBird1 = FlappyBird("Bird2.png")
PlayerBird1.rect.x = 160  
PlayerBird1.rect.y = 200 
all_Top_pipes = pygame.sprite.Group()
all_Bottom_pipes = pygame.sprite.Group()

k = random.randint(50,100)
j = random.randint(50,100)
numTop =  (k + 100)

TopPipe = pipeTop(500,(100 + k) , 70)
TopPipe.rect.x = 710                                         
TopPipe.rect.y = -25
TopPipe2 = pipeTop(500, 220, 70)
TopPipe2.rect.x = 1000
TopPipe2.rect.y = -105
bottom = Bottom(1000, 100)
bottom.rect.x = -10
bottom.rect.y = 450  
BottomPipe = pipeBottom(500,(500 - numTop), 70)
BottomPipe.rect.x = 710 
BottomPipe.rect.y = 380
BottomPipe2 = pipeBottom(500,250, 70)
BottomPipe2.rect.x = 1000
BottomPipe2.rect.y = 300
all_sprites_list.add(PlayerBird1)
all_sprites_list.add(BottomPipe)
all_Bottom_pipes.add(BottomPipe)
all_sprites_list.add(TopPipe)
all_Top_pipes.add(TopPipe)
all_Bottom_pipes.add(BottomPipe2)
all_sprites_list.add(BottomPipe2)
all_Top_pipes.add(TopPipe2)
all_sprites_list.add(TopPipe2)
all_sprites_list.add(bottom)

def show_score(x,y):
    score = font.render("Score : " + str(score_value),True, (252,133,153))
    screen.blit(score, (x,y))

clock = pygame.time.Clock()
while carryOn:      
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            carryOn = False 
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:      
                carryOn=False
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_SPACE]:
        PlayerBird1.moveUp(5)
    else:                  
        PlayerBird1.moveDown(3)  
    for pipe in all_Top_pipes:    
        pipe.moveForward(speed)
        if pipe.rect.x < -100:
            t = (random.choice((1, -1))*random.randint(50, 100))
            pipe.rect.x = 650
            pipe.rect.y = -100 + t
        if pipe.rect.x < 160 and pipe.rect.x > 153:
            score_value += 1
    for pipe in all_Bottom_pipes: 
        pipe.moveForward(speed)
        if pipe.rect.x < -100:
            pipe.rect.x = 650
            pipe.rect.y = 300 + t
    pipe_top_collision_list = pygame.sprite.spritecollide(PlayerBird1,all_Top_pipes,False)
    for pipe in pipe_top_collision_list:
        print("Bird died!")
        #End Of Game
        carryOn=False
    pipe_bottom_collision_list = pygame.sprite.spritecollide(PlayerBird1,all_Bottom_pipes,False)
    for pipe in pipe_bottom_collision_list:
        print("Bird died!")
        carryOn = False
    if PlayerBird1.rect.y > 407:
        print("Bird died!")   
        carryOn = False
    if PlayerBird1.rect.y <= -60:
        PlayerBird1.rect.y = -50             
    all_sprites_list.update() 
    screen.fill(WHITE)
    screen.blit(background, (0,0))
    all_sprites_list.draw(screen)
    show_score(10,10 )
    pygame.display.flip()
    clock.tick(60)
print("Your score is ", score_value)   
pygame.quit()


