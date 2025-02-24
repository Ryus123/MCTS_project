#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script contains the code
of the game 'Order and Chaos'.
sources : 
    - https://en.wikipedia.org/wiki/Order_and_Chaos
    - https://ludii.games/details.php?keyword=Order%20and%20Chaos

Created on 02/18/2025.

Last update 02/24/2025.

@authors: 
    - M. AALABOU
    - E. DELAR
"""

# =============================================================================
# Imports
# ============================================================================= 
import numpy as np
from copy import deepcopy
# =============================================================================
# Inputs
# ============================================================================= 
Dx = 6
Dy = 6
Empty = '-'
# =============================================================================
# Classes
# ============================================================================= 

# Class Move for Order & Chaos
class Move(object):
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
        
    def valid (self, board):
        # Move in the board
        if self.x >= Dx or self.y >= Dy or self.x < 0 or self.y <0:
            return False
        # Move in a free space
        if board.board[self.x][self.y] != Empty:
            return False
        
        return True
    
    
# Class Board to play Order & Chaos
class Board(object):
    def __init__(self):
        #self.history = {'Order' : [], 'Chaos' : []}
        self.turn = 'Order' #Order always start the game
        self.board = [[Empty for _ in range(Dx)] for _ in range(Dy)]
        self.board = np.array(self.board)
        self.nb_moves = 0
        
    def legalMoves(self):
        moves = []
        for i in range (0, Dx):
            for j in range (0, Dy):
                for symb in ['X', 'O']:
                    m = Move (i, j, symb)
                    if m.valid (self):
                        moves.append (m)
                    
        return moves
    
    def win(self):
        # Minimum 5 moves for player 1 to win
        if self.nb_moves < 9 :
            return False
        # Horizontal win
        
        # Vertical win
        
        # Diagonal win
        
    def draw(self):
        if self.nb_moves < Dx*Dy:
            return False
        if self.nb_moves >= Dx*Dy and not self.win():
            return True
        return False
        
    def terminal(self):
        if not self.win():
            return False
        if not self.draw():
            return False
        return True
    
    def __repr__(self):
        print(self.board)
        
    def play (self, move):
        change_player = {'Order' : 'Chaos', 'Chaos' : 'Order'}
        self.board[move.x][move.y] = move.symbol
        self.turn = change_player[self.turn]
        self.nb_moves += 1

    def playout (self):
        pass