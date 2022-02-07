# Cmput 455 sample code
# Boolean Negamax
# Written by Martin Mueller

import time
from game_basics import colorAsString, isBlackWhite, opponent


win_move = None
start = time.process_time()

def negamaxBoolean(state, time_limit):
    global win_move, node_count, start
    if state.endOfGame():
        return state.staticallyEvaluateForToPlay(), win_move
    legalmoves = state.legalMoves() 
    for m in legalmoves:
        state.play(m)
        success = not negamaxBoolean(state, time_limit)[0]
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
    return win, m, timeUsed, 1 # sending constant
