# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:15:05 2024

@author: Brooklyn
"""

def main ():
    import pygame
    pygame.init 
    
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Hello, world")
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill ("pink")
    
    clock = pygame.time.Clock()
    keepGoing = True 
    
    while keepGoing:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        screen.blit(background, (0,0))
        pygame.display.flip()
    pygame.quit()
    
if __name__ == "__main__":
    main()
    