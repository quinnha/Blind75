
def minPathSum(grid):

    m = len(grid)
    n = len(grid[0])
    dp = [[] * n for i in range(m)]

    # initialize the first row of dp
    counter = 0
    for val in grid[0]:
        counter += val
        dp[0].append(counter)
    
    # initialize the first col of dp
    counter = grid[0][0]
    for i in range(1, len(grid)):
        counter += grid[i][0]
        dp[i].append(counter)

    # take the minimum of the top element and the left element 

    # rows
    for i in range(1, len(grid)):
        #cols
        for j in range(1, len(grid[0])):
            dp[i].append(min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j]))
    
    return(dp[m-1][n-1])


print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(minPathSum([[1,2,3],[4,5,6]]))
print(minPathSum([[1,2],[5,6],[1,1]]))