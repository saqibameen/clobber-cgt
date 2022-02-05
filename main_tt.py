from clobber_1d import Clobber_1d
from game_basics import BLACK, WHITE, colorAsString
from transposition_table_simple import TranspositionTable
from boolean_negamax_tt import timed_solve
import time
import sys

def test_solve_with_tt(state, player, time_limit, board):
    tt = TranspositionTable()
    isWin, win_move, timeUsed, node_count =  timed_solve(state, tt, time_limit, board)

    if(isWin == None):
        isWin = "?"
    elif((player == BLACK and isWin) or (player == WHITE and not isWin)):
        isWin = "B"
    elif((player == BLACK and not isWin) or (player == WHITE and isWin)):
        isWin = "W"

    print("{} {} {:.64f} {}\n".format(isWin, win_move, timeUsed, node_count))

if __name__ == "__main__":

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
        test_solve_with_tt(state, player, time_limit, board)
    else:
        print(f"Misisng Arguments")
