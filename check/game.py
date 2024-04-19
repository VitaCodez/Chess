import pygame
from .board import Board
from .constants import BLACK, WHITE
from .pieces import Queen
import copy
class Game():

    def __init__(self, win):
        self.win = win
        self.board = Board(self.win)
        self.valid_moves = []
        self.enpassant_pieces = []
        self.selected_piece = 0
        self.turn = WHITE
        self.black_king = self.find_king(BLACK)
        self.white_king = self.find_king(WHITE)
        self.king = self.white_king

    def select_piece(self, row, col):
        if self.selected_piece != 0:
            if (row, col) in self.valid_moves:
                if  not self.king.killable_king(self.board.board_list, row, col, self.selected_piece):
                    if self.selected_piece.is_king and (row,col) == (self.selected_piece.row, self.selected_piece.col-2):
                        self.selected_piece.moved = True
                        self.board.board_list[self.selected_piece.row][self.selected_piece.col-4].moved = True
                        self.board.board_list[row][col] = self.selected_piece
                        self.board.board_list[self.selected_piece.row][self.selected_piece.col-1] =  self.board.board_list[self.selected_piece.row][self.selected_piece.col-4]
                        self.board.board_list[self.selected_piece.row][self.selected_piece.col-1].col = 3 
                        self.board.board_list[self.selected_piece.row][self.selected_piece.col-4] = 0
                        self.board.board_list[self.selected_piece.row][self.selected_piece.col] = 0     
                        self.selected_piece.row = row
                        self.selected_piece.col = col
                        self.change_turn()
                    elif self.selected_piece.is_king and (row,col) == (self.selected_piece.row, self.selected_piece.col+2):
                        self.selected_piece.moved = True
                        self.board.board_list[self.selected_piece.row][self.selected_piece.col+3].moved = True
                        self.board.board_list[row][col] = self.selected_piece
                        self.board.board_list[self.selected_piece.row][self.selected_piece.col+1] =  self.board.board_list[self.selected_piece.row][self.selected_piece.col+3]
                        self.board.board_list[self.selected_piece.row][self.selected_piece.col+1].col = 5
                        self.board.board_list[self.selected_piece.row][self.selected_piece.col+3] = 0
                        self.board.board_list[self.selected_piece.row][self.selected_piece.col] = 0
                        self.selected_piece.row = row
                        self.selected_piece.col = col
                        self.change_turn()
                    
                    elif self.selected_piece.is_pawn: 
                        if self.selected_piece.row == 3 and self.selected_piece.colour == WHITE:
                            if self.board.board_list[row+1][col] != 0:
                                if self.board.board_list[row+1][col].is_pawn and self.board.board_list[row+1][col].enpassant:
                                    self.board.board_list[row][col] = self.selected_piece
                                    self.board.board_list[self.selected_piece.row][self.selected_piece.col] = 0
                                    self.board.board_list[row+1][col] = 0
                                    self.selected_piece.row = row
                                    self.selected_piece.col = col
                                    self.change_turn()
                                else:
                                    self.normal_move(row, col)                           
                            else:
                                self.normal_move(row, col)
                        elif self.selected_piece.row == 4 and self.selected_piece.colour == BLACK:
                            if self.board.board_list[row-1][col] != 0:
                                if self.board.board_list[row-1][col].is_pawn and self.board.board_list[row-1][col].enpassant:
                                    self.board.board_list[row][col] = self.selected_piece
                                    self.board.board_list[self.selected_piece.row][self.selected_piece.col] = 0
                                    self.board.board_list[row-1][col] = 0
                                    self.selected_piece.row = row
                                    self.selected_piece.col = col
                                    self.change_turn()
                                else:
                                    self.normal_move(row, col)   
                            else:
                                self.normal_move(row, col)
                        else:
                            if self.selected_piece.row+2 == row or self.selected_piece.row-2 == row:
                                self.selected_piece.enpassant = 2
                                self.enpassant_pieces.append(self.selected_piece)
                            self.normal_move(row, col)
                        
                    else:
                        self.normal_move(row, col)
                else:
                    self.selected_piece = 0
            else:
                self.selected_piece = 0
        else:
            self.valid_moves = []
            self.selected_piece = self.board.board_list[row][col]
            if self.selected_piece != 0 and self.selected_piece.colour == self.turn:
                self.valid_moves = self.selected_piece.get_valid_moves(self.board.board_list)
                if self.selected_piece.is_king:
                    self.selected_piece.can_you_castle(self.board.board_list)
            print(self.selected_piece)
           
    

    def change_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
            self.king = self.black_king
        else:
            self.turn = WHITE
            self.king = self.white_king

        if self.selected_piece.is_king or self.selected_piece.is_rook:
           
            self.selected_piece.moved = True
        
        self.selected_piece = 0
        self.valid_moves = []
        for piece in self.board.board_list[0]:
            if piece != 0 and piece.colour == WHITE:
                if piece.is_pawn:
                    piece = Queen(piece.row, piece.col, piece.colour)

        for piece in self.board.board_list[7]:
            if piece != 0 and piece.colour == BLACK:
                if piece.is_pawn:
                    piece = Queen(piece.row, piece.col, piece.colour)

        for pawn in self.enpassant_pieces:
            if pawn.enpassant == 0:
                self.enpassant_pieces.remove(pawn)
            else:
                pawn.enpassant = pawn.enpassant-1

            
    
                
    def normal_move(self, row, col):
        self.board.board_list[row][col] = self.selected_piece
        self.board.board_list[self.selected_piece.row][self.selected_piece.col] = 0
        self.selected_piece.row = row
        self.selected_piece.col = col
        self.change_turn()      
        
        



    def find_king(self, colour):
        for row in self.board.board_list:
            for piece in row:
                if piece != 0:
                    if piece.colour == colour:
                        if piece.is_king:
                            return piece
    
    
                            

        