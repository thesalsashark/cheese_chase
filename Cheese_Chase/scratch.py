import random
import itertools
# import tabulate
# from prettytable import PrettyTable
import pygame
import time

screen_width = 800
screen_height = 600
screen_fps = 60

white = (255, 255, 255)
aqua = (127, 255, 212)
brick = (156, 102, 31)
dark_green = (100, 102, 31)
black = (0, 0, 0)
khaki = (240, 230, 140)
dark_khaki = (200, 190, 140)

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Title")
clock = pygame.time.Clock()

pygame.font.init()

bg = pygame.image.load("gottagofast.gif")
bg1 = pygame.image.load('background.gif')
bg2 = pygame.image.load('background.gif')
gamebg = pygame.image.load('game_bg.gif')
playerImg = pygame.image.load('mouse.gif')
enemyImg = pygame.image.load('cat.gif')
cheeseImg = pygame.image.load('cheese.gif')

player_width = playerImg.get_width()
player_height = playerImg.get_height()
enemy_width = enemyImg.get_width()
enemy_height = enemyImg.get_height()
cheese_width = cheeseImg.get_width()
cheese_height = cheeseImg.get_height()


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(enemy_x, enemy_y):
    screen.blit(enemyImg, (enemy_x, enemy_y))


def cheese(cheese_x, cheese_y):
    screen.blit(cheeseImg, (cheese_x, cheese_y))


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def message_display(text):
    my_font = pygame.font.SysFont('yoster.ttf', 30)
    text_surface, text_rect = text_objects(text, my_font)
    text_rect.center = (screen_width/2, screen_height/2)
    screen.blit(text_surface, text_rect)

    pygame.display.update()

    # time.sleep(3)


def crash():
    message_display('BM ate you')


def win():
    message_display('You got the cheese!')


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    small_text = pygame.font.Font('yoster.ttf', 20)
    text_surface, text_rect = text_objects(msg, small_text)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(text_surface, text_rect)


def text_box(msg, x, y, w, h, c):
    small_text = pygame.font.Font('yoster.ttf', 20)
    pygame.draw.rect(screen, c, (x, y, w, h))
    text_surface, text_rect = text_objects(msg, small_text)
    text_rect = (x, y)
    screen.blit(text_surface, text_rect)


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(bg1, (0, 0))
        med_text = pygame.font.Font('yoster.ttf', 30)
        text_surface, text_rect = text_objects("Escape Black Lightning!!", med_text)
        text_rect.center = (screen_width/2, screen_height/2)
        screen.blit(text_surface, text_rect)

        button('New Game', 225, 350, 150, 50, khaki, aqua, game_loop)
        button('How to Play', 425, 350, 150, 50, khaki, aqua, game_options)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    x = (screen_width * 0.45)
    y = (screen_height * 0.8)

    enemy_x = random.randrange(0, screen_width) ##come back and add image width so it's not off the screen
    enemy_y = -600
    enemy_speed = 7

    cheese_x = random.randrange(0, screen_width)
    cheese_y = -600
    cheese_speed = 5

    game_exit = False

    while not game_exit:

        for event in pygame.event.get(): ##Will handle all movement based on user input
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.K_ESCAPE:
                game_intro()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]: x += 5
        if pressed[pygame.K_LEFT]: x -= 5
        if pressed[pygame.K_UP]: y -= 5
        if pressed[pygame.K_DOWN]: y += 5
        if pressed[pygame.K_ESCAPE]: game_intro()

        screen.blit(gamebg, (0, 0))

        #def things(thing_x, thing_y, thing_w, thing_h, thing_color):
        cheese(cheese_x, cheese_y)
        cheese_y += cheese_speed
        enemy(enemy_x, enemy_y)
        enemy_y += enemy_speed
        player(x, y)
        # mouse(x, y)

        if x > screen_width - player_width or x < 0:
            crash()
            # game_exit = True

        if enemy_y > screen_height:
            enemy_y = 0 - enemy_height
            enemy_x = random.randrange(0, screen_width)

        if cheese_y > screen_height:
            cheese_y = 0 - enemy_height
            cheese_x = random.randrange(0, screen_width)

        if y + player_height > enemy_y and y < enemy_y + enemy_height:
            if x + player_width > enemy_x and x < enemy_x + enemy_width:
                crash()

        if y + player_height > cheese_y and y < cheese_y + cheese_height:
            if x + player_width > cheese_x and x < cheese_x + cheese_width:
                win()

        pygame.display.update()
        clock.tick(60)


def game_options():

    options = True

    while options is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.blit(gamebg, (0, 0))
        text_box("You're a mouse. Collect the cheese and avoid Black Lightning.", 5, 5, 790, 100, khaki)
        button("Main Menu", ((screen_width/2) - 150/2), ((screen_height/2) - 100/2), 150, 100, khaki, aqua, game_intro)
        pygame.display.update()
        clock.tick(15)


def quit_game():
    pygame.quit()
    quit()


game_intro()
pygame.quit()