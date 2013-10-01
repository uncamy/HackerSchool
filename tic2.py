
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
    if board[1] == board[2] == board[3] and board[1]!= ' ':
        return board[1]
    elif board[4] == board[5] == board[6] and board[4]!= ' ':
        return board[4]
    elif board[7] == board[8] == board[9] and board[7] != ' ':
        return board[7]
    #check columns
    elif board[1] == board[3] == board[5] and board[1]!= ' ':
        return board[1]
    elif board[2] == board[5] == board[6] and board[2] != ' ':
        return board[2]
    elif board[3] == board[6] == board[9] and board[3] != ' ':
        return board[3]
    #check diagonals
    elif board[1] == board[5] == board[9] and board[1] != ' ':
        return board[1]
    elif board[7] == board[5] == board[3] and board[3] != ' ':
        return board[3]
    else:
        return ' ' 

#main 
def playerMove():
    while True:
   #get the user's move
        move = raw_input("Make a move! Enter a number 1-9: ")
        try: 
           digit= int(move)
           if 1 <= digit <= 9:
               return digit
           else: 
               print "Must be a number between 1-9"
        except ValueError:
            print "Invalid input"

board= [' ']*10
print_board(board)
#Handle user move
movecounter = 0

while True:
    digit = playerMove()
    movecounter+=1
    board[digit] = "X"
    
    print_board(board)
    
    done = check4win(board)
    
    if (done != ' ' or movecounter == 9):
        break

if (done != ' '):
    print "yay!" + done + " won!"
else:
    print "we have a tie"


