# Cmput 455 sample code
# Boolean Negamax
# Written by Martin Mueller

import random
import time

from game_basics import BLACK, COLOR_MAPPING, NUMBER_TO_COLOR, colorAsString, isBlackWhite, opponent

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
        changed_position = hash_list[NUMBER_TO_COLOR[state.opp_color()]][m[1]]
        print(changed_position)
        current = 2 + 1 - state.opp_color()
        updated_hash = board_hash ^ changed_position ^ hash_list[NUMBER_TO_COLOR[current]][m[1]] ^ hash_list[NUMBER_TO_COLOR[current]][m[0]]

        # print(updated_hash, changed_position, m, state.opp_color())
        # state.print()
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
        hash_list = {'B': [], 'W': []}
        for index in range(len(board)):
            hash_B = random.randint(1, 2**63 - 1) + index + COLOR_MAPPING['B']
            hash_w = random.randint(1, 2**63 - 1) + index + COLOR_MAPPING['W'] 
            hash_list['B'].append(hash_B)
            hash_list['W'].append(hash_w)

        # Check all the entries are unique.
        assert len(hash_list['B']) == len(set(hash_list['B']))
        assert len(hash_list['W']) == len(set(hash_list['W']))

        return hash_list

# Initial board hash
def generate_board_hash(board, hash_list): 
    # Calculate hash code
    hash_code = 0
    for index, value in enumerate(board):
        if value == '.': continue
        hash_code = hash_code ^ hash_list[value][index]
    return hash_code