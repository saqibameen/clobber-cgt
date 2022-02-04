# Cmput 455 sample code
# Boolean Negamax
# Written by Martin Mueller

import random
import time
from game_basics import COLOR_MAPPING, colorAsString, isBlackWhite, opponent

win_move = None
node_count = 0
start = time.process_time()

def storeResult(tt, board_hash, result):
    tt.store(board_hash, result)
    return result

def negamaxBoolean(state, tt, time_limit, board_hash, hash_list):
    global win_move, node_count, start
    node_count += 1
    result = tt.lookup(board_hash)
    if result != None:
        return result, win_move
    if state.endOfGame():
        result = state.staticallyEvaluateForToPlay()
        return storeResult(tt, board_hash, result), win_move
    for m in state.legalMoves():
        state.play(m)
        changed_state = m[1]
        changed_position = hash_list[changed_state]
        updated_hash = board_hash ^ changed_position
        success = not negamaxBoolean(state, tt, time_limit, updated_hash, hash_list)[0]
        state.undoMove()
        timeUsed = time.process_time() - start
        if(timeUsed >= time_limit):
            win_move = None
            return None, None
        else:
            if success:
                win_move = m
                return storeResult(tt, board_hash, True), win_move
    return storeResult(tt, board_hash, False), None

def timed_solve(state, tt, time_limit, board): 
    global start
    start = time.process_time()
    hash_list = generate_hash(board)
    board_hash = generate_board_hash(board, hash_list)

    win, m = negamaxBoolean(state, tt, time_limit, board_hash, hash_list)
    timeUsed = time.process_time() - start
    return win, m, timeUsed, node_count

def generate_hash(board):
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
def generate_board_hash(board, hash_list): 
    # Calculate hash code
    hash_code = 0
    for hash in hash_list:
        hash_code = hash_code ^ hash
    return hash_code