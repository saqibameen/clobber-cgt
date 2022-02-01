# Cmput 455 sample code
# Boolean Negamax
# Written by Martin Mueller

import time
from game_basics import colorAsString, isBlackWhite, opponent

def negamaxBoolean(state):
    if state.endOfGame():
        return state.staticallyEvaluateForToPlay()
    for m in state.legalMoves():
        state.play(m)
        success = not negamaxBoolean(state)
        state.undoMove()
        if success:
            return True
    return False

def timed_solve(state): 
    start = time.process_time()
    win = negamaxBoolean(state)
    timeUsed = time.process_time() - start
    return win, timeUsed
