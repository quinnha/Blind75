matrix = [[]] # m x n matrix

#bfs starting at i, j, only going up down left right
def bfs(i,j):

    if not matrix: return
    
    q = []
    q.append([i,j])

    while q:
        val = q.pop(0)
        x = val[0]
        y = val[1]

        if matrix[x][y] != '#': 
            matrix[x][y] = "#"
            q.append[x + 1][y]
            q.append[x - 1][y]
            q.append[x][y + 1]
            q.append[x ][y - 1]

# bfs for adjacency matrix
def bfs(node):

    if not matrix: return

    q = []
    q.append(node)
    visited = {}
    while q:
        val = q.pop(0)
        if val not in visited: 
            visited[node] = ""
            for neighbour in val:
                q.append(neighbour)

