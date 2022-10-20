# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    node = head
    
    while node != None:
        
        while node.next!= None and node.val == node.next.val:
            node.next = node.next.next

        node = node.next
    
    return head