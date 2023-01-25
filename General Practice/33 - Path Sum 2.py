class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(root, targetSum):
        out = []
        def traverse(node, currSum, curr_path):
            if not node: return False
            if not node.left and not node.right and currSum + node.val == targetSum: out.append(curr_path + [node.val])
            return traverse(node.left, currSum + node.val, curr_path + [node.val]) or traverse(node.right, currSum + node.val, curr_path + [node.val])

        traverse(root, 0, [])
        return out