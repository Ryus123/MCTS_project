#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script contains the code
of the game 'Order and Chaos'.
sources : 
    - https://en.wikipedia.org/wiki/Order_and_Chaos
    - https://ludii.games/details.php?keyword=Order%20and%20Chaos
    - https://www.lamsade.dauphine.fr/~cazenave/papers/OptimizingPlayouts.pdf

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
    
    def verif_array(self, array):
        if (np.char.count(array, '-').sum() <= 1) and (len(np.unique(array[:5]))==1 or len(np.unique(array[1:]))==1):
            return True
        else:
            return False
        
    def win(self):
        # Horizontal win
        for row in self.board:
            if self.verif_array(row) == True:
                return True
            
        # Vertical win
        for col in self.board.T:
            if self.verif_array(col) == True:
                return True
            
        # Diagonal win
        for i in [-1, 0, 1]:
            diag = np.diagonal(self.board, offset=i)
            if (len(diag)==6) and (self.verif_array(diag) == True) or (np.char.count(diag, '-').sum() < 1) and (len(np.unique(diag))==1):
                return True
            
            diag_opposite = np.flipud(self.board).diagonal(offset=i)
            if (len(diag_opposite)==6) and (self.verif_array(diag_opposite) == True) or (np.char.count(diag_opposite, '-').sum() < 1) and (len(np.unique(diag_opposite))==1):
                return True
            
        return False
        
        
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
        return "\n".join(" ".join(row) for row in self.board)
        
    def play (self, move:Move):
        change_player = {'Order' : 'Chaos', 'Chaos' : 'Order'}
        if move.valid(self):
            self.board[move.x][move.y] = move.symbol
            self.turn = change_player[self.turn]
            self.nb_moves += 1

    def playout (self):
        pass
    
    
# Test example
game = Board()
game.play(Move(0, 0, 'X'))
game.play(Move(1, 1, 'X'))
game.play(Move(2, 2, 'O'))
game.play(Move(3, 3, 'X'))
game.play(Move(4, 4, 'X'))
print(game)
print("Win:", game.win())