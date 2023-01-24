"""
    Date : Tue Jan 24 2023 16:42:27 GMT+0530 (India Standard Time)
    Author : Suman Gurung
    Description : My version of the popular game GuessThatPokemon.
"""

import pygame
from pygame import mixer
import random
import time
from helper import get_random_pokemon

pygame.init()

# CONSTANTS
WIN_HEIGHT,WIN_WIDTH = 600,600

WIN = pygame.display.set_mode((WIN_WIDTH , WIN_HEIGHT))
pygame.display.set_caption("Guess that Pokemon")

SCORE_FONT = pygame.font.SysFont("comicsans",30)
MSG_FONT = pygame.font.SysFont("comicsans" , 30)

# CLASSES
class Pokemon:
    def __init__(self,pokemon):
        self.shadow = pygame.image.load(f"assets/{pokemon['image']['shadow']}.png")
        self.reveal = pygame.image.load(f"assets/{pokemon['image']['reveal']}.png")
        self.image = self.shadow
        self.answer_index = pokemon["answer_index"] 
        self.option = pokemon["options"]

class Board:
    def __init__(self,index,x,y):
        self.image = pygame.image.load("assets/board.png")
        self.index = index
        self.x = x
        self.y = y 
        self.width = 285
        self.height = 85

# FUNCTIONS
def draw_screen(win,score,screentype ):
    if screentype=="welcome":
        background = pygame.transform.scale( pygame.image.load("assets/bg.png"), (600,600))
        win.blit(background , (0 , 0))

        title = pygame.transform.scale( pygame.image.load("assets/title.png"), (350,400))
        win.blit(title , (WIN_WIDTH//2-180, 100))

        text = MSG_FONT.render(f"Press Enter to Start", 1 , (0,0,0))
        win.blit(text,(WIN_WIDTH//2 - 90, 520))
    
    if screentype=="exit":
        background = pygame.transform.scale( pygame.image.load("assets/bg.png"), (600,600))
        win.blit(background , (0 , 0))
        
        text1 = MSG_FONT.render(f"YOUR SCORE : {score}", 1 , (0,0,0))
        win.blit(text1,(WIN_WIDTH//2 - 90, WIN_HEIGHT//2))

    pygame.display.update()

def draw(win , current_pokemon , boards , score):
    background = pygame.transform.scale( pygame.image.load(f"assets/bg.png"), (600,600))
    win.blit(background , (0 , 0))

    current_pokemon_sprite = pygame.transform.scale(current_pokemon.image, (300,300))
    win.blit(current_pokemon_sprite , (150 , 50))

    for board in boards:
        board_sprite = pygame.transform.scale(board.image, (board.width,board.height))
        win.blit(board_sprite , (board.x, board.y))

    text1 = MSG_FONT.render(current_pokemon.option[0], 1 , (0,0,0))
    win.blit(text1,(40, 440))
    text2 = MSG_FONT.render(current_pokemon.option[1], 1 , (0,0,0))
    win.blit(text2,(335, 440))
    text3 = MSG_FONT.render(current_pokemon.option[2], 1 , (0,0,0))
    win.blit(text3,(40, 535))
    text4 = MSG_FONT.render(current_pokemon.option[3], 1 , (0,0,0))
    win.blit(text4,(335, 535))

    score = MSG_FONT.render(f"Score x {score}", 1 , (0,0,0))
    win.blit(score,(490, 5))

    pygame.display.update()

def check_answer(current_pokemon , position , boards):
    if current_pokemon.answer_index == 0:
        if position[0]>10 and position[0]<295 and position[1]>410 and position[1]<495:
            boards[0].image = pygame.image.load("assets/board_correct.png")
            return 1
    if current_pokemon.answer_index == 1:
        if position[0]>305 and position[0]<590 and position[1]>410 and position[1]<495:
            boards[1].image = pygame.image.load("assets/board_correct.png")
            return 1
    if current_pokemon.answer_index == 2:
        if position[0]>10 and position[0]<295 and position[1]>505 and position[1]<590:
            boards[2].image = pygame.image.load("assets/board_correct.png")
            return 1
    if current_pokemon.answer_index == 3:
        if position[0]>305 and position[0]<590 and position[1]>505 and position[1]<590:
            boards[3].image = pygame.image.load("assets/board_correct.png")
            return 1

    if position[0]>10 and position[0]<295 and position[1]>410 and position[1]<495:
        boards[0].image = pygame.image.load("assets/board_wrong.png")
        return 2
    if position[0]>305 and position[0]<590 and position[1]>410 and position[1]<495:
        boards[1].image = pygame.image.load("assets/board_wrong.png")
        return 2
    if position[0]>10 and position[0]<295 and position[1]>505 and position[1]<590:
        boards[2].image = pygame.image.load("assets/board_wrong.png")
        return 2
    if position[0]>305 and position[0]<590 and position[1]>505 and position[1]<590:
        boards[3].image = pygame.image.load("assets/board_wrong.png")
        return 2
    
    return 0

# MAIN
def main():
    run = True 
    score = 0
    clock = pygame.time.Clock()
    get_out = False
    
    while run:   # welcome screen loop
        draw_screen(WIN , score , screentype = "welcome")
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_RETURN]:
            run = False  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
                get_out = True
                pygame.quit()
    
    run = True

    while run and not get_out:   # main screen loop
        isrunning = True
        random_pokemon = get_random_pokemon()
        current_pokemon = Pokemon(random_pokemon)
        boards = []
        boards.append(Board(0,10,410))
        boards.append(Board(1,305,410))
        boards.append(Board(2,10,505))
        boards.append(Board(3,305,505))
        
        while isrunning and not get_out:
            clock.tick(60) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    get_out = True
                    isrunning = False
            draw(WIN , current_pokemon , boards , score)
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                result = check_answer(current_pokemon , pygame.mouse.get_pos(),boards)
                if result == 1:
                    score += 1
                    current_pokemon.image = current_pokemon.reveal
                    draw(WIN , current_pokemon , boards , score)
                    time.sleep(2)
                    isrunning = False
                if result == 2:
                    score -= 1
                    draw(WIN , current_pokemon , boards , score)
                    time.sleep(1) 
                    for board in boards:
                        board.image = pygame.image.load("assets/board.png")
        
        if random_pokemon["total"] == 0:
            run = False

    run = True

    while run and not get_out:   # exit screen loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_screen(WIN , score , screentype = "exit")
    
if __name__ == "__main__":
    main()





