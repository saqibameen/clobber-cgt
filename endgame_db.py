from itertools import product
from clobber_1d import Clobber_1d
from game_basics import EMPTY, BLACK, WHITE
from transposition_table_simple import TranspositionTable
# from cgt import timed_solve as cgt_timed_solve
from negamax_tt_martin import timed_solve as negamax_tt_timed_solve
import json



def solve_with_given_solver(state, player, time_limit, board):
    tt = TranspositionTable()
    isWin, win_move, timeUsed, node_count =  negamax_tt_timed_solve(state, tt, float(time_limit), board)

    # change win_move to from-to
    if win_move is not None:
        src, to = str(win_move).split(', ')
        src = src.replace('(', '')
        to = to.replace(')', '')
        win_move = "{}-{}".format(src, to)

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

    # if mode == "run":
    print("{} {} {:.4f} {}\n".format(isWin, win_move, timeUsed, node_count))

    return isWin, win_move, timeUsed, node_count


positions = ["B", "W", "."]
players = ["B", "W"]
# board_list = list(product(positions, repeat=6)) + list(product(positions, repeat=5)) + (list(product(positions, repeat=4))) + list(product(positions, repeat=3)) + list(product(positions, repeat=2)) + list(product(positions, repeat=1))

board_length = 10
board_lengths = range(board_length, 0, -1)

board_list = []
for i in board_lengths:
    board_list += (product(positions, repeat=i))

counter = 0
board_dict = {}
for board in board_list:

    board = "".join(board)
    board_dict[board] = list()

    for player in players:
        counter += 1
        print(f"Board: {board} Player: {player}")

        time_limit = float(10)
        assert player == "B" or player == "W"
        if(player == "B"):
            player = BLACK
        else:
            player = WHITE

        state = Clobber_1d(board, player)
        isWin, _, _, _ = solve_with_given_solver(state, player, time_limit, board)
        board_dict[board].append(isWin)

    B_result, W_result = board_dict[board]
    if(B_result == "B" and W_result == "W"):
        print(f"Game Value: N (first player win)")
        board_dict[board].append("N")
    elif(B_result == "W" and W_result == "B"):
        print(f"Game Value: P (second player win)")
        board_dict[board].append("P")
    elif(B_result == "B" and W_result == "B"):
        print(f"Game Value: L (Balck always win)")
        board_dict[board].append("L")  #L means B wins in any case
    elif(B_result == "W" and W_result == "W"):
        print(f"Game Value: R (White always win)")
        board_dict[board].append("R")  #R means W wins in any case

    print()
    print()
        

print(f"Total games: {counter}")

# Saving endgame databases
with open('endgamedb.json', 'w') as fp:
    json.dump(board_dict, fp,  indent=4)

# print(board_dict)