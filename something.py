from cgi import print_directory
import pygame,sys
from pygame.locals import *




SCREEN = 400
catx=10
caty=10
screen=10

def quitWin():
    pygame.quit()
    sys.exit(0)

def check_inputs(events):
    global catx,caty,screen
    for event in events:
        if event.type == QUIT:
            quit()
        elif event.type == KEYUP:
            if event.type == KEYDOWN:        
                if event.type == K_ESCAPE:
                    quitWin()
                elif event.key == K_LEFT:
                    catx -=5
                    print("Move Rect left")
                elif event.key == K_RIGHT:
                    catx += 5
                    print("Move Rect right")
                else:
                    print(event.key)    
        else:
            if event.type == KEYDOWN:        
                if event.type == K_ESCAPE:
                    quitWin()
                elif event.key == K_LEFT:
                    catx -=5
                    print("Move Rect left")
                elif event.key == K_RIGHT:
                    catx += 5
                    print("Move Rect right")
                else:
                    print(event.key)
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),(catx,50,50,10))
    pygame.display.update()

def main():
    global screen
    #initializing Gaming Sequence
    pygame.init()
    #setting up screen  
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 480
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('pING-pONG--Sutirtha')
    screen = pygame.display.get_surface()

    pygame.display.update()

    while True:
        check_inputs(pygame.event.get())

main()   

