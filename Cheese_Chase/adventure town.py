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
playerImg = pygame.image.load('mouse.gif')
enemyImg = pygame.image.load('cat.gif')
cheeseImg = pygame.image.load('cheese.gif')

player_width = playerImg.get_width()
player_height = playerImg.get_height()
enemy_width = enemyImg.get_width()
enemy_height = enemyImg.get_height()
cheese_width = cheeseImg.get_width()
cheese_height = cheeseImg.get_height()


# player_width = 26
# player_height = 20
# enemy_width = 77
# enemy_height = 60
# cheese_width = 23
# cheese_height = 20


# weapons = {'Fist': {'+atk': 0, 'Cost': 10},
#            'Wooden Sword': {'+atk': 2, 'Cost': 20},
#            'Rusty Sword': {'+atk': 4, 'Cost': 30},
#            'Iron Sword': {'+atk': 6, 'Cost': 40},
#            'Steel Sword': {'+atk': 8, 'Cost': 50},
#            'Sword of Crushing Puss': {'+atk': 100, 'Cost': 10000}}
#
#
# armor = {"Travelers Cloths": {'+def': 0, 'Cost': 10},
#          'Cloth Armor': {'+def': 2, 'Cost': 100},
#          'Leather Armor': {'+def': 4, 'Cost': 150},
#          'Iron Armor': {'+def': 6, 'Cost': 200},
#          'Mail Armor': {'+def': 8, 'Cost': 250},
#          'Steel Armor': {'+def': 10, 'Cost': 300}}
#
#
# class Player:
#     def __init__(self, name, curweap=None, curarmor=None):
#         if curweap is None:
#             curweap = random.choice(list(weapons.keys()))
#         if curarmor is None:
#             curarmor = random.choice(list(armor.keys()))
#         self.name = name
#         self.maxhealth = 100
#         self.health = self.maxhealth
#         self.base_attack = 14
#         self.base_defense = 5
#         self.critical = .05
#         self.gold = 10000
#         self.pots = 1
#         self.curweap = curweap
#         self.weap = []
#         self.curarmor = curarmor
#         self.armor = []
#         self.location = 'D2'
#         self.game_over = False
#
#     @property
#     def attack(self):
#         attack = self.base_attack + weapons[player.curweap]['+atk']
#         return attack
#
# player = Player("Tomer")
#
#
# def main():
#     print(input("Select 1 for Weapons or 2 for Armor"))
#     option = input("-> ")
#     if option is '1':
#         weapons_store()
#     elif option is '2':
#         armor_store()
#     else:
#         main()
#
#
# def weapons_store():
#     weapon_name = max(map(len, weapons)) + 2
#     weapon_atk = len(str(max(int(d['+atk']) for d in weapons.values()))) + 2
#     weapon_cost = len(str(max(int(d['Cost']) for d in weapons.values())))
#
#     print("{:<{weapon_name}} {:<{weapon_atk}} {:<{weapon_cost}}".format('Weapon', 'Atk', 'Cost', weapon_name=weapon_name, weapon_atk=weapon_atk, weapon_cost=weapon_cost))
#     for (k1, v1) in weapons.items():
#         Atk = v1["+atk"]
#         Cost = v1["Cost"]
#         print("{:<{weapon_name}} {:<{weapon_atk}} {:<{weapon_cost}}".format(k1, Atk, Cost, weapon_name=weapon_name, weapon_atk=weapon_atk, weapon_cost=weapon_cost))
#     option = input("You have %s gold. What would you like to buy?" % player.gold)
#     if option is not None:
#         player.curweap = list(armor.keys())[(int(option) - 1)] ##get the key the corresponds to the number typed in
#         print(player.curweap)
#     main()
#
#
# def armor_store():
#     armor_name = max(map(len, armor)) + 2
#     armor_def = len(str(max(int(d['+def']) for d in armor.values()))) + 2
#     armor_cost = len(str(max(int(d['Cost']) for d in armor.values())))
#
#     print("{:<{armor_name}} {:<{armor_def}} {:<{armor_cost}}".format('Armor', 'Def', 'Cost', armor_name=armor_name, armor_def=armor_def, armor_cost=armor_cost))
#     for (k1, v1) in enumerate(armor.items()):
#         Def = v1["+def"]
#         Cost = v1["Cost"]
#         print("{:<{armor_name}} {:<{armor_def}} {:<{armor_cost}}".format(k1, Def, Cost, armor_name=armor_name, armor_def=armor_def, armor_cost=armor_cost))
#     option = input("You have %s gold. What would you like to buy?" % player.gold)
#     if option is not None:
#         player.curarmor = list(armor.keys())[(int(option) - 1)] ##get the key the corresponds to the number typed in
#         print(player.curarmor)
#     main()

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(enemy_x, enemy_y):
    screen.blit(enemyImg, (enemy_x, enemy_y))


def cheese(cheese_x, cheese_y):
    screen.blit(cheeseImg, (cheese_x, cheese_y))

# main()
# weapon_name = max(map(len, weapons)) + 2
# x = input('weapons or armor?')
# if x is '1':
#     y = str('weapons')
# else: y = str('armor')
# print(y)
# print(y+'_name')
#
# print("{:<5} {:<23} {:^5} {:^6}".format('Num', 'Name', 'Atk', 'Cost'))
# for num, (k, v) in enumerate(weapons.items(), start=1):
#     print("{:<4}: {: <22} :{:^5}: {:^5}".format(num, k, v['+atk'], v['Cost']))


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


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(bg1, (0, 0))
        med_text = pygame.font.Font('yoster.ttf', 30)
        text_surface, text_rect = text_objects("Ohai", med_text)
        text_rect.center = (screen_width/2, screen_height/2)
        screen.blit(text_surface, text_rect)

        button('New Game', 250, 350, 150, 50, khaki, aqua, game_loop)
        button('Options', 450, 350, 150, 50, khaki, aqua, game_options)

        pygame.display.update()
        clock.tick(15)


# def game_loop():
#
#     game_exit = False
#
#     while game_exit is False:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_exit = True
#         screen.fill(white)
#         # button('Quit', 450, 350, 150, 50, khaki, aqua, quit_game)
#         message_display('Hi')
#         # message_display('My name is Mitts.')
#         # message_display("What's your name?")
#         screen.blit(catImg, (450, 300))
#         pygame.display.update()


def game_loop():
    x = (screen_width * 0.45)
    y = (screen_height * 0.8)

    enemy_x = random.randrange(0, screen_width) ##come back and add image width so it's not off the screen
    enemy_y = -600
    enemy_speed = 7

    cheese_x = random.randrange(0, screen_width)
    cheese_y = -600
    cheese_speed = 10

    game_exit = False

    while not game_exit:

        for event in pygame.event.get(): ##Will handle all movement based on user input
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]: x += 5
        if pressed[pygame.K_LEFT]: x -= 5
        if pressed[pygame.K_UP]: y -= 5
        if pressed[pygame.K_DOWN]: y += 5

        screen.fill(white)

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
                quit()

        screen.fill(white)
        message_display('Nothing here yet')
        button('Main Menu', 250, 350, 150, 50, khaki, aqua, game_intro)

        pygame.display.update()
        clock.tick(15)


def quit_game():
    pygame.quit()
    quit()


game_intro()
pygame.quit()