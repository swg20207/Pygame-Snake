import pgzhelper
from random import *
WIDTH = 800
HEIGHT = 800
gridx = 4       #position of head, x
gridy = 10      #also postition of head, but y
tilesize = 40
directionx = 1
directiony = 0
endx = 0
endy = 0
score = 1
gameOn = True
snake_tail = []
snake_head = Actor("snake_head", (gridx * tilesize, gridy * tilesize))
apple = Actor("snake_food", (randint(1, WIDTH/tilesize - 1) * tilesize, randint(1, HEIGHT/tilesize - 1) * tilesize))
snake_head.angle = -90
def draw():
    screen.clear()
    screen.draw.text("SCORE: " + str(score), (WIDTH/2 - WIDTH/10, 50), fontsize = 50)
    bound = Rect(((tilesize/2 - 1, tilesize/2 - 1), (WIDTH - tilesize + 2, HEIGHT - tilesize + 2)))
    screen.draw.rect(bound, (255, 255, 255))
    apple.draw()
    for tail in snake_tail:
        tail.draw()
    snake_head.draw()
    if not gameOn:
        screen.draw.text("YOU LOSE", (WIDTH / 2 - 175, HEIGHT / 2 - 50), fontsize = 100)
def snake_move():
    global gridx, gridy, endx, endy, score
    if snake_head.colliderect(apple):
        apple.x = randint(1, WIDTH/tilesize - 1) * tilesize
        apple.y = randint(1, HEIGHT/tilesize - 1) * tilesize
        snake_tail.insert(0, Actor("snake_tail",(snake_head.x, snake_head.y)))
        score += 1
    else:
        if len(snake_tail) > 0:
            endx = snake_tail[-1].x
            endy = snake_tail[-1].y
            snake_tail.pop()
            snake_tail.insert(0, Actor("snake_tail", (snake_head.x, snake_head.y)))
    gridx += directionx
    gridy += directiony
    snake_head.x = gridx * tilesize
    snake_head.y = gridy * tilesize
def snake_direction():
    global directionx, directiony
    if keyboard.right:
        snake_head.angle = -90
        directionx = 1
        directiony = 0
    elif keyboard.left:
        snake_head.angle = 90
        directionx = -1
        directiony = 0
    elif keyboard.down:
        snake_head.angle = 180
        directionx = 0
        directiony = 1
    elif keyboard.up:
        snake_head.angle = 0
        directionx = 0
        directiony = -1
def check_lose():
    global gameOn, score
    runend = False
    if gridx == 0 or gridx == 20 or gridy == 0 or gridy == 20:
        runend = True
    for tail in snake_tail:
        if snake_head.colliderect(tail):
            runend = True
    if runend:
        snake_head.x -= directionx * tilesize
        snake_head.y -= directiony * tilesize
        clock.unschedule(snake_move)
        end_tail = Actor("snake_tail", (endx, endy))
        snake_tail.append(end_tail)
        gameOn = False
def update():
    if gameOn:
        snake_direction()
        check_lose()
clock.schedule_interval(snake_move, 0.25)