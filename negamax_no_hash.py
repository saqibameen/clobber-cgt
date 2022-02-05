# Cmput 455 sample code
# Boolean Negamax
# Written by Martin Mueller

import time
from game_basics import colorAsString, isBlackWhite, opponent

win_move = None
node_count = 0
start = time.process_time()

def storeResult(tt, state, result):
    tt.store(state.code(), result)
    return result

def negamaxBoolean(state, tt, time_limit):
    global win_move, node_count, start
    node_count += 1
    result = tt.lookup(state.code())
    if result != None:
        return result, win_move
    if state.endOfGame():
        result = state.staticallyEvaluateForToPlay()
        return storeResult(tt, state, result), win_move
    for m in state.legalMoves():
        state.play(m)
        success = not negamaxBoolean(state, tt, time_limit)[0]
        state.undoMove()
        timeUsed = time.process_time() - start
        if(timeUsed >= time_limit):
            win_move = None
            return None, None
        else:
            if success:
                win_move = m
                return storeResult(tt, state, True), win_move
    return storeResult(tt, state, False), None


def timed_solve(state, tt, time_limit, _): 
    global start
    start = time.process_time()
    win, m = negamaxBoolean(state, tt, time_limit)
    timeUsed = time.process_time() - start
    return win, m, timeUsed, node_count