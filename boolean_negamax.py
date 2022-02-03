# Cmput 455 sample code
# Boolean Negamax
# Written by Martin Mueller

import time
from game_basics import colorAsString, isBlackWhite, opponent


win_move = None
node_count = 0
start = time.process_time()

def negamaxBoolean(state, time_limit):
    global win_move, node_count, start
    node_count += 1

    if state.endOfGame():
        return state.staticallyEvaluateForToPlay(), win_move
    for m in state.legalMoves():
        state.play(m)
        success = not negamaxBoolean(state, time_limit)[0]
        timeUsed = time.process_time() - start
        if(timeUsed >= time_limit):
            win_move = None
            return None, None
        else:
            state.undoMove()
            if success:
                win_move = m
                return True, win_move
    return False, None

def timed_solve(state, time_limit): 
    global start
    start = time.process_time()
    win, m = negamaxBoolean(state, time_limit)
    timeUsed = time.process_time() - start
    return win, m, timeUsed, node_count
