from clobber_1d import Clobber_1d
from game_basics import BLACK, WHITE, colorAsString
from transposition_table_simple import TranspositionTable
from cgt import timed_solve as cgt_timed_solve
import time
import sys

mode = "test" # run or test

def test_solve_with_cgt(state, player, time_limit, board):
    tt = TranspositionTable()
    isWin, win_move, timeUsed, node_count =  cgt_timed_solve(state, tt, time_limit, board)

    # change win_move to from-to
    if win_move is not None:
        src, to = str(win_move).split(', ')
        src = src.replace('(', '')
        to = to.replace(')', '')
        win_move = "{}-{}".format(src, to)
        
    if(isWin == None):
        isWin = "?"
    elif((player == BLACK and isWin) or (player == WHITE and not isWin)):
        isWin = "B"
    elif((player == BLACK and not isWin) or (player == WHITE and isWin)):
        isWin = "W"

    if mode == "run":
        print("{} {} {:.4f} {}\n".format(isWin, win_move, timeUsed, node_count))

    result = "{} {}".format(isWin, win_move)
    return result, timeUsed

def run_sanity_checks():
    test_cases = open("testcases.txt", "r").readlines()
    test_cases = [x.strip() for x in test_cases]
    time_limit = 10 # base time limit, in seconds
    for test_no, test_case in enumerate(test_cases):
        board, player_char = test_case.split()

        if(player_char == "B"):
            player = BLACK
        else:
            player = WHITE

        state = Clobber_1d(board, player)
        result, timeUsed = test_solve_with_cgt(state, player, time_limit, board)
        print(f"Result {result} | Time Used {timeUsed}")

if __name__ == "__main__":
    if mode == "run":
        if(len(sys.argv) == 4):
            board = str(sys.argv[1]).upper()
            player = str(sys.argv[2]).upper()
            time_limit = float(sys.argv[3])
            assert player == "B" or player == "W"

            if(player == "B"):
                player = BLACK
            else:
                player = WHITE

            state = Clobber_1d(board, player)
            # Playing the game, main
            test_solve_with_cgt(state, player, time_limit, board)
            # test_solve_with_tt(state, player, time_limit, board)
        else:
            print(f"Misisng Arguments")

    else: run_sanity_checks() # do the sanity check