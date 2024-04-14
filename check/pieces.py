import pygame
from .constants import black_queen, black_king, black_rook, black_bishop, black_knight, black_pawn, white_queen, white_king, white_rook, white_bishop, white_knight,white_pawn, WHITE, BLACK, SQUARE_SIZE, ROWS, COLS
class Pawn():

    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.is_king = False

    def draw(self, win):
        if self.colour == WHITE:
            win.blit(white_pawn, (self.col*SQUARE_SIZE+15, self.row*SQUARE_SIZE+35))
        else:
            win.blit(black_pawn, (self.col*SQUARE_SIZE+15, self.row*SQUARE_SIZE+35))

    def get_valid_moves(self, board_list):
        self.valid_moves = []

        if self.colour == WHITE and not (self.row-1) < 0:
            if board_list[self.row-1][self.col] == 0:
                self.valid_moves.append((self.row-1,self.col))
                if not (self.row-2) < 0:
                    if board_list[self.row-2][self.col] == 0 and self.row == 6:
                        self.valid_moves.append((self.row-2, self.col))
            if not (self.col-1) < 0:
                if board_list[self.row-1][self.col-1] != 0:
                    if board_list[self.row-1][self.col-1].colour != self.colour:
                        self.valid_moves.append((self.row-1,self.col-1))
            if not (self.col+1) >= COLS: 
                if board_list[self.row-1][self.col+1] != 0:
                    if board_list[self.row-1][self.col+1].colour != self.colour:
                        self.valid_moves.append((self.row-1,self.col+1))
        elif not (self.row+1) >= ROWS:
            if board_list[self.row+1][self.col] == 0:
                self.valid_moves.append((self.row+1,self.col))
                if not (self.row+2) >= ROWS:
                    if board_list[self.row+2][self.col] == 0 and self.row == 1:
                        self.valid_moves.append((self.row+2,self.col))
            if not (self.col-1) < 0:
                if board_list[self.row+1][self.col-1] != 0:
                    if board_list[self.row+1][self.col-1].colour != self.colour:
                        self.valid_moves.append((self.row+1,self.col-1))
            if not (self.col+1) >= COLS:
                if board_list[self.row+1][self.col+1] != 0:
                    if board_list[self.row+1][self.col+1].colour != self.colour:
                        self.valid_moves.append((self.row+1,self.col+1))
        
        return self.valid_moves
    


class Rook():

    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.is_king = False

    def draw(self, win):
        if self.colour == WHITE:
            win.blit(white_rook, (self.col*SQUARE_SIZE+10, self.row*SQUARE_SIZE+30))
        else:
            win.blit(black_rook, (self.col*SQUARE_SIZE+10, self.row*SQUARE_SIZE+30))

    def get_valid_moves(self, board_list):
        self.valid_moves = []
        self.streak = 1

        while self.streak and not (self.streak+self.col) >= COLS:

            if board_list[self.row][self.col+self.streak] == 0:
                self.valid_moves.append((self.row,self.col+self.streak))
                self.streak +=1
            elif board_list[self.row][self.col+self.streak].colour != self.colour:
                self.valid_moves.append((self.row,self.col+self.streak))
                self.streak = False
            else:
                self.streak = False
        self.streak = 1
        while self.streak and not (self.col-self.streak) < 0:
            
            if board_list[self.row][self.col-self.streak] == 0:
                self.valid_moves.append((self.row,self.col-self.streak))
                self.streak +=1
            elif board_list[self.row][self.col-self.streak].colour != self.colour:
                self.valid_moves.append((self.row,self.col-self.streak))
                self.streak = False
            else:
                self.streak = False
        self.streak = 1
        while self.streak and not (self.row+self.streak) >= ROWS:
            
            if board_list[self.row+self.streak][self.col] == 0:
                self.valid_moves.append((self.row+self.streak,self.col))
                self.streak +=1
            elif board_list[self.row+self.streak][self.col].colour != self.colour:
                self.valid_moves.append((self.row+self.streak,self.col))
                self.streak = False
            else:
                self.streak = False
        self.streak = 1
        while self.streak and not (self.row-self.streak) < 0:
            
            if board_list[self.row-self.streak][self.col] == 0:
                self.valid_moves.append((self.row-self.streak,self.col))
                self.streak +=1
            elif board_list[self.row-self.streak][self.col].colour != self.colour:
                self.valid_moves.append((self.row-self.streak,self.col))
                self.streak = False
            else:
                self.streak = False

        return self.valid_moves
        



