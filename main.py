# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while (1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        print("A")
        screen.fill(color=(255,255,255))
        #pygame.display.flip()
    
if __name__ == "__main__":
    main()