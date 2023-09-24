# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# num of islands
def numIslands(grid):
    def dfs(grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "0"
        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i, j - 1)

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                dfs(grid, i, j)
                count += 1
    return count


# clone graph
def cloneGraph(node):
    if not node:
        return node
    q = [node]
    clones = {node.val: Node(node.val, [])}

    while q:
        curr = q.pop(0)
        print(curr.val)
        curr_clone = clones[curr.val]

        for neighbor in curr.neighbors:
            if neighbor.val not in clones:
                q.append(neighbor)
                clones[neighbor.val] = Node(neighbor.val, [])

            curr_clone.neighbors.append(clones[neighbor.val])
    return clones[node.val]
