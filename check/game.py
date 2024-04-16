import pygame
from .board import Board
from .constants import BLACK, WHITE
import copy
class Game():

    def __init__(self, win):
        self.win = win
        self.board = Board(self.win)
        self.valid_moves = []
        self.selected_piece = 0
        self.turn = WHITE
        self.black_king = self.find_king(BLACK)
        self.white_king = self.find_king(WHITE)
        self.king = self.white_king

    def select_piece(self, row, col):
        if self.selected_piece != 0:
            if (row, col) in self.valid_moves:
                if  not self.king.killable_king(self.board.board_list, row, col, self.selected_piece):
                    self.board.board_list[row][col] = self.selected_piece
                    self.board.board_list[self.selected_piece.row][self.selected_piece.col] = 0
                    self.selected_piece.row = row
                    self.selected_piece.col = col
                    self.change_turn()
                else:
                    self.selected_piece = 0
            else:
                self.selected_piece = 0
        else:
            self.valid_moves = []
            self.selected_piece = self.board.board_list[row][col]
            if self.selected_piece != 0 and self.selected_piece.colour == self.turn:
                self.valid_moves = self.selected_piece.get_valid_moves(self.board.board_list)
            print(self.selected_piece)
           
    

    def change_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
            self.king = self.black_king
        else:
            self.turn = WHITE
            self.king = self.white_king
        
        self.selected_piece = 0
        self.valid_moves = []
        



    def find_king(self, colour):
        for row in self.board.board_list:
            for piece in row:
                if piece != 0:
                    if piece.colour == colour:
                        if piece.is_king:
                            return piece
    
    
                            

        