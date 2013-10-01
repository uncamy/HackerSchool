
def print_board(board):
    #board is a list of 10 strings ignoring index 0
    print (' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print ('-----------')
    print (' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print ('-----------')
    print (' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


#todo: handle moves by user and computer


#checks rows, columns and diagonals
def check4win(board):
    #check rows
    if board[1] == board[2] == board[3]:
        return board[1]
    elif board[4] == board[5] == board[6]:
        return board[4]
    elif board[7] == board[8] == board[9]:
        return board[7]
    #check columns
    elif board[1] == board[3] == board[5]:
        return board[1]
    elif board[2] == board[5] == board[6]:
        return board[2]
    elif board[3] == board[6] == board[9]:
        return board[3]
    #check diagonals
    elif board[1] == board[5] == board[9]:
        return board[1]
    elif board[7] == board[5] == board[3]:
        return board[3]
    else:
        return False

#main 
def playerMove():
    while True:
   #get the user's move
    move = raw_input("Make a move! Enter a number 1-9")
    #validate input
    try: 
        int(move)
    except:
        print "Invalid input"
    #return cell
    return move


board = [' ']* 10
board[1]= 'o'
board[5]= 'o'
board[9]= 'o'

print_board(board)

playerMove()

check4win(board)


done = check4win(board)
if done == False:
    print "keep playing!"
else: 
    print "We have a winner!"

