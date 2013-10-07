
import pdb 

def print_board(board):
    print (str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]))
    print ('-----------')
    print (str(board[3]) + ' | ' + str(board[4]) + ' | ' + str(board[5]))
    print ('-----------')
    print (str(board[6]) + ' | ' + str(board[7]) + ' | ' + str(board[8]))


def check4win(board):
    """
    x = 1 o = -1 blank = 0 
    board[i] ----> 1, -1, 0, None
    """
    #check rows
    if abs(board[0] + board[1] + board[2]) == 3: 
        return board[0]
    elif abs(board[3] + board[4] + board[5]) == 3:
        return board[3]
    elif abs(board[6] + board[7] + board[8]) == 3: 
        return board[6]
 
    #check columns
    elif abs(board[0] + board[3] + board[6]) == 3:
        return board[0]
    elif abs(board[1] + board[4] + board[7]) == 3:
        return board[1]
    elif abs(board[2] + board[5] + board[8]) == 3:
        return board[2]
    
    #check diagonals
    elif abs(board[0] + board[4] + board[8]) == 3:
        return board[0]
    elif abs(board[2] + board[4] + board[6]) == 3:
        return board[2]
    #check tie    
    elif len([x for x in board if x != 0]) == 9:
        return 0

def movesAvailable(board):
    moves = [ ]
    for x in range(9):
        if (board[x] == 0):
            moves.append(x)
    return moves

def score(board, player):
    #pdb.set_trace()
    if check4win(board) == player:
        return 1
    elif check4win(board) == -player:
        return -1
    elif check4win(board) == 0:
        return 0
    else: 
        values = [ ]
        for m in (movesAvailable(board)): 
            board[m] = player
            values.append((-score(board, -player)))
            board[m] = 0
        return max(values)


#tests

def testBlank():
    board = [ 0, 0, 0,
              0, 0, 0,
              0, 0, 0 ]
    assert check4win(board) == None
    assert movesAvailable(board) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print_board(board)
def testRow():
    board = [ 1, 1, 1,
              0, 0, 0,
              0, 0, 0 ]
    assert check4win(board) == 1

    board = [ 0, 0, 0,
              1, 1, 1,
              0, 0, 0 ]
    assert check4win(board) == 1

    board = [ 0, 0, 0,
              0, 0, 0,
              1, 1, 1 ]
    assert check4win(board) == 1

def testCol():
    board = [ 1, 0, 0,
              1, 0, 0,
              1, 0, 0]
    assert check4win(board) ==1

    board = [ 0, 1, 0,
              0, 1, 0,
              0, 1, 0 ]
    assert check4win(board) == 1

    board = [0, 0, 1,
             0, 0, 1,
             0, 0, 1]
    assert check4win(board) == 1

def testDiag(): 
    board = [1, 0, 0,
             0, 1, 0,
             0, 0, 1]
    assert check4win(board) == 1 

    board = [0, 0, 1,
             0, 1, 0,
             1, 0, 0]
    assert check4win(board) == 1

def testFull():
    board = [1, -1, -1,
             -1, 1, 1,
             1, 1, -1 ] 
    assert check4win(board) == 0

def all_board_tests():
    testRow()
    testCol()
    testDiag()
    testFull()
    testBlank()


all_board_tests()

def testOneMove():
    board = [1, -1, -1,
             0, 1, 1,
             -1, 1, -1]
    assert score(board, 1) == 1


def testTwoMoves():
    board = [1, -1, -1,
             0, 1, 1,
             0, 1, -1]
    assert score(board, 1) == 1
    assert score(board, -1)== 0

def testThreeMoves():
    board = [1, -1, -1,
             0, 1, 0,
             0, 1, -1]
    assert score(board, 1) == 0

def testMoves():
    testOneMove()
    testTwoMoves()
    testThreeMoves()

testMoves()

