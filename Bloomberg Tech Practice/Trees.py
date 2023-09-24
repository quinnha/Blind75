class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# invert binary tree
def invertTree(root):
    def reverse(node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        reverse(node.left)
        reverse(node.right)

    reverse(root)
    return root


# max depth
def maxDepth(root):
    def traverse(node, depth):
        if not node:
            return depth
        return max(traverse(node.left, depth + 1), traverse(node.right, depth + 1))

    return traverse(root, 0)


# same tree
def isSameTree(p, q):
    def traverse(p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val:
            return traverse(p.left, q.left) and traverse(p.right, q.right)

    return traverse(p, q)


# is subtree
def isSubtree(a, b):
    if not b:
        return True

    def checkTree(root1, root2):
        if not root1 and not root2:
            return True
        elif root1 and not root2 or root2 and not root1:
            return False

        if root1.val != root2.val:
            return False

        return checkTree(root1.left, root2.left) and checkTree(root1.right, root2.right)

    def dfs(s, t):
        if not s:
            return False

        if s.val == t.val and checkTree(s, t):
            return True

        return dfs(s.left, t) or dfs(s.right, t)

    return dfs(a, b)
