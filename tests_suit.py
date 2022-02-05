import random
from clobber_1d import Clobber_1d
from game_basics import BLACK, WHITE, colorAsString
from transposition_table_simple import TranspositionTable
from boolean_negamax_tt import timed_solve as zobrist_solver
from negamax_no_hash import timed_solve as regular_hash_solver
import time
import sys

def test_solve_with_tt(state, player, time_limit, board, solver):
    tt = TranspositionTable()
    isWin, win_move, timeUsed, node_count =  solver(state, tt, time_limit, board)
    
    if(isWin == None):
        isWin = "?"
    elif((player == BLACK and isWin) or (player == WHITE and not isWin)):
        isWin = "B"
    elif((player == BLACK and not isWin) or (player == WHITE and isWin)):
        isWin = "W"

    # open logs file in append mode and create if does not exist.
    logs = open("logs.txt", "a")
    # Write the solver name, isWin, win_move, time_used and the number of nodes visited.
    logs.write("{} {} {:.64f} {}\n".format(isWin, win_move, timeUsed, node_count))

    return isWin, win_move, timeUsed, node_count

def worst_case_testing():
    # Generate random board. With a random number of 'B','W','.'.
    for i in range(1, 15):
        board = "BW" * i
        print("board: ", board)
        state = Clobber_1d(board, BLACK)
        state2 = Clobber_1d(board, BLACK)

        # Playing the game, main
        isWin, win_move, timeUsed, node_count = test_solve_with_tt(state, BLACK, 100, board, zobrist_solver)
        isWin2, win_move2, timeUsed2, node_count2 =test_solve_with_tt(state2, BLACK, 100, board, regular_hash_solver)

        if(isWin != None):
            assert isWin == isWin2 and win_move == win_move2 and node_count == node_count2
        else:
            assert isWin == isWin2 and win_move == win_move2

        
        state = Clobber_1d(board, WHITE)
        state2 = Clobber_1d(board, WHITE)
        isWin, win_move, timeUsed, node_count = test_solve_with_tt(state, WHITE, 100, board, zobrist_solver)
        isWin2, win_move2, timeUsed2, node_count2 =test_solve_with_tt(state2, WHITE, 100, board, regular_hash_solver)

        if(isWin != None):
            assert isWin == isWin2 and win_move == win_move2 and node_count == node_count2
        else:
            assert isWin == isWin2 and win_move == win_move2

# hashing_correctness_test()


def random_test_suit_testing():
    # Generate random board. With a random number of 'B','W','.' of length 64.
    for _ in range(1):
        board = ""
        for i in range(64):
            # Randomly select from ["W", "B", "."]
            board += random.choice(["W", "B", "."])

        board = "BW...WBBBW.WBB..WWWWWW.WBBWWW.WWWBBW.WWB.BWBW.BBBBW.BWBB..BWWWW."
        print("board: ", board)
        state = Clobber_1d(board, BLACK)
        state2 = Clobber_1d(board, BLACK)

        # Playing the game, main
        isWin, win_move, timeUsed, node_count = test_solve_with_tt(state, BLACK, 100, board, zobrist_solver)
        isWin2, win_move2, timeUsed2, node_count2 =test_solve_with_tt(state2, BLACK, 100, board, regular_hash_solver)

        print("isWin: ", isWin, " win_move: ", win_move, " timeUsed: ", timeUsed, " node_count: ", node_count)
        print("isWin2: ", isWin2, " win_move2: ", win_move2, " timeUsed2: ", timeUsed2, " node_count2: ", node_count2)

        if(isWin == "W" or isWin == "B"):
            assert isWin == isWin2 and win_move == win_move2 and node_count == node_count2
        else:
            assert isWin == isWin2 and win_move == win_move2

        
        state = Clobber_1d(board, WHITE)
        state2 = Clobber_1d(board, WHITE)
        isWin, win_move, timeUsed, node_count = test_solve_with_tt(state, WHITE, 100, board, zobrist_solver)
        isWin2, win_move2, timeUsed2, node_count2 =test_solve_with_tt(state2, WHITE, 100, board, regular_hash_solver)

        print("isWin: ", isWin, " win_move: ", win_move, " timeUsed: ", timeUsed, " node_count: ", node_count)
        print("isWin2: ", isWin2, " win_move2: ", win_move2, " timeUsed2: ", timeUsed2, " node_count2: ", node_count2)
        
        if(isWin == "W" or isWin == "B"):
            assert isWin == isWin2 and win_move == win_move2 and node_count == node_count2
        else:
            assert isWin == isWin2 and win_move == win_move2


# worst_case_testing()
random_test_suit_testing()