import random
from clobber_1d import Clobber_1d
from game_basics import BLACK, WHITE, colorAsString
from transposition_table_simple import TranspositionTable
from negamax_tt_martin import timed_solve as martin_timed_solve
from cgt import timed_solve as cgt_timed_solve
import time
import sys


def test_solve_with_tt(state, player, time_limit, board, solver):
    tt = TranspositionTable()
    isWin, win_move, timeUsed, node_count =  solver(state, tt, time_limit, board)
    
    if(isWin == None):
        isWin = "?"
    elif((player == BLACK and isWin)):
        isWin = "B"
    elif(player == WHITE and not isWin):
        isWin = "B"
        win_move = None
    elif(player == WHITE and isWin):
        isWin = "W"
    elif(player == BLACK and not isWin) :
        isWin = "W"
        win_move = None

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

        state = Clobber_1d(board, BLACK)
        state2 = Clobber_1d(board, BLACK)

        time_allowed = 10

        # Playing the game, main
        isWin, win_move, timeUsed, node_count = test_solve_with_tt(state, BLACK, time_allowed, board, cgt_timed_solve)
        print("[CGT_Black___] : ", isWin, " : ", win_move, " : ", timeUsed, " : ", node_count)

        isWin2, win_move2, timeUsed2, node_count2 = test_solve_with_tt(state2, BLACK, time_allowed, board, martin_timed_solve)
        print("[Martin_Black] : ", isWin2, " : ", win_move2, " : ", timeUsed2, " : ", node_count2)
        print()

        try:
            assert isWin == isWin2
        except AssertionError:
            print("assertion error.")
            print("===============================")
        
        state = Clobber_1d(board, WHITE)
        state2 = Clobber_1d(board, WHITE)

        isWin, win_move, timeUsed, node_count = test_solve_with_tt(state, WHITE, time_allowed, board, cgt_timed_solve)
        print("[CGT_White___] : ", isWin, " : ", win_move, " : ", timeUsed, " : ", node_count)

        isWin2, win_move2, timeUsed2, node_count2 = test_solve_with_tt(state2, WHITE, time_allowed, board, martin_timed_solve)
        print("[Martin_White] : ", isWin2, " : ", win_move2, " : ", timeUsed2, " : ", node_count2)
        print()

        try:
            assert isWin == isWin2
        except AssertionError:
            print("assertion error.")
            print("===============================")

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

        print("board: ", board, " size: ", i)

        state = Clobber_1d(board, BLACK)
        state2 = Clobber_1d(board, BLACK)

        time_to_solve = 10

        # Playing the game, main
        isWin, win_move, timeUsed, node_count = test_solve_with_tt(state, BLACK, time_to_solve, board, cgt_timed_solve)
        print("[CGT_Black___] : ", isWin, " : ", win_move, " : ", timeUsed, " : ", node_count)

        isWin2, win_move2, timeUsed2, node_count2 = test_solve_with_tt(state2, BLACK, time_to_solve, board, martin_timed_solve)
        print("[Martin_Black] : ", isWin2, " : ", win_move2, " : ", timeUsed2, " : ", node_count2)
        print()
        
        if(isWin2 == "W" or isWin2 == "B" or isWin != "W" or isWin != "B"):
            try:
                assert isWin == isWin2 
            except AssertionError:
                print("assertion error.")
                print("===============================")
     
        state = Clobber_1d(board, WHITE)
        state2 = Clobber_1d(board, WHITE)


        isWin, win_move, timeUsed, node_count = test_solve_with_tt(state, WHITE, time_to_solve, board, cgt_timed_solve)
        print("[CGT_White___] : ", isWin, " : ", win_move, " : ", timeUsed, " : ", node_count)

        isWin2, win_move2, timeUsed2, node_count2 = test_solve_with_tt(state2, WHITE, time_to_solve, board, martin_timed_solve)        
        print("[Martin_White] : ", isWin2, " : ", win_move2, " : ", timeUsed2, " : ", node_count2)
        print()


        if(isWin2 == "W" or isWin2 == "B" or isWin != "W" or isWin != "B"):
            try:
                assert isWin == isWin2 
            except AssertionError:
                print("assertion error.")
                print("===============================")


worst_case_testing()
# random_test_suit_testing()