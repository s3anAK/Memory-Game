import pygame
import pygame.freetype
import time
from random import *

'''
#I imported random to handle the choosing of the random pattern sequence for the computer.

#I imported time to use time.sleep() in order to make each square stay green for a short time when clicked or highlighted.

#I used the pygame library to handle the graphic part of my program.
#Specifically, the pygame library handled displaying the squares on the screen and dealing with user interaction.
#Pygame is a standard library that comes with some installations of python. All of the actual code was developed by myself, but 
#in some places I used functions and commands from pygame. 
#All the documentation where I got the various commands and objects from is here: https://www.pygame.org/docs/
#Below are the various commands and objects that I used:

pygame.font.SysFont()
font.render()
surface.blit()
pygame.draw.rect()
pygame.display.flip()
screen.fill()
pygame.init()
pygame.display.set_mode()
pygame.display.set_caption()
pygame.time.Clock()
clock.tick()
pygame.Rect()
pygame.Color()
pygame.event.get()
event.type
pygame.QUIT
pygame.MOUSEMOTION
pygame.mouse.get_pos()
start.collidepoint()
pygame.MOUSEBUTTONDOWN
'''


def display_text(text, font, size, x, y, surface, color):
    font = pygame.font.SysFont(text, size)
    textsurface = font.render(text, True, color)
    surface.blit(textsurface, (x, y))

def tile_updater(tile,surface,first_color,second_color):
    pygame.draw.rect(surface, first_color, tile)
    pygame.display.flip()
    time.sleep(0.5)
    pygame.draw.rect(surface, second_color, tile)
    pygame.display.flip()

def pattern_checker(player,computer):
    global player_turn
    global computer_turn
    global memory_running
    global screen
    for i in range(0, len(player)):
        if player[i] != computer[i]:
            screen.fill((255, 255, 255))
            display_text("That was the incorrect answer. You lost!", \
                         "Helvetica", 50, 80, 250, screen, (0, 0, 255))
            pygame.display.flip()
            time.sleep(2)
            player_turn = False
            computer_turn = False
            memory_running = False
        else:
            if i == len(computer)-1:
                player_turn = False
                computer_turn = True
            else:
                pass


def main():
    global player_turn
    global computer_turn
    global memory_running
    global screen
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Memory Game')

    clock = pygame.time.Clock()
    clock.tick(60)

    screen.fill((255, 255, 255))

    tile1 = pygame.Rect(130, 50, 250, 250)
    tile2 = pygame.Rect(400, 50, 250, 250)
    tile3 = pygame.Rect(130, 320, 250, 250)
    tile4 = pygame.Rect(400, 320, 250, 250)

    grey = pygame.Color((211, 211, 211))
    tile_selected_color = pygame.Color((22,100,8))

    light_button = pygame.Color((190, 190, 190))
    dark_button = pygame.Color((100, 100, 100))

    start = pygame.Rect(130, 320, 250, 250)
    pygame.draw.rect(screen,light_button,start)
    display_text("Start", "Helvetica", 50, 215, 425, screen, (0, 0, 255))

    display_text("Welcome to the Memory Game!", "Helvetica", 50, 100, 0, screen, (0, 0, 0))
    display_text("The computer will light up the tiles", "Helvetica", 50, 80, 70, screen, (0, 0, 255))
    display_text("in a certain order. Then you will have", "Helvetica", 50, 80, 140, screen, (0, 0, 255))
    display_text("to match the pattern. If you press the", "Helvetica", 50, 80, 210, screen, (0, 0, 255))
    display_text("tiles out of order, then you will lose.", "Helvetica", 50, 80, 280, screen, (0, 0, 255))

    pygame.display.flip()

    memory_running = False
    game_start = True
    computer_turn = False
    player_turn = False

    tile_list = [tile1,tile2,tile3,tile4]
    computer_pattern = []
    player_pattern = []

    while game_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = False
            if event.type == pygame.MOUSEMOTION:
                mouse = pygame.mouse.get_pos()
                if mouse[0] > 130 and mouse[0] < 380 and mouse[1] > 320 and mouse[1] < 570:
                    pygame.draw.rect(screen,dark_button,start)
                else:
                    pygame.draw.rect(screen, light_button, start)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if start.collidepoint(mouse[0],mouse[1]):
                    game_start = False
                    memory_running = True
                    computer_turn = True

        display_text("Start", "Helvetica", 50, 215, 425, screen, (0, 0, 255))
        pygame.display.flip()



    while memory_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                memory_running = False

        print('nobody"s turn')

        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, grey, tile1)
        pygame.draw.rect(screen, grey, tile2)
        pygame.draw.rect(screen, grey, tile3)
        pygame.draw.rect(screen, grey, tile4)

        pygame.display.flip()

        while computer_turn:
            print("_____COMPUTER_____")
            display_text("Computer Turn", "Helvetica", 50, 320, 10, screen, (0, 0, 255))
            pygame.display.flip()
            if len(computer_pattern) >= 4:
                screen.fill((255, 255, 255))
                display_text("Congratulations. You Won!", "Helvetica", 50, 80, 250, screen, (0, 0, 255))
                pygame.display.flip()
                time.sleep(2)
                computer_turn = False
                memory_running = False
                player_turn = False
                break
            tile_number = randint(1, 4)
            while tile_list[tile_number - 1] in computer_pattern:
                tile_number = randint(1, 4)
            computer_pattern.append(tile_list[tile_number - 1])
            print('computer is',computer_pattern)
            time.sleep(0.5)
            for tile in computer_pattern:
                pygame.draw.rect(screen, tile_selected_color, tile)
                pygame.display.flip()
                time.sleep(0.5)
                pygame.draw.rect(screen, grey, tile)
                pygame.display.flip()
                time.sleep(0.5)
            computer_turn = False
            player_turn = True
            player_pattern = []
            screen.fill((255, 255, 255))
            pygame.draw.rect(screen, grey, tile1)
            pygame.draw.rect(screen, grey, tile2)
            pygame.draw.rect(screen, grey, tile3)
            pygame.draw.rect(screen, grey, tile4)

            pygame.display.flip()

        while player_turn:
            display_text("Your Turn", "Helvetica", 50, 320, 10, screen, (0, 0, 255))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    memory_running = False
                    player_turn = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if tile1.collidepoint(mouse[0], mouse[1]):
                        print('___tile pressed___')
                        tile_updater(tile1, screen, tile_selected_color, grey)
                        player_pattern.append(tile1)
                        pattern_checker(player_pattern,computer_pattern)
                        print(player_turn)
                    if tile2.collidepoint(mouse[0], mouse[1]):
                        print('___tile pressed___')
                        tile_updater(tile2, screen, tile_selected_color, grey)
                        player_pattern.append(tile2)
                        pattern_checker(player_pattern,computer_pattern)
                        print(player_turn)
                    if tile3.collidepoint(mouse[0], mouse[1]):
                        print('___tile pressed___')
                        tile_updater(tile3, screen, tile_selected_color, grey)
                        player_pattern.append(tile3)
                        pattern_checker(player_pattern,computer_pattern)
                        print(player_turn)
                    if tile4.collidepoint(mouse[0], mouse[1]):
                        print('___tile pressed___')
                        tile_updater(tile4, screen, tile_selected_color, grey)
                        player_pattern.append(tile4)
                        pattern_checker(player_pattern,computer_pattern)
                        print(player_turn)


main()

pygame.quit()