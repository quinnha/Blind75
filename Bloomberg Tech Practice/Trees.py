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
