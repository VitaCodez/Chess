import pygame
from .board import Board
from .constants import BLACK, WHITE
class Game():

    def __init__(self, win):
        self.win = win
        self.board = Board(self.win)
        self.valid_moves = []
        self.selected_piece = 0
        self.turn = WHITE
        self.enemy_moves =[]

    def select_piece(self, row, col):
        if self.selected_piece != 0:
            
                
            if (row, col) in self.valid_moves:
                self.board.board_list[row][col] = self.selected_piece
                self.board.board_list[self.selected_piece.row][self.selected_piece.col] = 0
                self.selected_piece.row = row
                self.selected_piece.col = col
                self.change_turn()
            else:
                self.selected_piece = 0

        else:
            self.valid_moves = []
            self.enemy_moves = []
            self.selected_piece = self.board.board_list[row][col]
            if self.selected_piece != 0 and self.selected_piece.colour == self.turn:
                if self.selected_piece.is_king:
                    for row in self.board.board_list:
                        for piece in row:
                            if piece != 0:
                                if piece.colour != self.selected_piece.colour and not piece.is_king:
                                    self.enemy_moves.append(piece.get_valid_moves(self.board.board_list))
                    self.valid_moves = self.selected_piece.get_valid_moves(self.board.board_list, self.enemy_moves)
                else:
                    self.valid_moves = self.selected_piece.get_valid_moves(self.board.board_list)
            print(self.selected_piece)
    

    def change_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE
        self.selected_piece = 0
        self.valid_moves = []
        self.enemy_moves = []

            

        