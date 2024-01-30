import pygame
import sys
import math
from random import *
from button import Button
import threading, time

pygame.init()
       

screen_width, screen_height = 480, 360
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong goal")
pygame.display.set_icon(pygame.image.load("assets/icon_.png"))



def isCollision(x1, y1, x2, y2, width1, height1, width2, height2):
    rect1 = pygame.Rect(x1, y1, width1, height1)
    rect2 = pygame.Rect(x2, y2, width2, height2)
    return rect1.colliderect(rect2)

def player(x, y, playerImg):
    resized_playerImg = pygame.transform.scale(playerImg, (30, 90))
    screen.blit(resized_playerImg, (x, y))

def drawCs(x, y, cs):
    resized_cs = pygame.transform.scale(cs, (30, 90))
    screen.blit(resized_cs, (x, y))

def drawBall(x, y, cs):
    resized_ball = pygame.transform.scale(cs, (40, 40))
    screen.blit(resized_ball, (x, y))

def reset_collision_thread():
    global reset_collision
    while True:
        time.sleep(0.3)
        reset_collision = True

def play_window():
#fonts
    f1 = pygame.font.Font("assets\CartoonTown.ttf",45)
    def displayText(text,x,y):
        global screen
        
        myText= f1.render(text, True, "black")
        screen.blit(myText,[x,y])
    global reset_collision
    # player
    playerImg = pygame.image.load("assets/player.png")
    playerX, playerY = 70, 100
    # cs
    csImg = pygame.image.load("assets/enemy.png")
    csX, csY = 390, 100

    # ball
    ballImg = pygame.image.load("assets/ball.png")
    ballX, ballY = screen_width // 2, screen_height // 2
    csYChange = 0
    speed=1.5

    angle = uniform(30, 150)  # Use uniform for a continuous range
    scoreP, scoreC = 0, 0
    while True:

     
        mouseX, mouseY = pygame.mouse.get_pos()
        playerY = mouseY  # playerY movement is done with the mouse

        if playerY <= 30:  # limiting Y axis movement
            playerY = 30
        elif playerY >= 250:
            playerY = 250

        # Movement of the enemy
        if ballY > csY:
            csYChange = 1
        else:
            csYChange = -1

        # Limiting enemy Y axis movement
        if csY <= 30:
            csY = 30
        elif csY >= 250:
            csY = 250
    
        #scoring 
        if ballX <= 0 and (ballY>=30 and ballY<=250):
            ballX, ballY = screen_width // 2, screen_height // 2
            scoreC += 1
            print("\nComputer Scored")
            displayText("Computer Scored !",70 , 0)
         
            pygame.display.update()

            time.sleep(2)
        elif ballX >= screen_width and (ballY>=30 and ballY<=250):
            ballX, ballY = screen_width // 2, screen_height // 2
            scoreP += 1
            print("\nPlayer Scored")
            displayText("Player Scored !",90 , 0)
       
            pygame.display.update()

            time.sleep(2)

        # Ball rebounding and angle turns
        if ballY <= 30 and reset_collision:
            angle = uniform(30, 150)
            reset_collision = False
        elif ballY >= screen_height - 40 and reset_collision:
            angle = uniform(-150, -30)
            reset_collision = False

        # Collisions logic with rebounding
        if isCollision(playerX, playerY, ballX, ballY, 30, 90, 40, 40) and reset_collision:
            angle = uniform(-150, -30)
            print("Ball , player collision detected")
            reset_collision = False
        elif isCollision(csX, csY, ballX, ballY, 30, 90, 40, 40) and reset_collision:
            angle = uniform(30, 150)
            print("Ball , enemy collision detected")
            reset_collision = False

        screen.fill((0, 0, 0))
        bg = pygame.image.load("assets/bg.png")
        bg = pygame.transform.scale(bg, (screen_width + 260, 180 + screen_height))
        screen.blit(bg, (-130, -80))
        ballX += math.cos(math.radians(angle)) * speed
        ballY += math.sin(math.radians(angle)) * speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        csY += csYChange
        player(playerX, playerY, playerImg)  # drawing player
        drawCs(csX, csY, csImg)  # drawing enemy
        drawBall(ballX, ballY, ballImg)  # drawing ball
        displayText(str(scoreP),0,150)  
        displayText(str(scoreC),screen_width-20,150)
        pygame.display.update()


def main_menu():
    reset_thread = threading.Thread(target=reset_collision_thread)
    reset_thread.daemon = True
    reset_thread.start()
    running = True
    button_size = (100, 50)

    play_button = Button(
        image=pygame.transform.scale(pygame.image.load("assets/p.png"), button_size),
        pos=(250, 300),
        text_input="",
        font=pygame.font.Font(None, 36),
        base_color=(255, 255, 255),
        hovering_color=(150, 150, 150),
    )

    while running:
        screen.fill((0, 0, 0))
        bg = pygame.image.load("assets/b.png")
        bg = pygame.transform.scale(bg, (screen_width  ,   screen_height))
        screen.blit(bg, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(pygame.mouse.get_pos()):
                    print("clicked")
                    running = False
                    play_window()

        play_button.update(screen)
        pygame.display.update()

main_menu()
