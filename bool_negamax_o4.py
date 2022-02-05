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

def negamaxBoolean(state, tt, time_limit, moves):
    global win_move, node_count, start
    node_count += 1
    result = tt.lookup(state.code())
    if result != None:
        return result, win_move
    if state.endOfGame():
        result = state.staticallyEvaluateForToPlay()
        return storeResult(tt, state, result), win_move

    # print(f"Opponenet: {colorAsString(state.opp_color())}")
    # print(f"legal moves: {state.legalMoves()}")
    # state.print()
    
    for m in state.legalMovesO4(moves):
        # print(f"Move: {m}")
        state.play(m)
        # reverse the legal moves for opponent
        moves = [(m[1], m[0]) for m in moves]

        success = not negamaxBoolean(state, tt, time_limit, moves)[0]
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
    moves = []
    start = time.process_time()
    win, m = negamaxBoolean(state, tt, time_limit, moves)
    timeUsed = time.process_time() - start
    return win, m, timeUsed, node_count