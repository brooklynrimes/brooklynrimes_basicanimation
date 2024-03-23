# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:35:16 2024

@author: Brooklyn
"""
import pygame 
import random

def main():
    pygame.init()

    #Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Princess!")

    #Entities
    #yellow background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill("pink")

    #load an image
    princesscarriage = pygame.image.load("princesscarriage.jpg")
    princesscarriage = princesscarriage.convert_alpha()
    princesscarriage = pygame.transform.scale(princesscarriage, (100, 100))

    # set up some princesscarriage variables
    princesscarriage_x = 0
    princesscarriage_y = 200

    #ACTION

        #Assign
    clock = pygame.time.Clock()
    keepGoing = True
    princesscarriage_right= True
    princesscarriage_up = True
    background_color = True

        #Loop
    while keepGoing:

        #Time
        clock.tick(30)

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        if background_color:
            background.fill(pygame.Color(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            background_color =False
        #modify cardinal value
        if princesscarriage_right:
            princesscarriage_x += 5 
        else: 
            princesscarriage_x -= 5 
        if princesscarriage_up:
            princesscarriage_y += 5
        else:
            princesscarriage_y -= 5
            
        #check boundaries
        if princesscarriage_x > screen.get_width()-100:
            princesscarriage_right = False
        if princesscarriage_x < 0 :
            princesscarriage_right = True 
            background_color = True
            
        if princesscarriage_y > screen.get_height()-100:
            princesscarriage_up = False
        if princesscarriage_y < 0: 
            princesscarriage_up = True 
            background_color= True
            
        

        #Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(princesscarriage, (princesscarriage_x, princesscarriage_y))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
    