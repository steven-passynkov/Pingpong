import pygame as pg
import os
import random
import socket
import numpy
import csv

state = 0

#Colours
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

#Setup
pg.init()
screen = pg.display.set_mode((800,600)) #set your window size, (x,y)
clock = pg.time.Clock()#you can just use import time and time.sleep()
font = pg.font.Font('freesansbold.ttf', 24)
die = 0
coin = 0
num = 30000
x = False
t = 0
g = 0
i = 0
color = random.randint(1,4)
counter = 0
time_coin = 0
health = 15
maze = []
move_wall = []
walls = 1
player = pg.Rect(373,300,50,50)
coin_1 = pg.Rect(700,510,25,25)
coin_2 = pg.Rect(750,25,25,25)
coin_3 = 0
game = pg.Rect(200,300,100,100)
leaderbord = pg.Rect(600,300,100,100)
Quit = pg.Rect(400, 450,100,100)
name = socket.gethostname()
score = num/10

end = pg.Rect(225,120,50,50)
door_image = pg.image.load("door.png")
door_image = pg.transform.scale(door_image,(end[2],end[3]))

wall_1 = pg.Rect(0,75,700,10)
maze.append(wall_1)
wall_2 = pg.Rect(700,75,10,100)
maze.append(wall_2)
wall_3 = pg.Rect(630,260,200,10)
maze.append(wall_3)
wall_4 = pg.Rect(630,170,10,90)
maze.append(wall_4)
wall_5 = pg.Rect(520,170,120,10)
maze.append(wall_5)
wall_6 = pg.Rect(450,75,10,400)
maze.append(wall_6)
wall_7 = pg.Rect(450,260,180,10)
maze.append(wall_7)
wall_8 = pg.Rect(450,370,270,10)
maze.append(wall_8)
wall_9 = pg.Rect(450,460,10,140)
maze.append(wall_9)
wall_10 = pg.Rect(460,460,180,10)
maze.append(wall_10)
wall_11 = pg.Rect(635,460,10,140)
maze.append(wall_11)
wall_12 = pg.Rect(645,460,270,10)
maze.append(wall_12)

move_1 = pg.Rect(300,500,150,10)
move_wall.append(move_1)
move_2 = pg.Rect(300,400,150,10)
move_wall.append(move_2)
move_3 = pg.Rect(300,300,150,10)
move_wall.append(move_3)
move_4 = pg.Rect(300,200,150,10)
move_wall.append(move_4)

top = pg.Rect(0,0,800,0)
maze.append(top)
bottom = pg.Rect(0,600,800,0)
maze.append(bottom)
side_r = pg.Rect(0,0,0,600)
maze.append(side_r)
side_l = pg.Rect(800,0,0,800)
maze.append(side_l)
side = pg.Rect(0,80,10,600)
maze.append(side)

def move(which,num):
    keys = pg.key.get_pressed()
    if which == 0:
        player[num] -= 1
        if keys[pg.K_LSHIFT]:
            player[num] -= 2
    if which == 1:
        player[num] += 1
        if keys[pg.K_LSHIFT]:
            player[num] += 2

def esc():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.display.update()
            pg.display.quit()
            pg.quit()
