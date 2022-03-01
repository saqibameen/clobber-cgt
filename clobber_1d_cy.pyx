# Cmput 655 sample code
# 1xn Clobber game board, rules, and a random game simulator
# Includes the code() method to compute a "hash code" for 
# use in a transposition table (This is actually a perfect code, 
# not a hash code, since the state space is so small)
# Written by Martin Mueller

import random
from typing import overload
from game_basics import EMPTY, BLACK, WHITE, isEmptyBlackWhite, opponent
import heapq

cdef class Clobber_1d(object):
# Board is stored in 1-d array of EMPTY, BLACK, WHITE

    cdef list init_board
    cdef list board
    cdef list moves
    cdef toPlay

    @classmethod
    def standard_board(cls, size):
        pairs = (size+1) // 2
        board = [BLACK, WHITE] * pairs
        return board[:size]
            
    @classmethod
    def custom_board(cls, start_position): # str of B, W, E or .
        color_map = { 'B': BLACK, 'W': WHITE, 'E': EMPTY, '.': EMPTY }
        board = []
        for c in start_position:
            board.append(color_map[c])
        return board
    
    @classmethod
    def to_string(cls, board):
        char_map = { BLACK: 'B', WHITE: 'W', EMPTY: '.'}
        s = ""
        for p in board:
            s += char_map[p]
        return s
        

    def getToPlay(self):
        return self.toPlay
    
    def getBoard(self):
        return self.board

    def getMoves(self):
        return self.moves

    def __init__(self, start_position, first_player = WHITE, moves = None): 
        # we take either a board size for standard "BWBW...", 
        # or a custom start string such as "BWEEWWB"
        if moves == None:
            if type(start_position) == int:
                self.init_board = Clobber_1d.standard_board(start_position)
            else:
                assert type(start_position) == str
                self.init_board = Clobber_1d.custom_board(start_position)
            self.resetGame(first_player)
        else: 
            self.board = start_position
            self.toPlay = first_player
            self.moves = moves

    

    def resetGame(self, first_player):
        self.board = self.init_board
        self.toPlay = first_player
        self.moves = []

    def resetToMoveNumber(self, moveNr):
        numUndos = self.moveNumber() - moveNr
        assert numUndos >= 0
        for _ in range(numUndos):
            self.undoMove()
        assert self.moveNumber() == moveNr

    def opp_color(self):
        return opponent(self.toPlay)
        
    def switchToPlay(self):
        self.toPlay = self.opp_color()

    cpdef void play(self, move):
        cdef unsigned int src = move[0]
        cdef unsigned int to = move[1]
        
        assert self.board[src] == self.toPlay
        assert self.board[to] == self.opp_color()
        self.board[src] = EMPTY
        self.board[to] = self.toPlay
        self.moves.append(move)
        self.switchToPlay()

    cpdef void undoMove(self):
        self.switchToPlay()
        src, to = self.moves.pop()
        assert self.board[src] == EMPTY
        assert self.board[to] == self.toPlay
        self.board[to] = self.opp_color()
        self.board[src] = self.toPlay
    
    def winner(self):
        if self.endOfGame():
            return self.opp_color()
        else:
            return EMPTY

    def staticallyEvaluateForToPlay(self):
        winColor = self.winner()
        return winColor == self.toPlay

    def moveNumber(self):
        return len(self.moves)

    def endOfGame(self):
        return len(self.legalMoves()) == 0

    cpdef list legalMoves(self):
        # To do: this is super slow. Should keep track of moves
        cdef list moves = []
        cdef opp = self.opp_color()
        cdef unsigned int last = len(self.board) - 1
        for i, p in enumerate(self.board):
            if p == self.toPlay:
                if i > 0 and self.board[i-1] == opp:
                    moves.append((i, i-1))
                if i < last and self.board[i+1] == opp:
                    moves.append((i, i+1))
        if(len(moves) > 3):
            moves[0], moves[len(moves)//2] = moves[len(moves)//2], moves[0]

        return moves


    cpdef list legalMovesOriginal(self):
        # To do: this is super slow. Should keep track of moves
        cdef list moves = []
        cdef opp = self.opp_color()
        cdef unsigned int last = len(self.board) - 1
        for i, p in enumerate(self.board):
            if p == self.toPlay:
                if i > 0 and self.board[i-1] == opp:
                    moves.append((i, i-1))
                if i < last and self.board[i+1] == opp:
                    moves.append((i, i+1))

        return moves

    def code(self):
        # To do: this is super slow. Should keep track of code
        c = 0
        for color in self.board:
            c = 3*c + color
        return 2*c + self.toPlay - 1 # BLACK = 1, WHITE = 2

    ##def void print(self):
        ##print(Clobber_1d.to_string(self.board))