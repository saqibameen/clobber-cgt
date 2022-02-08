import random
from clobber_1d import Clobber_1d
from game_basics import BLACK, WHITE, colorAsString
from transposition_table_simple import TranspositionTable
from boolean_negamax_tt import timed_solve as zobrist_solver
from negamax_no_hash import timed_solve as regular_hash_solver
from boolean_negamax_tt_ids import timed_solve as ids_solver
from boolean_negamax_tt_ids_no_heuristic import timed_solve as ids_no_heuristic_solver
import time
import sys

from clobber_1d_cy import Clobber_1d as Clobber_1dC
from transposition_table_simple_cy import TranspositionTable as TTC
# import boolean_negamax_tt_cy
from boolean_negamax_tt_cy import timed_solve as timed_solve_hashC


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
    # logs = open("logs.txt", "a")
    # Write the solver name, isWin, win_move, time_used and the number of nodes visited.
    # logs.write("{} {} {:.64f} {}\n".format(isWin, win_move, timeUsed, node_count))

    return isWin, win_move, timeUsed, node_count

def test_solve_with_ttC(state, player, time_limit, board, solver):
    tt = TTC()
    isWin, win_move, timeUsed, node_count =  solver(state, tt, time_limit, board)
    
    if(isWin == None):
        isWin = "?"
    elif((player == BLACK and isWin) or (player == WHITE and not isWin)):
        isWin = "B"
    elif((player == BLACK and not isWin) or (player == WHITE and isWin)):
        isWin = "W"

    # open logs file in append mode and create if does not exist.
    # logs = open("logs.txt", "a")
    # Write the solver name, isWin, win_move, time_used and the number of nodes visited.
    # logs.write("{} {} {:.64f} {}\n".format(isWin, win_move, timeUsed, node_count))

    return isWin, win_move, timeUsed, node_count

def worst_case_testing():
    # Generate random board. With a random number of 'B','W','.'.
    heuristic_ids, zob_hash, mm = [], [], []
    # results = open("results3.csv", "w")
    # results.write("Cython, Board_Size")
    # results.write("\n")
    for i in range(1, 31):
        # BW pattern upto i + 1
        pairs = (i+1) // 2
        board = "BW" * pairs
        board =  board[:i]

        print("board: ", board, " size: ", i)

        # state = Clobber_1d(board, BLACK)
        # state2 = Clobber_1d(board, BLACK)
        # state3 = Clobber_1d(board, BLACK)

        # # Playing the game, main
        # isWin, win_move, timeUsed, node_count = test_solve_with_tt(state, BLACK, 100, board, zobrist_solver)
        # isWin3, win_move3, timeUsed3, node_count3 = test_solve_with_tt(state3, BLACK, 100, board, ids_solver)
        # isWin2, win_move2, timeUsed2, node_count2 = test_solve_with_tt(state2, BLACK, 100, board, regular_hash_solver)
        # if win_move3 == "depthReached" or win_move3 == "timelimitReached":
        #     win_move3 = None

        # print("[Zobrist] isWin: ", isWin, " win_move: ", win_move, " timeUsed: ", timeUsed, " node_count: ", node_count)
        # print("[IDS] isWin3: ", isWin3, " win_move3: ", win_move3, " timeUsed3: ", timeUsed3, " node_count3: ", node_count3)
        # print("[MM] isWin2: ", isWin2, " win_move2: ", win_move2, " timeUsed2: ", timeUsed2, " node_count2: ", node_count2)
        # print()

        # if(isWin2 == "W" or isWin2 == "B" or (isWin != "W" and isWin != "B") or (isWin3 != "W" and isWin3 != "B")):
        #     assert isWin == isWin2 == isWin3 and win_move == win_move2 == win_move3
        
        state = Clobber_1d(board, WHITE)
        state2 = Clobber_1d(board, WHITE)
        state3 = Clobber_1d(board, WHITE)
        state4 = Clobber_1d(board, WHITE)
        state5 = Clobber_1dC(board, WHITE)

        isWin, win_move, timeUsed, node_count = test_solve_with_tt(state, WHITE, 100, board, zobrist_solver)
        isWin3, win_move3, timeUsed3, node_count3 = test_solve_with_tt(state3, WHITE, 100, board, ids_solver)
        isWin4, win_move4, timeUsed4, node_count4 = test_solve_with_tt(state4, WHITE, 100, board, ids_no_heuristic_solver)
        isWin5, win_move5, timeUsed5, node_count5 = test_solve_with_ttC(state5, WHITE, 100, board, timed_solve_hashC)
        isWin2, win_move2, timeUsed2, node_count2 = test_solve_with_tt(state2, WHITE, 100, board, regular_hash_solver)
        

        if win_move3 == "depthReached" or win_move3 == "timelimitReached":
            win_move3 = None

        if win_move4 == "depthReached" or win_move4 == "timelimitReached":
            win_move4 = None
        
        print("[Zobrist] isWin: ", isWin, " win_move: ", win_move, " timeUsed: ", timeUsed, " node_count: ", node_count)
        print("[Cython] isWin5: ", isWin5, " win_move5: ", win_move5, " timeUsed5: ", timeUsed5, " node_count5: ", node_count5)
        print("[IDS Heuristic] isWin3: ", isWin3, " win_move3: ", win_move3, " timeUsed3: ", timeUsed3, " node_count3: ", node_count3)
        print("[IDS No-Heuristic] isWin4: ", isWin4, " win_move4: ", win_move4, " timeUsed4: ", timeUsed4, " node_count4: ", node_count4)
        print("[MM] isWin2: ", isWin2, " win_move2: ", win_move2, " timeUsed2: ", timeUsed2, " node_count2: ", node_count2)
        print()

        if(isWin2 == "W" or isWin2 == "B" or (isWin != "W" and isWin != "B") or (isWin3 != "W" and isWin3 != "B") or (isWin4 != "W" and isWin4 != "B")):
            assert isWin == isWin2 == isWin3 == isWin4 and win_move == win_move2 == win_move3 == win_move4

        # results.write(f"{timeUsed5},{len(board)}")
        # results.write("\n")
    
    # results.close()


