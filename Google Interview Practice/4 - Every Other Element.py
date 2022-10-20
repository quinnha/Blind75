
from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def EveryKElements(head, k):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    node = head
    counter = 1

    out = ListNode(head.val)
    outhead = out

    while node is not None:
        if counter % k == 0:
            out.next = ListNode(node.val)
            out = out.next

        node = node.next
        counter += 1
    
    return outhead


n = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))

o = EveryKElements(n, 2)

while o is not None:
    print(o.val)
    o = o.next
    