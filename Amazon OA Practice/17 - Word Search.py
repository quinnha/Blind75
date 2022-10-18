
def exist(board, word):

    # missing some validatoin/edge cases :( 

    def dfs(board, i, j, k, word):
        if word[k] != board[i][j] or i < 0 or j < 0 or i > len(board) \
            or j > len(board[0]) or k >= len(word):
            return False
        if word[k] == len(word) -1:
            return True

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for x, y in directions:
            tmp = board [i][j]
            board[i][j] = -1

            if dfs(board, i + x, j + y, k + 1, word):
                return True
            
            board[i][j] = tmp

    
    for i in range(len(word)):
        for j in range(len(word[0])):
            if board[i][j] == word[0]: 
                if dfs(board, i, j, 0, word): return True
    return False
    
