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


# merge sorted lists
def mergeTwoLists(list1, list2):
    ret = ListNode()
    ret1 = ret

    while list1 or list2:
        if not list1:
            ret.next = list2
            list2 = list2.next
        elif not list2:
            ret.next = list1
            list1 = list1.next
        elif list1.val >= list2.val:
            ret.next = list2
            list2 = list2.next
        elif list2.val > list1.val:
            ret.next = list1
            list1 = list1.next

        ret = ret.next

    return ret1.next


# reorder list
def reorderList(head):
    """
    Do not return anything, modify head in-place instead.
    """
    if not head.next:
        return head

    forwards = head
    backwards = None

    helper = head

    n = 0

    while helper:
        node = ListNode(helper.val)
        node.next = backwards
        backwards = node
        helper = helper.next
        n += 1

    for i in range(n // 2 - 1):
        temp = forwards.next
        forwards.next = backwards
        backwards = backwards.next
        forwards = forwards.next
        forwards.next = temp
        forwards = forwards.next
    if n % 2 != 0:
        temp = forwards.next
        forwards.next = backwards
        backwards = backwards.next
        forwards = forwards.next
        forwards.next = temp
        forwards = forwards.next
    else:
        forwards = forwards.next

    if forwards:
        forwards.next = None

    return head


# reorder list 2 -> find middle, reverse middle, merge lists together
def reorderList(head):
    """
    Do not return anything, modify head in-place instead.
    """

    if not head:
        return []

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    reverse = None

    prev, curr = None, slow.next
    while curr:
        nextt = curr.next
        curr.next = prev
        prev = curr
        curr = nextt
    slow.next = None

    head1, head2 = head, prev
    while head2:
        nextt = head1.next
        head1.next = head2
        head1 = head2
        head2 = nextt
    return head
