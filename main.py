#I like chess and Lord of the Rings. This combines them both and makes a fun game! :D
#This project will heavily use pygame

import pygame
from pygame.examples.go_over_there import screen

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('LOTR Chess')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60
# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn','pawn','pawn','pawn','pawn','pawn','pawn']
white_locations = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                   (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn','pawn','pawn','pawn','pawn','pawn','pawn']
black_locations = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                   (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]
captured_pieces_white = []
captured_pieces_black = []
'''
In chess, a turn/move is only "completed" when both players have made their moves. 
(The only exception to this rule is when White plays a move that ends the game.) 
So now we create a variable called 'turn_step' which will keep track of the 4 phases of each turn:

0- white's turn, no selection.
1- white's turn, piece selected.
2- black's turn, no selection.
3- black's turn, piece selected.

This variable will have 2 jobs: 
1. To keep track of which of the 4 phases we are in in the game (and which player is currently active).
2. To keep track of what valid moves are available on the board (which can be displayed on the board w/dots).
'''



#main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')

    #event handling (getting all your inputs, key board, mouse, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
