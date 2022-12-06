class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(self, head):
    oddHead = ListNode(None)
    evenHead = ListNode(None)
    oddNode = oddHead
    evenNode = evenHead
    isEven = True
    while head != None:
        if isEven:  # even case
            isEven = False
            oddNode.next = head
            oddNode = oddNode.next
        else:  # odd case
            isEven = True
            evenNode.next = head
            evenNode = evenNode.next
        head = head.next

    oddNode.next = evenHead.next
    evenNode.next = None
    return oddHead.next