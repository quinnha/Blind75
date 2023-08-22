class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    head = ListNode()
    ret = head

    while list1 or list2:
        if list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
        else:
            if list1:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next

        head = head.next

    return ret.next
