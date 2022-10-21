from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# bfs
def maxLevelSum(root) -> int:
    
    sum, l, ans = float('-inf') , 1, 0
    q = []
    q.append(root)
    
    while(len(q)):
        n, s = len(q), 0

        for _ in range(n):
            temp = q.pop(0)
            s += temp.val
            if temp.left: q.append(temp.left)
            if temp.right: q.append(temp.right)
        if s > sum:
            sum = s
            ans = l
        l += 1
    
    return ans

# recursion
def maxLevelSum(root):
    levels = defaultdict(int)
    def sum_vals(root, depth):
        if root:
            levels[depth] += root.val
            sum_vals(root.left,  depth+1)
            sum_vals(root.right, depth+1)
        
    sum_vals(root, 1)
    return max(levels, key=levels.get)