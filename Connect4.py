import numpy as npy
import pygame
import sys
import math

GREEN = (0,250,0)
BLACK = (0,0,0)
BLUE = (0,0,250)
RED = (250,0,0) #rgb colors to be used later in the program 
rows = 6
columns = 7 #number of rows and columns for this specific connect 4 board 

def create_board():
    board = npy.zeros((rows,columns)) #this function creates the board by setting the board as a matrix using the rows and columns deifned above 
    return board

def drop_piece(board, row, selectedCol, piece):
    board[row][selectedCol] = drop_piece        #the drop piece fucntion defines where the piece should be dropped on the board depedning the the row and selected column

def is_validLocation(board, selectedCol):
    return board[rows-1][selectedCol] == 0  #this function checks to see if the place the pieces is being dropped is a valid spot

def get_nextOpenRow(board, selectedCol):
    for i in range(rows):
        if board[i][selectedCol] == 0: #uses a for loop to see where the next open row is for the piece to drop depending on the chosen column
            return i

def printBoard(board):
    print(npy.flip(board, 0)) #this function flips the orientation of the board as normally the 0,0 coordinate starts at the top left hand corner but for the game we want it in the bottom left hand corner 

def win(board,piece):#this function checks for a connect four win, by checking all possible rows, columns, and diagonals 
    for i in range(columns-3):
        for j in range(rows):
            if board[j][i] == piece and board[j][i +1] == piece and board[j][i +2] == piece and board[j][i +3] == piece:
                return True#this first nested for loop checks all the possible combinations of 4 in a row columns 

    for i in range(columns):
        for j in range(rows-3):
            if board[j][i] == piece and board[j+1][i] == piece and board[j+2][i] == piece and board[j+3][i] == piece:
                return True#this nested for loop checks all the possible combinations of 4 in a row rows

    for i in range(columns-3):
        for j in range(rows-3):
            if board[j][i] == piece and board[j+1][i+1] == piece and board[j+2][i+2] == piece and board[j+3][i+3] == piece:
                return True#this nested for loop checks all the possible combinations of 4 in a row positive slope diagonals 

    for i in range(columns-3):
        for j in range(3, rows):
            if board[j][i] == piece and board[j-1][i+1] == piece and board[j-2][i+2] == piece and board[j-3][i+3] == piece:
                return True#this nested for loop checks all the possible combinations of 4 in a row negative slope diagonals 

def paintBoard(board):#this function is used to display the actual game using pygame 
    for i in range(columns):
        for j in range(rows):
            pygame.draw.rect(screen, GREEN, (i*squareSize, j*squareSize + squareSize, squareSize, squareSize))
            pygame.draw.circle(screen, BLACK,(int(i*squareSize+squareSize/2, int(j*squareSize+squareSize+squareSize/2)), radius)
    #this nested for loop is used to print the actual board in the color green, along with the circular holes in the board
    for c in range(columns):
        for r in range(rows):
            if board[j][i] == 1
                pygame.draw.circle(screen, BLUE,(int(c*squareSize+squareSize/2, height - int(r*squareSize+squareSize/2)), radius)
            elif board[j][i] == 2:
                pygame.draw.circle(screen, RED,(int(c*squareSize+squareSize/2, height - int(r*squareSize+squareSize/2)), radius)
    #this nested for loop is used to display the dropped piece, and does either Blue or Red for the piece depending on which player 
    pygame.display.update()

board = create_board()
printBoard(board)
turn = 0
game_over = False

pygame.init()
squareSize = 120

width = columns = squareSize
height = (rows + 1) = squareSize

size = (width, height)
radius = int(squareSize/2 -4)
screen = pygame.display.set_mode(size)
paintBoard(board)
pygame.display.update()

font = pygame.font.SysFont("Arial",70)


while not game_over:#loop will continue to run while the game_over variabe is false, meaning a connect four has not been reached 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:#if the user wants to quit then the system will exit 
            sys.exit

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, squareSize))
            positionx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, BLUE, (positionx, int(squareSize/2)), radius)
            else:
                pygame.draw.circle(screen, RED, (positionx, int(squareSize/2)), radius)
        pygame.display.update()
        #this statement detects the mouse motion and allows the user to hover a piece above the board and then move it to where they want to drop it
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if turn == 0:# if turn is zero then player 1 makes the selection, otherwise player 2 makes the selection  
                positionx = event.pos[0]
                selectedCol = int(math.floor(positionx/100))

                selectedCol = int(input("Make a Selection Player 1 (0-6): "))

                if is_validLocation(board,selectedCol):
                    row = get_nextOpenRow(board, selectedCol)
                    drop_piece(board,row,selectedCol,1)#calls the earlier defined function to check whether the piece can be dropped, and then is either dropped or is not

                    if win(board,1):
                        label = myfont.render("Player 1 has won!", 1, BLUE)
                        screen.blit(label, (40,10))
                        game_over = True#if a connect four has been achieved using the win function, then the message will be displayed and game_over will be set to true and the loop will stop

            else:
                positionx = event.pos[0]
                selectedCol = int(math.floor(positionx/100))

                selectedCol = int(input("Make a Selection Player 2 (0-6): "))
                if is_validLocation(board,selectedCol):
                    row = get_nextOpenRow(board, selectedCol)
                    drop_piece(board,row,selectedCol,2)

                    if win(board,2):
                        label = myfont.render("Player 2 has won!", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True

            printBoard(board)
            #printBoard is for the commandline output
            paintBoard(board)
            #paintBoard is for displaying through pygame 
            turn += 1
            turn  = turn % 2
            #the turn is incremented by 1 everytime and then set to a remainder of either 0 or 1 to determine which players turn
            if game_over:
                pygame.time.wait(2000)#if the game is done, there is a slight puase time and then it exits 
