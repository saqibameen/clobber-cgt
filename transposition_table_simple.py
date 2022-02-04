# Cmput 455 sample code
# Simple transposition table for TicTacToe solver
# This is much slower than an array-based table
# which is used in competitive programs
# Written by Martin Mueller

import random


COLOR_MAPPING = {
    ".": 0,
    "B": 1,
    "W": 2
}
class TranspositionTable():
# Table is stored in a dictionary, with board code as key, 
# and minimax score as the value

    # Calculate a random has for each (index, value) pair. 0 for empty.
    def generate_hash(self, board):
        hash_list = []
        for index, value in enumerate(board):
            # if i == ".", append 0
            if value == ".":
                hash_list.append(0)
            else:
                # Generate random hash based on (index, value) pair
                # 64-bit random hash
                hash = random.randint(1, 2**64 - 1) + index + (COLOR_MAPPING[value] * 2) 
                hash_list.append(hash)
        return hash_list

    # Initial board hash
    def board_hash(self, board, hash_list): 
        # Calculate hash code
        hash_code = 0
        for hash in hash_list:
            hash_code = hash_code ^ hash
        return hash_code

    # Empty dictionary
    def __init__(self):
        self.table = {}

    # Used to print the whole table with print(tt)
    def __repr__(self):
        return self.table.__repr__()
        
    def store(self, code, score):
        self.table[code] = score
    
    # Python dictionary returns 'None' if key not found by get()
    def lookup(self, code):
        return self.table.get(code)