
import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

ORCHID = (255, 131, 250)
SKYBLUE = (0, 191, 255)
PALEGREEN = (152, 251, 152)
LINE_COLOR = (187, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill( PALEGREEN )

board = np.zeros( (BOARD_ROWS, BOARD_COLS) )
print(board)

def draw_lines():
    pygame.draw.line( screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH )
    pygame.draw.line( screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH )
    pygame.draw.line( screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH )
    pygame.draw.line( screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH )
draw_lines()

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle( screen, SKYBLUE, (int( col * 200 + 100 ), int( row * 200 + 100 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
            elif board[row][col] == 2:
                pygame.draw.line( screen, ORCHID, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH )
                pygame.draw.line( screen, ORCHID, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH )

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True
          
def check_win(player):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True


    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagnol(player)
        return True

    return False

def draw_vertical_winning_line(col, player):
    posX = col * 200 + 100

    if player == 1:
        color = SKYBLUE
    elif player == 2:
        color = ORCHID

    pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), 15 )

def draw_horizontal_winning_line(row, player):
     posY = row * 200 + 100

     if player == 1:
         color = SKYBLUE
     elif player == 2:
        color = ORCHID

     pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), 15 )

def draw_asc_diagonal(player):
     if player == 1:
         color = SKYBLUE
     elif player == 2:
        color = ORCHID

     pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15 )

def draw_desc_diagonal(player):
     if player == 1:
         color = SKYBLUE
     elif player == 2:
        color = ORCHID

     pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15 )

def restart():
    screen.fill( PALEGREEN )
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


player = 1
game_over = False

#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            print(clicked_row)
            print(clicked_col)

            if available_square( clicked_row, clicked_col ):
                if player == 1:
                    mark_square( clicked_row, clicked_col, 1 )
                    if check_win( player ):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square( clicked_row, clicked_col, 2 )
                    if check_win( player ):
                        game_over = True
                    player = 1
                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

    
                

    pygame.display.update()
