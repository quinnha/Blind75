# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    
    l3 = ListNode(-1)
    l3head = l3
    carry = 0 
    
    while l1 != None and l2 != None:
        
        total = l1.val + l2.val + carry
        
        carry, rem = divmod(total, 10)
        
        l3.next = ListNode(rem)
        l3 = l3.next
        l1 = l1.next
        l2 = l2.next

    if l1 == None:
        while l2 != None:
            total = l2.val + carry
            
            carry, rem = divmod(total, 10)
            
            l3.next = ListNode(rem)
            l3 = l3.next
            l2 = l2.next
            
    elif l2 == None:
        while l1 != None:
            total = l1.val + carry

            carry, rem = divmod(total, 10)

            l3.next = ListNode(rem)
            l3 = l3.next
            l1 = l1.next
    
    if carry > 0: l3.next = ListNode(carry)
    
    return l3head.next