import pygame as pg
import random
import time
import sys
from color import *
from constant import *

state = 0

class Game:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed_x = 0
        self.speed_y = 0

def make_ball():
    game = Game()
    game.x = 400
    game.y = 300

    game.speed_x = 5
    game.speed_y = -2.5
    return game

while True:
    pg.init()
    pg.event.pump()
    size = [SCREENWIDTH, SCREENHEIGHT]
    screen = pg.display.set_mode(size)

    pg.display.set_caption("PingPong")
    clock = pg.time.Clock()

    clock = pg.time.Clock()

    ball_list = []

    ball = make_ball()
    ball_list.append(ball)

    y_player = 250
    speed_y_player = 0

    y_player_ai = 250
    speed_y_player_ai = 0

    counter = 0

    myfont = pg.font.SysFont("freesansbold", 40)

    counterfont = pg.font.SysFont("freesansbold", 60)

    while state == 0:
        screen.fill(BLACK)

        howToPlay1 = myfont.render("To play you need two players.", 1, (255, 255, 255))
        howToPlay2 = myfont.render(
            "The controls are WASD and the arrow keys.", 1, (255, 255, 255)
        )
        howToPlay3 = myfont.render("Click any where to start", 1, (255, 255, 255))
        screen.blit(howToPlay1, (200, 200))
        screen.blit(howToPlay2, (125, 300))
        screen.blit(howToPlay3, (240, 400))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.display.update()
                pg.display.quit()
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    state = 1
        pg.display.flip()
        clock.tick(60)
    while state == 1:
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.display.update()
                pg.display.quit()
                pg.quit()
                sys.exit()
        if keys[pg.K_w] == 1 or keys[pg.K_s] == 1:
            if keys[pg.K_w] == 1:
                speed_y_player_ai = SPEED_STEP_DOWN
            if keys[pg.K_s] == 1:
                speed_y_player_ai = SPEED_STEP_UP
        if keys[pg.K_w] == 0 and keys[pg.K_s] == 0:
            speed_y_player_ai = 0

        if keys[pg.K_UP] == 1 or keys[pg.K_DOWN] == 1:
            if keys[pg.K_UP] == 1:
                speed_y_player = SPEED_STEP_DOWN
            if keys[pg.K_DOWN] == 1:
                speed_y_player = SPEED_STEP_UP
        if keys[pg.K_UP] == 0 and keys[pg.K_DOWN] == 0:
            speed_y_player = 0

        for game in ball_list:
            game.x += game.speed_x
            game.y += game.speed_y

            if game.y > SCREENHEIGHT - BALLSIZE or game.y < BALLSIZE:
                game.speed_y *= -1
            if game.x > SCREENWIDTH - BALLSIZE or game.x < BALLSIZE:
                game.speed_x *= -1
            if game.x > SCREENWIDTH - BALLSIZE:
                state = 2
            if game.x < BALLSIZE:
                state = 2

        if y_player + 100 > SCREENHEIGHT - BALLSIZE:
            speed_y_player = SPEED_STEP_DOWN
        if y_player < BALLSIZE:
            speed_y_player = 5

        if y_player_ai + 100 > SCREENHEIGHT - BALLSIZE:
            speed_y_player_ai = SPEED_STEP_DOWN
        if y_player_ai < BALLSIZE:
            speed_y_player_ai = SPEED_STEP_UP

        y_player += speed_y_player
        y_player_ai += speed_y_player_ai
        if (
            1 + y_player <= game.y
            and game.y <= 100 + y_player
            and game.x > 750 - BALLSIZE
        ):
            game.speed_x = SPEED_STEP_DOWN
            counter += 1
        if (
            1 + y_player_ai <= game.y
            and game.y <= 100 + y_player_ai
            and game.x - 26 < 55 - BALLSIZE
        ):
            game.speed_x = SPEED_STEP_UP
            counter += 1
        screen.fill(BLACK)

        label = counterfont.render(str(counter), 1, (255, 255, 255))
        screen.blit(label, (400, 50))

        pg.draw.line(screen, WHITE, (750, y_player + 100), (750, y_player), 5)
        pg.draw.line(screen, WHITE, (50, y_player_ai + 100), (50, y_player_ai), 5)

        for ball in ball_list:
            color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
            pg.draw.circle(screen, color, [game.x, game.y], BALLSIZE)

        clock.tick(60)
        pg.display.flip()
    while state == 2:
        screen.fill(BLACK)

        endGame = myfont.render(
            "You lost. Your our score is " + str(counter), 1, (255, 255, 255)
        )
        play = myfont.render("Press anywhere to play again", 1, (255, 255, 255))

        screen.blit(endGame, (210, 200))
        screen.blit(play, (200, 300))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.display.update()
                pg.display.quit()
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    state = 1
                    counter = 0

        pg.display.flip()
        clock.tick(60)