class Bishop():

    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.is_king = False

    def draw(self, win):
        if self.colour == WHITE:
            win.blit(white_bishop, (self.col*SQUARE_SIZE+10, self.row*SQUARE_SIZE+20))
        else:
            win.blit(black_bishop, (self.col*SQUARE_SIZE+10, self.row*SQUARE_SIZE+20))
    
    def get_valid_moves(self, board_list):
        self.valid_moves = []
        self.streak = 1

        while self.streak and not (self.streak+self.row) >= ROWS and not (self.streak+self.col) >= COLS:
            if board_list[self.row+self.streak][self.col+self.streak] == 0:
                self.valid_moves.append((self.row+self.streak, self.col+self.streak))
                self.streak +=1
            elif board_list[self.row+self.streak][self.col+self.streak].colour != self.colour:
                self.valid_moves.append((self.row+self.streak, self.col+self.streak))
                self.streak = False
            else:
                self.streak = False
        self.streak = 1
        while self.streak and not (self.row-self.streak) < 0 and not (self.streak+self.col) >= COLS:
            if board_list[self.row-self.streak][self.col+self.streak] == 0:
                self.valid_moves.append((self.row-self.streak, self.col+self.streak))
                self.streak +=1
            elif board_list[self.row-self.streak][self.col+self.streak].colour != self.colour:
                self.valid_moves.append((self.row-self.streak, self.col+self.streak))
                self.streak = False
            else:
                self.streak = False
        self.streak = 1
        while self.streak and not (self.row-self.streak) < 0 and not (self.col-self.streak) < 0:
            if board_list[self.row-self.streak][self.col-self.streak] == 0:
                self.valid_moves.append((self.row-self.streak, self.col-self.streak))
                self.streak +=1
            elif board_list[self.row-self.streak][self.col-self.streak].colour != self.colour:
                self.valid_moves.append((self.row-self.streak, self.col-self.streak))
                self.streak = False
            else:
                self.streak = False
        self.streak = 1
        while self.streak and not (self.streak+self.row) >= ROWS and not (self.col-self.streak) < 0:
            if board_list[self.row+self.streak][self.col-self.streak] == 0:
                self.valid_moves.append((self.row+self.streak, self.col-self.streak))
                self.streak +=1
            elif board_list[self.row+self.streak][self.col-self.streak].colour != self.colour:
                self.valid_moves.append((self.row+self.streak, self.col-self.streak))
                self.streak = False
            else:
                self.streak = False

        return self.valid_moves


class Knight():

    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.is_king = False

    def draw(self, win):
        if self.colour == WHITE:
            win.blit(white_knight, (self.col*SQUARE_SIZE+10, self.row*SQUARE_SIZE+25))
        else:
            win.blit(black_knight, (self.col*SQUARE_SIZE+10, self.row*SQUARE_SIZE+25))


    def get_valid_moves(self, board_list):
        self.valid_moves = []

        if not (self.row-2) < 0 and not (self.col-1) < 0:
            if board_list[self.row-2][self.col-1] == 0:
                self.valid_moves.append((self.row-2, self.col-1))
            elif board_list[self.row-2][self.col-1].colour != self.colour:
                self.valid_moves.append((self.row-2, self.col-1))
        if not (self.row-2) < 0 and not (self.col+1) >= COLS:
            if board_list[self.row-2][self.col+1] == 0:
                self.valid_moves.append((self.row-2, self.col+1))
            elif board_list[self.row-2][self.col+1].colour != self.colour:
                self.valid_moves.append((self.row-2, self.col+1))
        if not (self.row+2) >= ROWS and not (self.col+1) >= COLS:
            if board_list[self.row+2][self.col+1] == 0:
                self.valid_moves.append((self.row+2, self.col+1))
            elif board_list[self.row+2][self.col+1].colour != self.colour:
                self.valid_moves.append((self.row+2, self.col+1))
        if not (self.row+2) >= ROWS and not (self.col-1) < 0:
            if board_list[self.row+2][self.col-1] ==0:
                self.valid_moves.append((self.row+2, self.col-1))
            elif board_list[self.row+2][self.col-1].colour != self.colour:
                self.valid_moves.append((self.row+2, self.col-1))

        if not (self.row-1) < 0 and not (self.col-2) < 0:
            if board_list[self.row-1][self.col-2] == 0:
                self.valid_moves.append((self.row-1, self.col-2))
            elif board_list[self.row-1][self.col-2].colour != self.colour:
                self.valid_moves.append((self.row-1, self.col-2))
        if not (self.row+1) >= ROWS and not (self.col-2) < 0:
            if board_list[self.row+1][self.col-2] == 0:
                self.valid_moves.append((self.row+1, self.col-2))
            elif board_list[self.row+1][self.col-2].colour != self.colour:
                self.valid_moves.append((self.row+1, self.col-2))
        if not (self.row+1) >= ROWS and not (self.col+2) >= COLS:
            if board_list[self.row+1][self.col+2] == 0:
                self.valid_moves.append((self.row+1, self.col+2))
            elif board_list[self.row+1][self.col+2].colour != self.colour:
                self.valid_moves.append((self.row+1, self.col+2))
        if not (self.row-1) < 0 and not (self.col+2) >= COLS:
            if board_list[self.row-1][self.col+2] == 0:
                self.valid_moves.append((self.row-1, self.col+2))
            elif  board_list[self.row-1][self.col+2].colour != self.colour:
                self.valid_moves.append((self.row-1, self.col+2))
        
        return self.valid_moves

