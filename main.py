# Cmput 655 sample code
# Solve Clobber with Boolean Minimax
# Written by Martin Mueller

from game_basics import BLACK, WHITE, EMPTY, colorAsString
from clobber_1d import Clobber_1d
from boolean_negamax import timed_solve

def solveAndPrint(state, solver): 
    print("Solve Board: size", len(state.board))
    state.print()
    print(colorAsString(state.toPlay), "to play")
    isWin, timeUsed = solver(state)
    print("Win: {}\nTime used: {:.4f}\n".format(
        isWin, timeUsed))

def testGames(solver):
    for i in range(2,25):
        for player in [WHITE,BLACK]:
            game = Clobber_1d(i, player)
            solveAndPrint(game, solver)

def analyze655Variation(solver):
    game = Clobber_1d("BWBWBWB.WW", BLACK)
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

testGames(timed_solve)

#analyze655Game(timed_solve)
#analyze655Variation(timed_solve)