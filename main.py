import pygame
pygame.init()

#initalizing screen and setting icon
screen_width, screen_height = 480, 360
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pingoal")
pygame.display.set_icon(pygame.image.load("assets/icon_.png"))
running=True

#iniatilizing images, assets
bg = pygame.image.load("assets/menu.png")
bg = pygame.transform.scale(bg, (screen_width+260,180+ screen_height))
while running:
  
     #checking for events
     screen.blit(bg,(-130,-80))
     for event in pygame.event.get():
          if event.type == pygame.QUIT: #cross button event function
               running=False
     pygame.display.update()

pygame.quit()
