class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    return check(root)
    
def check( head):
    if head.left == None and head.right == None:
        return True
    elif head.left == None and head.right.val > head.val:
        return check(head.right)
    elif head.right == None and head.left.val < head.val:
        return check(head.left)
    elif head.left.val < head.val and head.right.val > head.val:
        return check(head.left) and check(head.right)
    else:
        return False

x = TreeNode(1, None, TreeNode(1, None, None))

print(isValidBST(x))