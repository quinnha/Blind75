class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        out = None
        
        while head != None:
            temp = ListNode(head.val, None)
            temp.next = out
            out = temp
            head = head.next
        return out