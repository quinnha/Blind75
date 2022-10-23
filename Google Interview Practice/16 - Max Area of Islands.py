def maxAreaOfIsland(grid):
        
        if not grid: return 0
        
        q = []
        
        out = 0
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append([i,j])
                    
                    while q:
                        val = q.pop(0)
                        a = val[0]
                        b = val[1]

                        if grid[a][b] == 1:
                            grid[a][b] = 2
                            count += 1
                            if a + 1 < len(grid): q.append([a + 1, b])
                            if a - 1 >= 0: q.append([a - 1, b])
                            if b + 1 < len(grid[0]): q.append([a, b + 1])
                            if b - 1 >= 0: q.append([a, b - 1])              
                            
                out = max(out, count)
                count = 0
                q = []
                          
        return out