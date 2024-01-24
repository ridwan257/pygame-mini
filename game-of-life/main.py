import numpy as np
import pygame as pg


WIDTH, HEIGHT = (600,600)

nR, nC = 200, 200
dx, dy = int(WIDTH/nC), int(HEIGHT/nR)
theta = 0.1

board =  np.random.binomial(1, theta, nR*nC).reshape(nR,nC)
# board = np.array([[1 ,0 ,0 ,1 ,1 ,0, 1, 1],
#  [1 ,0, 0, 0, 1, 0, 1, 1],
#  [1, 1, 0, 0 ,1 ,1 ,0, 1],
#  [0 ,0, 1, 1, 0, 1, 0, 0],
#  [1, 1, 0 ,1, 1, 0 ,0 ,1],
#  [0 ,1, 0, 0 ,1 ,0, 1, 0],
#  [1 ,1 ,1 ,1, 1, 1 ,0 ,0],
#  [1 ,1, 1 ,0, 1 ,1, 0, 0]])


def draw_board(canvus):
    global board, nR, nC, dx, dy
    black = (25, 178, 209)
    white = (250,235,215)
    for i in range(nR):
        for j in range(nC):
            fill_color = black if not board[i,j] else white
            pg.draw.rect(canvus, fill_color, (j*dx+0.5, i*dy+0.5, dx-1, dy-1), width=0)
            # pg.draw.rect(canvus, (200,200,200), (j*dx, i*dy, dx, dy), width=1)


def count_neighbour(x, y):
    global board, nR, nC
    count = 0
    for i in (-1,0,1):
        for j in (-1,0,1):
            # print(f"({i}, {j}) : ", end='')
            posX, posY = x+i, y+j
            if not (i==0 and j==0) and (posX>=0 and posX<nR) and (posY>=0 and posY<nC):
                # print(f"({posX}, {posY}) -> {board[posX, posY]}", end='')
                count += 1 if board[posX, posY] else 0
            # print()
    return count


def update_board():
    global board, nR, nC
    for i in range(nR):
        for j in range(nC):
            neighbour = count_neighbour(i,j)
            if board[i,j]:
                if neighbour < 2 or neighbour > 3:
                    board[i,j] = 0
            else:
                if neighbour == 3:
                    board[i,j] = 1



print(board)
# print()


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Game of Life')
running = True

pause = True

while running:  
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_r:
                board =  np.random.binomial(1, theta, nR*nC).reshape(nR,nC)
                pause = True
            if event.key == pg.K_SPACE:
                pause = True if not pause else False
            if event.key == pg.K_n:
                update_board()
                # print(board)
                # print()

    screen.fill((250,235,215))
    
    #game logic
    draw_board(screen)
    if not pause:
        update_board()
    

    # Update the display
    pg.display.flip()
    # pg.time.delay(50)

pg.quit()
