from game_basics import BLACK, WHITE, colorAsString
from clobber_1d import Clobber_1d
from game_basics import BLACK, WHITE, colorAsString
from transposition_table_simple import TranspositionTable
from negamax_no_hash import timed_solve as timed_solve_no_hash
from cgt import timed_solve as cgt_timed_solve
import time
import sys

mode = "test" # run or test

def solve_with_given_solver(state, player, time_limit, board):
    tt = TranspositionTable()
    isWin, win_move, timeUsed, node_count =  cgt_timed_solve(state, tt, float(time_limit), board)

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

    return isWin, win_move, timeUsed, node_count


def test_cases_run():
    test_cases = open("tests_small.txt", "r").readlines()

    for test_case in test_cases:
        board, player_char, time_limit = test_case.split()

        if(player_char == "B"):
            player = BLACK
        else:
            player = WHITE

        state = Clobber_1d(board, player)
        isWin, win_move, timeUsed, node_count = solve_with_given_solver(state, player, time_limit, board)
        tt = open("results_small.txt", "a")
        tt.write(test_case)
        tt.write("{} {} {:.4f} {}\n".format(isWin, win_move, timeUsed, node_count))
        tt.close()

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
            solve_with_given_solver(state, player, time_limit, board)
        else:
            print(f"Misisng Arguments")

    else: test_cases_run() # do the sanity check