def random_test_suit_testing():
    # Generate random board. With a random number of 'B','W','.' of length 64.
    for _ in range(50):
        board = ""
        for i in range(55):
            # Randomly select from ["W", "B", "."]
            board += random.choice(["W", "B", "."])

        # board = "BW...WBBBW.WBB..WWWWWW.WBBWWW.WWWBBW.WWB.BWBW.BBBBW.BWBB..BWWWW."
        # print("board: ", board)
        # state = Clobber_1d(board, BLACK)
        # state2 = Clobber_1d(board, BLACK)
        # state3 = Clobber_1d(board, BLACK)

        # # Playing the game, main
        # isWin, win_move, timeUsed, node_count = test_solve_with_tt(state, BLACK, 100, board, zobrist_solver)
        # isWin3, win_move3, timeUsed3, node_count3 = test_solve_with_tt(state3, BLACK, 100, board, ids_solver)
        # isWin2, win_move2, timeUsed2, node_count2 = test_solve_with_tt(state2, BLACK, 100, board, regular_hash_solver)
        # if win_move3 == "depthReached" or win_move3 == "timelimitReached":
        #     win_move3 = None

        # print("[Zobrist] isWin: ", isWin, " win_move: ", win_move, " timeUsed: ", timeUsed, " node_count: ", node_count)
        # print("[IDS] isWin3: ", isWin3, " win_move3: ", win_move3, " timeUsed3: ", timeUsed3, " node_count3: ", node_count3)
        # print("[MM] isWin2: ", isWin2, " win_move2: ", win_move2, " timeUsed2: ", timeUsed2, " node_count2: ", node_count2)
        # print()

        # if(isWin2 == "W" or isWin2 == "B" or (isWin != "W" and isWin != "B") or (isWin3 != "W" and isWin3 != "B")):
        #     assert isWin == isWin2 == isWin3 and win_move == win_move2 == win_move3
        
     
        state = Clobber_1d(board, WHITE)
        state2 = Clobber_1d(board, WHITE)
        state3 = Clobber_1d(board, WHITE)
        state4 = Clobber_1d(board, WHITE)
        state5 = Clobber_1dC(board, WHITE)

        isWin, win_move, timeUsed, node_count = test_solve_with_tt(state, WHITE, 100, board, zobrist_solver)
        isWin3, win_move3, timeUsed3, node_count3 = test_solve_with_tt(state3, WHITE, 100, board, ids_solver)
        isWin4, win_move4, timeUsed4, node_count4 = test_solve_with_tt(state4, WHITE, 100, board, ids_no_heuristic_solver)
        isWin5, win_move5, timeUsed5, node_count5 = test_solve_with_ttC(state5, WHITE, 100, board, timed_solve_hashC)
        isWin2, win_move2, timeUsed2, node_count2 = test_solve_with_tt(state2, WHITE, 100, board, regular_hash_solver)
        

        if win_move3 == "depthReached" or win_move3 == "timelimitReached":
            win_move3 = None

        if win_move4 == "depthReached" or win_move4 == "timelimitReached":
            win_move4 = None
        
        print("[Zobrist] isWin: ", isWin, " win_move: ", win_move, " timeUsed: ", timeUsed, " node_count: ", node_count)
        print("[Cython] isWin5: ", isWin5, " win_move5: ", win_move5, " timeUsed5: ", timeUsed5, " node_count5: ", node_count5)
        print("[IDS Heuristic] isWin3: ", isWin3, " win_move3: ", win_move3, " timeUsed3: ", timeUsed3, " node_count3: ", node_count3)
        print("[IDS No-Heuristic] isWin4: ", isWin4, " win_move4: ", win_move4, " timeUsed4: ", timeUsed4, " node_count4: ", node_count4)
        print("[MM] isWin2: ", isWin2, " win_move2: ", win_move2, " timeUsed2: ", timeUsed2, " node_count2: ", node_count2)
        print()

        if(isWin2 == "W" or isWin2 == "B" or (isWin != "W" and isWin != "B") or (isWin3 != "W" and isWin3 != "B") or (isWin4 != "W" and isWin4 != "B")):
            assert isWin == isWin2 == isWin3 == isWin4 and win_move == win_move2 == win_move3 == win_move4


# worst_case_testing()
random_test_suit_testing()