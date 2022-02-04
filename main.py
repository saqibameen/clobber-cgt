# Cmput 655 sample code
# Solve Clobber with Boolean Minimax
# Written by Martin Mueller

from game_basics import BLACK, WHITE, EMPTY, colorAsString
from clobber_1d import Clobber_1d
from boolean_negamax import timed_solve
import sys



def solveAndPrint(state, player, time_limit, solver): 
    print("Solve Board: size", len(state.board))
    state.print()
    print(colorAsString(state.toPlay), "to play")
    isWin, win_move, timeUsed, node_count = solver(state, time_limit)

    if(isWin == None):
        isWin = "?"
    
    elif(player == BLACK and isWin):
        isWin = "B"
    elif(player == BLACK and not isWin):
        isWin = "W"
    elif(player == WHITE and isWin):
        isWin = "W"
    elif(player == WHITE and not isWin):
        isWin = "B"

    print("{} {} {:.64f} {}\n".format(isWin, win_move, timeUsed, node_count))

def testGames(solver):
    for i in range(2,25):
        for player in [WHITE,BLACK]:
            game = Clobber_1d(i, player)
            solveAndPrint(game, solver)

def analyze655Variation(solver):
    game = Clobber_1d("BWBWBWB.WW", WHITE)
    solveAndPrint(game, solver)

def analyze655Game(solver):# Analyze the game we played in class
    game = Clobber_1d(10)
    solveAndPrint(game, solver)
    game.play((1, 2))
    solveAndPrint(game, solver)
    game.play((6, 7))
    solveAndPrint(game, solver)
    game.play((3, 4))
    solveAndPrint(game, solver)
    game.play((8, 9))
    solveAndPrint(game, solver)



def main(board, player, time_limit, timed_solve):
    # testGames(timed_solve)
    #analyze655Game(timed_solve)
    # analyze655Variation(timed_solve)

    game = Clobber_1d(board, player)
    solveAndPrint(game, player, time_limit, timed_solve)


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

        # Playing the game, main 
        main(board, player, time_limit, timed_solve)
    else:
        print(f"Misisng Arguments")

