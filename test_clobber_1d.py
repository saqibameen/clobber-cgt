from game_basics import EMPTY, BLACK, WHITE, isEmptyBlackWhite, opponent
from clobber_1d import Clobber_1d

def test_board_init():
    game = Clobber_1d(1)
    assert game.board == [BLACK]
    game = Clobber_1d(2)
    assert game.board == [BLACK, WHITE]
    game = Clobber_1d(3)
    assert game.board == [BLACK, WHITE, BLACK]
    game = Clobber_1d(10)
    assert game.board == [BLACK, WHITE, BLACK, WHITE, BLACK, WHITE, BLACK, WHITE, BLACK, WHITE]
    game = Clobber_1d("BWWEWWWWBW")
    assert game.board == [BLACK, WHITE, WHITE, EMPTY, WHITE, WHITE, WHITE, WHITE, BLACK, WHITE]

def test_legal_moves():
    game = Clobber_1d(2)
    moves = game.legalMoves()
    assert len(moves) == 1
    assert moves[0][0] == 1 # src
    assert moves[0][1] == 0 # to
    
def test_play():
    game = Clobber_1d(2)
    game.play((1,0))
    assert game.board == [WHITE, EMPTY]

def test_undo():
    game = Clobber_1d(2)
    game.play((1,0))
    game.undoMove()
    assert game.board == [BLACK, WHITE]
    
test_board_init()
test_legal_moves()
test_play()
test_undo()