import pygame
import sys
pygame.init()

#initalizing screen and setting icon
screen_width, screen_height = 480, 360
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pingoal")
pygame.display.set_icon(pygame.image.load("assets/icon_.png"))

def play_window():
     while True:
          screen.fill("BLACK")
          bg = pygame.image.load("assets/menu.png")
          bg = pygame.transform.scale(bg, (screen_width+260,180+ screen_height))
          screen.blit(bg,(-130,-80))

          for event in pygame.event.get():
               if event.type == pygame.QUIT: #cross button event function
                    running=False
                    pygame.quit()
                    sys.exit()


def main_menu():
     running=True
     while running:
     #iniatilizing images, assets
          bg = pygame.image.load("assets/menu.png")
          bg = pygame.transform.scale(bg, (screen_width+260,180+ screen_height))

          #checking for events
          screen.blit(bg,(-130,-80))
          for event in pygame.event.get():
               if event.type == pygame.QUIT: #cross button event function
                    running=False
                    pygame.quit()
                    sys.exit()
                    
          

          pygame.display.update()
          
main_menu()

