class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        if head.next is None: return None
        
        node = head

        while node.next is not None:
            if node.next.val == val: 
                node.next = node.next.next
            else: node = node.next


        