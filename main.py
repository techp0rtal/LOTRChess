#I like chess and Lord of the Rings.

import pygame
from pygame.examples.go_over_there import screen

pygame.init()
WIDTH = 1000
HEIGHT = 900
screem = pygame.display.set_mode([WIDTH,HEIGHT])
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60
# game variables and images

#main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')

    #event handling (getting all your inputs, key board, mouse, etc)
    for event in pygame.event.get():

