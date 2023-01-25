class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum) -> bool:

    def traverse(node, currSum):
        if not node: return False
        if not node.left and not node.right and currSum + node.val == targetSum: return True
        return traverse(node.left, currSum + node.val) or traverse(node.right, currSum + node.val)

    return traverse(root, 0)