class Queen():

    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.is_king = False


    def draw(self, win):
        if self.colour == WHITE:
            win.blit(white_queen, (self.col*SQUARE_SIZE+5, self.row*SQUARE_SIZE+10))
        else:
            win.blit(black_queen, (self.col*SQUARE_SIZE+5, self.row*SQUARE_SIZE+10))

    def get_valid_moves(self, board_list):
        self.valid_moves = []
        self.streak = 1

        while self.streak and not (self.streak+self.col) >= COLS:

            if board_list[self.row][self.col+self.streak] == 0:
                self.valid_moves.append((self.row,self.col+self.streak))
                self.streak +=1
            elif board_list[self.row][self.col+self.streak].colour != self.colour:
                self.valid_moves.append((self.row,self.col+self.streak))
                self.streak = False
            else:
                self.streak = False
        self.streak = 1
        while self.streak and not (self.col-self.streak) < 0:
            
            if board_list[self.row][self.col-self.streak] == 0:
                self.valid_moves.append((self.row,self.col-self.streak))
                self.streak +=1
            elif board_list[self.row][self.col-self.streak].colour != self.colour:
                self.valid_moves.append((self.row,self.col-self.streak))
                self.streak = False
            else:
                self.streak = False
        self.streak = 1
        while self.streak and not (self.row+self.streak) >= ROWS:
            
            if board_list[self.row+self.streak][self.col] == 0:
                self.valid_moves.append((self.row+self.streak,self.col))
                self.streak +=1
            elif board_list[self.row+self.streak][self.col].colour != self.colour:
                self.valid_moves.append((self.row+self.streak,self.col))
                self.streak = False
            else:
                self.streak = False
        self.streak = 1
        while self.streak and not (self.row-self.streak) < 0:
            
            if board_list[self.row-self.streak][self.col] == 0:
                self.valid_moves.append((self.row-self.streak,self.col))
                self.streak +=1
            elif board_list[self.row-self.streak][self.col].colour != self.colour:
                self.valid_moves.append((self.row-self.streak,self.col))
                self.streak = False
            else:
                self.streak = False
        


        self.streak = 1

        while self.streak and not (self.streak+self.row) >= ROWS and not (self.streak+self.col) >= COLS:
            if board_list[self.row+self.streak][self.col+self.streak] == 0:
                self.valid_moves.append((self.row+self.streak, self.col+self.streak))
                self.streak +=1
            elif board_list[self.row+self.streak][self.col+self.streak].colour != self.colour:
                self.valid_moves.append((self.row+self.streak, self.col+self.streak))
                self.streak = False
            else:
                self.streak = False
        self.streak = 1
        while self.streak and not (self.row-self.streak) < 0 and not (self.streak+self.col) >= COLS:
            if board_list[self.row-self.streak][self.col+self.streak] == 0:
                self.valid_moves.append((self.row-self.streak, self.col+self.streak))
                self.streak +=1
            elif board_list[self.row-self.streak][self.col+self.streak].colour != self.colour:
                self.valid_moves.append((self.row-self.streak, self.col+self.streak))
                self.streak = False
            else:
                self.streak = False
        self.streak = 1
        while self.streak and not (self.row-self.streak) < 0 and not (self.col-self.streak) < 0:
            if board_list[self.row-self.streak][self.col-self.streak] == 0:
                self.valid_moves.append((self.row-self.streak, self.col-self.streak))
                self.streak +=1
            elif board_list[self.row-self.streak][self.col-self.streak].colour != self.colour:
                self.valid_moves.append((self.row-self.streak, self.col-self.streak))
                self.streak = False
            else:
                self.streak = False
        self.streak = 1
        while self.streak and not (self.streak+self.row) >= ROWS and not (self.col-self.streak) < 0:
            if board_list[self.row+self.streak][self.col-self.streak] == 0:
                self.valid_moves.append((self.row+self.streak, self.col-self.streak))
                self.streak +=1
            elif board_list[self.row+self.streak][self.col-self.streak].colour != self.colour:
                self.valid_moves.append((self.row+self.streak, self.col-self.streak))
                self.streak = False
            else:
                self.streak = False

        return self.valid_moves




