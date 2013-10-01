#HackerSchool Project 1- Tic Tac Toe with Smita

board = []

#create board
for x in range(0,3):
    board.append(["*"] *3)

#print the board
def print_board(board):
    row_num = ["1","2","3"]
    print "  A B C "
    print "-------"
    for i, row in zip(row_num, board):
        print (i + "|" + " ".join(row))

print_board(board)
