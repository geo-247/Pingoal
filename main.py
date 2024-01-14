import pygame
import sys
from button import Button  

pygame.init()

screen_width, screen_height = 480, 360
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pongoal")
pygame.display.set_icon(pygame.image.load("assets/icon_.png"))

def play_window():
    while True:
        screen.fill("BLACK")
        bg = pygame.image.load("assets/bg.png")
        bg = pygame.transform.scale(bg, (screen_width + 260, 180 + screen_height))
        screen.blit(bg, (-130, -80))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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
