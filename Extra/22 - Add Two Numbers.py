# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    l = ListNode()
    head = l

    carry = False
    while l1 and l2:
        val = l1.val + l2.val
        if carry:
            val += 1
        if val >= 10:
            val %= 10
            carry = True
        else:
            carry = False
        l.next = ListNode(val)

        l = l.next
        l1 = l1.next
        l2 = l2.next

    while l1:
        val = l1.val
        if carry:
            val += 1
        if val >= 10:
            val %= 10
            carry = True
        else:
            carry = False
        l.next = ListNode(val)

        l = l.next
        l1 = l1.next

    while l2:
        val = l2.val
        if carry:
            val += 1
        if val >= 10:
            val %= 10
            carry = True
        else:
            carry = False
        l.next = ListNode(val)

        l = l.next
        l2 = l2.next
    if carry:
        l.next = ListNode(1)
    return head.next
