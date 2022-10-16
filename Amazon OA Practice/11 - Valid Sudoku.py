
def isValidSudoku(board):

    check = {}

    # horizontal
    for row in board:
        for i in row:
            if i != "." and i not in check.keys(): check[i] = ""
            elif i != "." and i in check.keys(): return False
        check = {}
    
    check = {}
    # vertical
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[j][i] != "." and board[j][i] not in check.keys(): check[board[j][i]] = ""
            elif board[j][i] != "." and board[j][i] in check.keys(): return False
        check = {}

    check = {}
    s = board
    # squares
    s1 = s[0][0:3] + s[1][0:3] + s[2][0:3]
    s2 = s[0][3:6] + s[1][3:6] + s[2][3:6]
    s3 = s[0][6:9] + s[1][6:9] + s[2][6:9]
    s4 = s[3][0:3] + s[4][0:3] + s[5][0:3]
    s5 = s[3][3:6] + s[4][3:6] + s[5][3:6]
    s6 = s[3][6:9] + s[4][6:9] + s[5][6:9]
    s7 = s[6][0:3] + s[7][0:3] + s[8][0:3]
    s8 = s[6][3:6] + s[7][3:6] + s[8][3:6]
    s9 = s[6][6:9] + s[7][6:9] + s[8][6:9]
    squares = [s1, s2, s3, s4, s5, s6, s7, s8, s9]

    for square in squares:
        for i in square:
            if i != "." and i not in check.keys(): check[i] = ""
            elif i != "." and i in check.keys(): return False
        check = {}

    return True




s = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(s))