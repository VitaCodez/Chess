import pygame
from .constants import ROWS, COLS, WHITE, BLACK, BROWN, GRAY, SQUARE_SIZE
from .pieces import Pawn, Rook, Queen, King, Bishop, Knight

class Board():

    def __init__(self, win):
        self.win = win
        self.white_pieces = []
        self.black_pieces = []
        self.board_list = []
        self.create_board()
    
    def create_board(self):
        for row in range(ROWS):
            self.board_list.append([])
            for col in range(COLS):
                if row == 1:
                    self.board_list[row].append(Pawn(row, col, BLACK))
                elif row ==0 and (col == 0 or col == 7):
                    self.board_list[row].append(Rook(row, col, BLACK))
                elif row ==0 and (col ==1 or col ==6):
                    self.board_list[row].append(Knight(row, col, BLACK))
                elif row ==0 and (col ==2 or col ==5):
                    self.board_list[row].append(Bishop(row, col, BLACK))
                elif row ==0 and col ==3:
                    self.board_list[row].append(Queen(row, col, BLACK))
                elif row ==0 and col ==4:
                    self.board_list[row].append(King(row, col, BLACK))
                elif row == 6:
                    self.board_list[row].append(Pawn(row, col, WHITE))
                elif row ==7 and (col == 0 or col == 7):
                    self.board_list[row].append(Rook(row, col, WHITE))
                elif row ==7 and (col ==1 or col ==6):
                    self.board_list[row].append(Knight(row, col, WHITE))
                elif row ==7 and (col ==2 or col ==5):
                    self.board_list[row].append(Bishop(row, col, WHITE))
                elif row ==7 and col ==3:
                    self.board_list[row].append(Queen(row, col, WHITE))
                elif row ==7 and col ==4:
                    self.board_list[row].append(King(row, col, WHITE))
                else:
                    self.board_list[row].append(0)

    def draw_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                if row % 2:
                    if not col % 2:
                        pygame.draw.rect(self.win, BROWN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    else:
                        pygame.draw.rect(self.win, GRAY, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                elif col % 2:
                    pygame.draw.rect(self.win, BROWN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))  
                else:
                    pygame.draw.rect(self.win, GRAY, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))  


        for row in self.board_list:
            for piece in row:
                if piece != 0:
                    piece.draw(self.win)



        

    
