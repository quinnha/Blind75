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
