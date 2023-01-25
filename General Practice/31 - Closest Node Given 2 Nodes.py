
def closestMeetingNode(edges, node1: int, node2: int) -> int:
    
    table = {}
    for idx, val in enumerate(edges):
        table[idx] = val
    print(table)

    from_n1 = set()
    from_n2 = set()
    stack = [node1]
    max_ = float('inf')
    

    while stack:
        val = stack.pop()
        p2 = table[val]
        print(val, p2)
        
        if p2 != -1 and val not in from_n1: 
            stack.append(p2)
        from_n1.add(val)
    
    stack = [node2]
    print(from_n1)
    while stack:
        val = stack.pop()
        p2 = table[val]
        print(val, p2)
        if val in from_n1: 
            max_ = max(max_, val)
        if p2 != -1 and  val not in from_n2:
            stack.append(p2)
        from_n2.add(val)

    
    return -1
    

# Better Answer

def closestMeetingNode(edges, n1: int, n2: int) -> int:

    def dfs(node):
    
        dist, res = 0, [-1]*len(edges)
        
        while node != -1 and res[node] == -1:
            res[node], node = dist, edges[node]
            dist += 1
            
        return res

    ans = (inf,-1)
    
    for i, (d1,d2) in enumerate(zip(dfs(n1),dfs(n2))):
    
        if d1 == -1 or d2 == -1: continue
        ans = min(ans,(max(d1, d2),i))
            
    return ans[1]