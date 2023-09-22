class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# reverse linked list
def reverseList(head):
    ret = None

    while head:
        node = ListNode(head.val)
        node.next = ret
        ret = node

        head = head.next

    return ret