class King():

    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.is_king = True


    def draw(self, win):
        if self.colour == WHITE:
            win.blit(white_king, (self.col*SQUARE_SIZE+5, self.row*SQUARE_SIZE+10))
        else:
            win.blit(black_king, (self.col*SQUARE_SIZE+5, self.row*SQUARE_SIZE+10))

    def get_valid_moves(self, board_list, enemy_moves):
        self.valid_moves = []
        if not self.row+1 >= ROWS:
            if board_list[self.row+1][self.col]  == 0:
                self.valid_moves.append((self.row+1, self.col))
            elif board_list[self.row+1][self.col].colour != self.colour:
                self.valid_moves.append((self.row+1, self.col))
        if not self.row-1 < 0:
            if board_list[self.row-1][self.col]  == 0:
                self.valid_moves.append((self.row-1, self.col))
            elif board_list[self.row-1][self.col].colour != self.colour:
                self.valid_moves.append((self.row-1, self.col))
        if not self.col-1 < 0:
            if board_list[self.row][self.col-1]  == 0:
                self.valid_moves.append((self.row, self.col-1))
            elif board_list[self.row][self.col-1].colour != self.colour:
                self.valid_moves.append((self.row, self.col-1))
        if not self.col+1 >= COLS:
            if board_list[self.row][self.col+1]  == 0:
                self.valid_moves.append((self.row, self.col+1))
            elif board_list[self.row][self.col+1].colour != self.colour:
                self.valid_moves.append((self.row, self.col+1))


        if not self.col-1 < 0 and not self.row-1 < 0:
            if board_list[self.row-1][self.col-1]  == 0:
                self.valid_moves.append((self.row-1, self.col-1))
            elif board_list[self.row-1][self.col-1].colour != self.colour:
                self.valid_moves.append((self.row-1, self.col-1))
        if not self.col+1 >= COLS and not self.row-1 < 0:
            if board_list[self.row-1][self.col+1]  == 0:
                self.valid_moves.append((self.row-1, self.col+1))
            elif board_list[self.row-1][self.col+1].colour != self.colour:
                self.valid_moves.append((self.row-1, self.col+1))
        if not self.col-1 < 0 and not self.row+1 >= ROWS:
            if board_list[self.row+1][self.col-1]  == 0:
                self.valid_moves.append((self.row+1, self.col-1))
            elif board_list[self.row+1][self.col-1].colour != self.colour:
                self.valid_moves.append((self.row+1, self.col-1))
        if not self.col+1 >= COLS and not self.row+1 >= ROWS:
            if board_list[self.row+1][self.col+1]  == 0:
                self.valid_moves.append((self.row+1, self.col+1))
            elif board_list[self.row+1][self.col+1].colour != self.colour:
                self.valid_moves.append((self.row+1, self.col+1))
        
        self.king_valid_moves = []
        print(enemy_moves)
        for move in self.valid_moves:
            if not (move in enemy_moves):
                self.king_valid_moves.append(move)
        print(self.king_valid_moves)

        return self.king_valid_moves

        