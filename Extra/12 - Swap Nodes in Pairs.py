# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(None, head)
    prev, cur = dummy, head
    while cur and cur.next:
        prev.next = cur.next
        cur.next = cur.next.next
        prev.next.next = cur
        prev, cur = cur, cur.next
    return dummy.next