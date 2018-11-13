import pygame
import time
import random
import math

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Black Lightning')
clock = pygame.time.Clock()

playerImg = pygame.image.load('mouse.gif')
player_width = 26
player_height = 20
enemyImg = pygame.image.load('cat.gif')
enemy_width = 77
enemy_height = 60
cheeseImg = pygame.image.load('cheese.gif')
cheese_width = 23
cheese_height = 20

def things(thing_x, thing_y, thing_w, thing_h, thing_color):
    pygame.draw.rect(gameDisplay, thing_color, [thing_x, thing_y, thing_w, thing_h])

def text_objects(text, font):
    text_suface = font.render(text, True, black)
    return text_suface, text_suface.get_rect()

def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 72)
    text_surface, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width/2), (display_height)/2)
    gameDisplay.blit(text_surface, text_rect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def player(x, y):
    gameDisplay.blit(playerImg, (x, y))

def enemy(enemy_x, enemy_y):
    gameDisplay.blit(enemyImg, (enemy_x, enemy_y))

def cheese(cheese_x, cheese_y):
    gameDisplay.blit(cheeseImg, (cheese_x, cheese_y))

    # def is_collision(self, other):
    #     a = self.xcor() - other.xcor()
    #     b = self.ycor() - other.ycor()
    #     distance = math.sqrt((a ** 2) + (b ** 2))
    #
    #     if distance < 5:
    #         return True
    #     else:
    #         return False

def crash():
    message_display('BM ate you')

def win():
    message_display('You got the cheese!')

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    # x_change = 0
    # y_change = 0

    # thing_start_x = random.randrange(0, display_width) ##come back and add image width so it's not off the screen
    # thing_start_y = -600
    # thing_speed = 7
    # thing_width = 50
    # thing_height = 50

    enemy_x = random.randrange(0, display_width) ##come back and add image width so it's not off the screen
    enemy_y = -600
    enemy_speed = 7

    cheese_x = random.randrange(0, display_width)
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

        gameDisplay.fill(white)

        #def things(thing_x, thing_y, thing_w, thing_h, thing_color):
        cheese(cheese_x, cheese_y)
        cheese_y += cheese_speed
        enemy(enemy_x, enemy_y)
        enemy_y += enemy_speed
        player(x, y)
        # mouse(x, y)

        if x > display_width - player_width or x < 0:
            crash()
            # game_exit = True

        if enemy_y > display_height:
            enemy_y = 0 - enemy_height
            enemy_x = random.randrange(0, display_width)

        if cheese_y > display_height:
            cheese_y = 0 - enemy_height
            cheese_x = random.randrange(0, display_width)

        if y + player_height > enemy_y and y < enemy_y + enemy_height:
            if x + player_width > enemy_x and x < enemy_x + enemy_width:
                crash()

        if y + player_height > cheese_y and y < cheese_y + cheese_height:
            if x + player_width > cheese_x and x < cheese_x + cheese_width:
                win()

        # #def things(thing_x, thing_y, thing_w, thing_h, thing_color):
        # things(thing_start_x, thing_start_y, thing_width, thing_height, black)
        # thing_start_y += thing_speed
        # player(x, y)
        # # mouse(x, y)

        # if thing_start_y > display_height:
        #     thing_start_y = 0 - thing_height
        #     thing_start_x = thing_start_x = random.randrange(0, display_width)
        #
        # if y + player_height > thing_start_y and y < thing_start_y + thing_height:
        #     if x + player_width > thing_start_x and x < thing_start_x + thing_width:
        #         crash()

        pygame.display.update()
        clock.tick(60)

game_loop()

pygame.quit()
quit()