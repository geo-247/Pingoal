import pygame
import sys
import math
from button import Button  

pygame.init()

screen_width, screen_height = 480, 360
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pongoal")
pygame.display.set_icon(pygame.image.load("assets/icon_.png"))

def is_collision(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x1 - x2, 2) + (math.pow(y1 - y2, 2))) #applying distance formula
    if distance < 27:
        return True
    else:
        return False
def player(x,y,playerImg):
    resized_playerImg = pygame.transform.scale(playerImg, (30, 90))
    screen.blit(resized_playerImg,(x,y))
def drawCs(x,y,cs):
    resized_playerImg = pygame.transform.scale(cs, (30, 90))
    screen.blit(resized_playerImg,(x,y))


def play_window():
    #player
    playerImg = pygame.image.load("assets/player.png")
    playerX,playerY = 70,100
    #cs
    csImg = pygame.image.load("assets/enemy.png")
    csX,csY = 390,100
    
    while True:
        mouseX,mouseY = pygame.mouse.get_pos()
        playerY = mouseY #playerY movement is done with the mouse

        if playerY <= 30: #limiting Y axis movement
            playerY = 30
        elif playerY >= 250:
            playerY = 250


        screen.fill("BLACK")
        bg = pygame.image.load("assets/bg.png")
        bg = pygame.transform.scale(bg, (screen_width + 260, 180 + screen_height))
        screen.blit(bg, (-130, -80))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player(playerX,playerY,playerImg)#drawing player
        drawCs(csX,csY,csImg)#drawing enemy
        pygame.display.update()

def main_menu():
    running = True
    button_size = (100, 100)  

    play_button = Button(
        image=pygame.transform.scale(pygame.image.load("assets/play.png"), button_size),
        pos=(250,250),
        text_input="",
        font=pygame.font.Font(None, 36),
        base_color=(255, 255, 255),
        hovering_color=(150, 150, 150),
    )


    while running:
        screen.fill("BLACK")
        bg = pygame.image.load("assets/menu.png")
        bg = pygame.transform.scale(bg, (screen_width + 260, 180 + screen_height))
        screen.blit(bg, (-130, -80))

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
