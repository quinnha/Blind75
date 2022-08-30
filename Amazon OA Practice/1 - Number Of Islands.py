# just dfs on the boxes around you
def numIslands(grid):

    if not grid: return 0

    count = 0
    visited = []

    columns = len(grid[0])
    rows = len(grid)

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == "1":
                dfs(grid, i,j)
                count +=1

    return count

def dfs(grid, i, j):
    if i < 0 or j < 0 or i >=len(grid) or j >= len(grid[0]) or grid[i][j] != "1": return 

    # mark it (visited)
    grid[i][j] = '#'

    # basically check the square aroudn it

    # check the up down
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)

    # check the left right
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(grid))

