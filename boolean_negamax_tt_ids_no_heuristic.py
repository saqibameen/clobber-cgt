import random
import time
from game_basics import BLACK, COLOR_MAPPING, colorAsString, isBlackWhite, opponent

win_move = None
node_count = 0
start = time.process_time()

def storeResult(tt, board_hash, result):
    tt.store(board_hash, result)
    return result

def negamaxBoolean(state, tt, time_limit, board_hash, hash_list, current_legal_moves, depth):
    global win_move, node_count, start
    node_count += 1
    result = tt.lookup(board_hash)
    
    if result != None:
        return result, None

    if len(current_legal_moves) == 0:
        return storeResult(tt, board_hash, False), win_move
    
    elif depth == 0:
        return None, "depthReached"

    for m in current_legal_moves:
        current = state.toPlay
        opposite =  2 + 1 - current
        opp_moves = state.get_opponents_moves(current_legal_moves, m, current, opposite)

        changed_position = hash_list[opposite-1][m[1]]
        updated_hash = board_hash ^ changed_position ^ hash_list[current-1][m[1]] ^ hash_list[current-1][m[0]]
        state.play(m)
        success, condition = negamaxBoolean(state, tt, time_limit, updated_hash, hash_list, opp_moves, depth-1)
        state.undoMove()
        
        if(success == None and condition == "depthReached"):
            return None, "depthReached"
        
        # if(success == None and condition == "timelimitReached"):
        #     return None, "timelimitReached"

        success = not success
        timeUsed = time.process_time() - start        
        if(timeUsed >= time_limit):
            win_move = None
            return None, "timelimitReached"

        elif success:
            win_move = m
            return storeResult(tt, board_hash, True), win_move

    return storeResult(tt, board_hash, False), None

def timed_solve(state, tt, time_limit, board): 
    global start
    start = time.process_time()
    hash_list = generate_hash(board)
    board_hash = generate_board_hash(board, hash_list)
    current_legal_moves, opp_legal_moves = state.legalMovesForBoth()
    max_depth = 1000
    for depth in range(2, max_depth, 2):
        win, m = negamaxBoolean(state, tt, time_limit, 
                                    board_hash, hash_list, 
                                    current_legal_moves, depth)
        
        if m != "depthReached" and m != "timelimitReached":
            break
    
    timeUsed = time.process_time() - start
    return win, m, timeUsed, node_count

def generate_hash(board):
        hash_list = [[],[]]
        for _ in range(len(board)):
            hash_list[0].append(random.randint(1, 2**64 - 1))
            hash_list[1].append(random.randint(1, 2**64 - 1))

        # Check all the entries are unique.
        assert len(hash_list[0]) == len(set(hash_list[0]))
        assert len(hash_list[1]) == len(set(hash_list[1]))

        return hash_list

# Initial board hash
def generate_board_hash(board, hash_list): 
    # Calculate hash code
    hash_code = 0
    for index, value in enumerate(board):
        if value == '.': continue
        hash_code = hash_code ^ hash_list[COLOR_MAPPING[value]-1][index]
    return hash_code