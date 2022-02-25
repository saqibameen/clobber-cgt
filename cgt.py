# Cmput 455 sample code
# Boolean Negamax
# Written by Martin Mueller

import time
from game_basics import colorAsString, isBlackWhite, opponent
from clobber_1d import Clobber_1d


win_move = None
node_count = 0
start = time.process_time()

# TODO: Do CGT updates
def update_board_CGT(state):
    inverse_board = [(2+1-x) if x != 0 else 0 for x in state.board]
    # print(f"real: {state.board}")
    # print(f"inve: {inverse_board}")

    sub_games = "".join([str(x) for x in state.board]).split("0")
    inverse_sub_games = "".join([str(x) for x in inverse_board]).split("0")
    sub_games = [x for x in sub_games if x != ""]
    inverse_sub_games = [x for x in inverse_sub_games if x != ""]

    to_remove = []
    for i in range(len(sub_games)):
        inverse_subgame = inverse_sub_games[i]
        if(inverse_subgame in sub_games):
            to_remove.append(sub_games[i])
            to_remove.append(inverse_subgame)

        if(sub_games[i] in sub_games[i+1:]):
            to_remove.append(sub_games[i])

    new_sub_game = []
    # Removing moves
    for game in sub_games:
        if(game not in to_remove):
            new_sub_game.append(game)

    
    new_sub_game = [int(x) for x in list('0'.join(new_sub_game))]

    for i in range(len(state.board) - len(new_sub_game)):
        new_sub_game.append(0)

    new_state = Clobber_1d(new_sub_game, state.toPlay, state.moves)
    return new_state

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
        
        # print(f"Move: {m}")
        state.play(m)
        new_state = update_board_CGT(state)
        success = not negamaxBoolean(new_state, tt, time_limit)[0]
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