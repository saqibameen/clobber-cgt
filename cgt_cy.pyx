# Cmput 455 sample code
# Boolean Negamax
# Written by Martin Mueller

import time
from clobber_1d_cy import Clobber_1d
from zero import zeros_db
# from newdb import endgame_db

cdef tuple win_move = None
cdef unsigned long node_count = 0
cdef double start = time.process_time()

cdef saqib_board_CGT(state):
    # board = state.board
    board = state.getBoard()
    cdef list sub_games = []

    cdef list game = []
    cdef list game_inverse = []

    # L_game = 0
    # R_game = 0

    is_game_m_n = True
    is_already_flipped = False

    cdef unsigned short int last_index = len(board) - 1
    for index, value in enumerate(board):
        if value == 0 or index == last_index:
            if(index == last_index and value != 0):
                game.append(value)
                game_inverse.append(2 + 1 - value)

            if(len(game) > 3 and is_game_m_n and is_already_flipped):
                if (game[len(game) - 1] != game[len(game) - 2]):
                    is_game_m_n = False
            else:
                is_game_m_n = False
            
            if is_game_m_n:
                is_game_m_n = True
                is_already_flipped = False
            elif game_inverse in sub_games:
                sub_games.remove(game_inverse)
            elif game_inverse[::-1] in sub_games:
                sub_games.remove(game_inverse[::-1])
            elif len(game) > 1 and len(set(game)) != 1 and tuple(game) not in zeros_db:
                sub_games.append(game)
                # game_tuple = tuple(game)
                # if(endgame_db.get(game_tuple) == 'L'):
                #     L_game += 1
                # elif(endgame_db.get(game_tuple) == 'R'):
                #     R_game += 1

            game = []
            game_inverse = []
            is_game_m_n = True
            is_already_flipped = False
        else:
            game.append(value)
            game_inverse.append(2 + 1 - value)

            if(len(game) > 1 and is_game_m_n and game[len(game) - 1] != game[len(game) - 2]):
                if(len(game) < 3): is_game_m_n = False
                if(not is_already_flipped): is_already_flipped = True
                else: is_game_m_n = False
   
    cdef list combined_games = []

    # if(L_game == len(sub_games) and len(sub_games) !=0):
    #     sub_games = [[1,1,2]]
    # elif(R_game == len(sub_games) and len(sub_games) !=0):
    #     sub_games = [[2,2,1]]

    for sub_game in sub_games:
        combined_games += sub_game + [0]

    if(len(combined_games) > 1):
        del combined_games[-1]

    new_state = Clobber_1d(combined_games, state.getToPlay(), state.getMoves())
    return new_state

cdef storeResult(tt, state, result):
    tt.store(state.code(), result)
    return result

cdef negamaxBoolean(state, tt, time_limit):
    global win_move, node_count, start
    node_count += 1
    result = tt.lookup(state.code())
    if result != None:
        return result, win_move
    if state.endOfGame():
        result = False
        return storeResult(tt, state, result), win_move
    moves = state.legalMoves()
    for m in moves:
        state.play(m)
        new_state = saqib_board_CGT(state)
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
    global start, node_count
    start = time.process_time() 
    node_count = 0
    new_state = saqib_board_CGT(state)
    win, m = negamaxBoolean(new_state, tt, time_limit)
    timeUsed = time.process_time() - start
    return win, m, timeUsed, node_count