while True:
    while state == 0:
        counter += 1
        pg.display.set_caption("Times died: " + str(die) + " Score: " + str(score))
        pg.event.pump()
        screen.fill(black)
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            move(0,1)
        if keys[pg.K_s]:
            move(1,1)
        if keys[pg.K_a]:
            move(0,0)
        if keys[pg.K_d]:
            move(1,0)

        if player.colliderect(top):
            player = pg.Rect(10,10,50,50)
        if player.colliderect(bottom):
            player = pg.Rect(10,10,50,50)
        if player.colliderect(side_r):
            player = pg.Rect(10,10,50,50)
        if player.colliderect(side_l):
            player = pg.Rect(10,10,50,50)
        if player.colliderect(game):
            player = pg.Rect(10,10,50,50)
            counter = 0
            state = 2
        if player.colliderect(leaderbord):
            counter = 0
            state = 1
        if counter == 9:
            color = random.randint(1,4)
            counter = 0
        the_color = dict({1:white,2:blue,3:red,4:green})

        text = font.render("Maze game", True, the_color[color])
        textRect = text.get_rect()
        textRect.center = (400, 200)
        screen.blit(text,textRect)

        text = font.render("Game", True, the_color[color])
        textRect = text.get_rect()
        textRect.center = (200, 300)
        screen.blit(text,textRect)

        text = font.render("Leaderbord", True, the_color[color])
        textRect = text.get_rect()
        textRect.center = (600, 300)
        screen.blit(text,textRect)

        text = font.render("Quit", True, the_color[color])
        textRect = text.get_rect()
        textRect.center = (400, 450)
        screen.blit(text,textRect)

        if player.colliderect(Quit):
            pg.display.update()
            pg.display.quit()
            pg.quit()

        esc()
        pg.draw.ellipse(screen,white,player)
        pg.display.flip()
        clock.tick(50)
    while state == 1:
        counter += 1
        score = num/10
        pg.display.set_caption("Times died: " + str(die) + " Score: " + str(score))
        counter += 1
        pg.event.pump()
        screen.fill(black)
        keys = pg.key.get_pressed()
        Quit = pg.Rect(400,500,100,100)

        if keys[pg.K_w]:
            move(0,1)
        if keys[pg.K_s]:
            move(1,1)
        if keys[pg.K_a]:
            move(0,0)
        if keys[pg.K_d]:
            move(1,0)

        if player.colliderect(top):
            player = pg.Rect(10,10,50,50)
        if player.colliderect(bottom):
            player = pg.Rect(10,10,50,50)
        if player.colliderect(side_r):
            player = pg.Rect(10,10,50,50)
        if player.colliderect(side_l):
            player = pg.Rect(10,10,50,50)
        if player.colliderect(Quit):
            player = pg.Rect(373,300,50,50)
            counter = 0
            state = 0

        if counter == 9:
            color = random.randint(1,4)
            counter = 0
        the_color = dict({1:white,2:blue,3:red,4:green})

        data = pd.read_csv("score.csv")
        print(data)
        data["name"] = data["score"].rank()
        data.sort_values("name", inplace = True)

        df_text = font.render(str(data), True, white)
        df_textRect = df_text.get_rect()
        df_textRect.center = (400,300)
        screen.blit(df_text,df_textRect)

        text = font.render("Maze game", True, the_color[color])
        textRect = text.get_rect()
        textRect.center = (400, 500)
        screen.blit(text,textRect)

        esc()
        pg.draw.ellipse(screen,white,player)
        pg.display.flip()
        clock.tick(50)
    while state == 2:
        counter += 1
        score = num/10
        pg.display.set_caption("Times died: " + str(die) + " Score: " + str(score))
        pg.event.pump()
        keys = pg.key.get_pressed()
        screen.fill(black)

        fields = [name,score]
        with open('score.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)

        for wall in move_wall:
            image_wall = pg.image.load("wall.jpg")
            image_wall = pg.transform.scale(image_wall,(wall[2],wall[3]))
            x_wall = wall[0]
            y_wall = wall[1]

            ran = random.uniform(0.5,5.5)
            if wall.colliderect(wall_6):
                walls = 1
            if wall.colliderect(side):
                walls = 2

            if walls == 1:
                wall[0] -= ran
            if walls == 2:
                wall[0] += ran
            screen.blit(image_wall, (x_wall,y_wall))
            if player.colliderect(wall):
                health -= 1
                if health == 0:
                    die += 1
                    player = pg.Rect(10,10,50,50)
                    health = 15

        if keys[pg.K_w]:
            move(0,1)
        if keys[pg.K_s]:
            move(1,1)
        if keys[pg.K_a]:
            move(0,0)
        if keys[pg.K_d]:
            move(1,0)

        if player.colliderect(end):
            counter = 0
            state = 1
        if player.colliderect(wall_7):
            player = pg.Rect(500,300,50,50)
        if player.colliderect(wall_9):
            player = pg.Rect(200,530,50,50)
        if player.colliderect(coin_1):
            coin += 1
            score += 100
            x = True
            coin_1 = pg.Rect(x,999,50,50)
        if player.colliderect(wall_12) and x == True:
            player = pg.Rect(500,300,50,50)
        if player.colliderect(coin_2):
            coin += 1
            score + 500
            coin_2 = pg.Rect(999,999,50,50)
        if player.colliderect(wall_10):
            player = pg.Rect(530,500,50,50)
        if player.colliderect(wall_11):
            if t == 0:
                player = pg.Rect(700,510,50,50)
                t += 1
            if t == 10:
                player = pg.Rect(530,500,50,50)
                t -= 1

        for wall in maze:
            image_wall = pg.image.load("wall.jpg")
            image_wall = pg.transform.scale(image_wall,(wall[2],wall[3]))
            x_walls = wall[0]
            y_walls = wall[1]
            screen.blit(image_wall, (x_walls,y_walls))
            if player.colliderect(wall):
                health -= 1
                if health == 0:
                    die += 1
                    player = pg.Rect(10,10,50,50)
                    health = 15
        if num == 0:
            state = 2

        num = num-1
        num_text = font.render("timer: "+ str(num), True, white)
        num_textRect = num_text.get_rect()
        num_textRect.center = (475,20)
        screen.blit(num_text,num_textRect)

        h_text = font.render("health: "+ str(health), True, white)
        h_textRect = h_text.get_rect()
        h_textRect.center = (325, 20)
        screen.blit(h_text,h_textRect)

        x_door = end[0]
        y_door = end[1]

        esc()
        pg.draw.ellipse(screen,white,coin_1)
        pg.draw.ellipse(screen,white,coin_2)
        pg.draw.ellipse(screen,white,player)
        pg.draw.rect(screen,white,end)
        screen.blit(door_image, (x_door,y_door))

        pg.display.flip()
        clock.tick(50)
