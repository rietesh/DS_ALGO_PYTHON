def initializeBorad(n, board):
    board['queen'] = [-1]*n
    board['row'] = [0]*n
    board['col'] = [0]*n
    board['top_bottom'] = [0]*(2*n-1)
    board['bottom_top'] = [0]*(2*n-1)
    return board

def updateBoard(n, i,j,board):
    board['queen'][i] = j
    board['row'][i] = 1
    board['col'][j] = 1
    board['top_bottom'][(j-i) + n-1] = 1
    board['bottom_top'][j+i] = 1
    return board

def undoBoard(n, i,j, board):
    board['queen'][i] = -1
    board['row'][i] = 0
    board['col'][j] = 0
    board['top_bottom'][(j-i) + n-1] = 0
    board['bottom_top'][j+i] = 0
    return board

def isFree(n, i,j,board):
    if (board['queen'][i] == -1 and board['row'][i] == 0 and board['col'][j] == 0
        and board['top_bottom'][(j-i) + n-1] == 0 and board['bottom_top'][j+i] == 0):
        return True
    else:
        return False

def queens(i, board):
    n = len(board['queen'])
    for c in range(n):
        if isFree(n, i, c, board):
            board = updateBoard(n, i, c, board)
            if i == n-1:
                return True
            else:
                extend = queens(i+1, board)
            if extend:
                return True
            else:
                board = undoBoard(n, i, c, board)
    else: 
        return False

board = {}
n = int(input('Enter Number of Queens: '))
board = initializeBorad(n, board)
print_board = [[' ']*n for i in range(n)]
if queens(0, board):
    print('Placed Queens at: ', end='\n')
    for i,j in enumerate(board['queen']):
        print_board[i][j] = 'Q'
        print(i,j)

print('Final Board')
for i in range(n):
    print(print_board[i], end='\n')