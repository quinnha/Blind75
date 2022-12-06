# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """

    fast, slow = head, head
    for _ in range(n): fast = fast.next
    if not fast: return head.next
    while fast.next: fast, slow = fast.next, slow.next
    slow.next = slow.next.next
    return head

# Perfect Explanation of fast/slow here: https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/1164542/js-python-java-c-easy-two-pointer-solution-w-explanation/