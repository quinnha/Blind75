matrix = [[]]

def dfs(i,j):

    if matrix[i][j] == "#" or i < 0 or j < 0 or i > len(matrix) or j > len(matrix[0]): return

    if matrix[i][j] == "1": 
        matrix[i][j] = "#"
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

