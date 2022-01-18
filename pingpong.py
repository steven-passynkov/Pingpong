import pygame as pg
import random
import time
import sys

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

screenWidth = 800
screenHeight = 600
ballSize = 15

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


def esc():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.display.update()
            pg.display.quit()
            pg.quit()
            sys.exit()


while True:
    pg.init()
    size = [screenWidth, screenHeight]
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
        esc()

        screen.fill(black)

        howToPlay1 = myfont.render("To play you need two players.", 1, (255, 255, 255))
        howToPlay2 = myfont.render(
            "The controls are WASD and the arrow keys.", 1, (255, 255, 255)
        )
        howToPlay3 = myfont.render("Click any where to start", 1, (255, 255, 255))
        screen.blit(howToPlay1, (200, 200))
        screen.blit(howToPlay2, (125, 300))
        screen.blit(howToPlay3, (240, 400))
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    state = 1
        pg.display.flip()
        clock.tick(60)
    while state == 1:
        esc()
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                esc()
        if keys[pg.K_w] == 1 or keys[pg.K_s] == 1:
            if keys[pg.K_w] == 1:
                speed_y_player_ai = -5
            if keys[pg.K_s] == 1:
                speed_y_player_ai = 5
        if keys[pg.K_w] == 0 and keys[pg.K_s] == 0:
            speed_y_player_ai = 0

        if keys[pg.K_UP] == 1 or keys[pg.K_DOWN] == 1:
            if keys[pg.K_UP] == 1:
                speed_y_player = -5
            if keys[pg.K_DOWN] == 1:
                speed_y_player = 5
        if keys[pg.K_UP] == 0 and keys[pg.K_DOWN] == 0:
            speed_y_player = 0

        for game in ball_list:
            game.x += game.speed_x
            game.y += game.speed_y

            if game.y > screenHeight - ballSize or game.y < ballSize:
                game.speed_y *= -1
            if game.x > screenWidth - ballSize or game.x < ballSize:
                game.speed_x *= -1
            if game.x > screenWidth - ballSize:
                state = 2
            if game.x < ballSize:
                state = 2

        if y_player + 100 > screenHeight - ballSize:
            speed_y_player = -5
        if y_player < ballSize:
            speed_y_player = 5

        if y_player_ai + 100 > screenHeight - ballSize:
            speed_y_player_ai = -5
        if y_player_ai < ballSize:
            speed_y_player_ai = 5

        y_player += speed_y_player
        y_player_ai += speed_y_player_ai
        if (
            1 + y_player <= game.y
            and game.y <= 100 + y_player
            and game.x > 750 - ballSize
        ):
            game.speed_x = -5
            counter += 1
        if (
            1 + y_player_ai <= game.y
            and game.y <= 100 + y_player_ai
            and game.x - 26 < 55 - ballSize
        ):
            game.speed_x = 5
            counter += 1
        screen.fill(black)

        label = counterfont.render(str(counter), 1, (255, 255, 255))
        screen.blit(label, (400, 50))

        pg.draw.line(screen, white, (750, y_player + 100), (750, y_player), 5)
        pg.draw.line(screen, white, (50, y_player_ai + 100), (50, y_player_ai), 5)

        for ball in ball_list:
            color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
            pg.draw.circle(screen, color, [game.x, game.y], ballSize)

        clock.tick(60)
        pg.display.flip()
    while state == 2:
        esc()
        screen.fill(black)

        endGame = myfont.render(
            "You lost  your our score is " + str(counter), 1, (255, 255, 255)
        )
        play = myfont.render("Press any where to play again", 1, (255, 255, 255))

        screen.blit(endGame, (210, 200))
        screen.blit(play, (200, 300))

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    state = 1
                    counter = 0

        pg.display.flip()
        clock.tick(60)
