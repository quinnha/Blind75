import heapq


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


# lowest common ancestor
def lowestCommonAncestor(root, p, q):
    # keep doing down if they are in the same subtree -> the moment that they arent in the subtree, thats the LCA -> ordered btree bruh

    while (root.val - p.val) * (root.val - q.val) > 0:
        root = root.left if p.val < root.val else root.right
    return root


# level order traversal
def levelOrder(root):
    if not root:
        return []
    queue = [root]
    ret = [[root.val]]

    while queue:
        ans = []
        for i in range(len(queue)):
            node = queue.pop(0)
            if not node:
                continue
            if node.left:
                ans.append(node.left.val)
            if node.right:
                ans.append(node.right.val)
            queue.append(node.left)
            queue.append(node.right)

        if ans:
            ret.append(ans)

    return ret


# kth smallest
def kthSmallest(root, k):
    heap = []

    def traverse(node):
        if not node:
            return
        heap.append(node.val)
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    heapq.heapify(heap)
    for i in range(k - 1):
        heapq.heappop(heap)

    return heapq.heappop(heap)


# kth smallest (indended version)
def kthSmallest(root, k):
    # basically go all the way left until you cant, then go right once,
    # then go all the way left, decreasing your k until its 0,
    # then its the value you want (cool algo)

    number = 0
    count = 0

    def helper(node):
        if not node.left:
            helper(node.left)
        count -= 1
        if count == 0:
            number = node.val
            return
        if not node.right:
            helper(node.right)

    count = k
    helper(root)
    return number


# is valid bst
def isValidBST(root):
    # inorder traversal will be in numerical order
    out = []

    def inOrder(root, out):
        if not root:
            return

        inOrder(root.left, out)
        out.append(root.val)
        inOrder(root.right, out)

    inOrder(root, out)

    for i in range(1, len(out)):
        if out[i - 1] >= out[i]:
            return False

    return True
