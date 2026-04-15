# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = list1, list2

        ret = None
        head = None
        while c1 is not None and c2 is not None:
            print(1)
            if c1.val < c2.val:
                if ret is None:
                    ret = ListNode(c1.val)
                    head = ret
                else:
                    ret.next = ListNode(c1.val)
                    ret = ret.next
                c1 = c1.next
            else:
                if ret is None:
                    ret = ListNode(c2.val)
                    head = ret
                else:
                    ret.next = ListNode(c2.val)
                    ret = ret.next
                c2 = c2.next
        
        remaining = c1 if c1 is not None else c2

        while remaining is not None:
            if ret is None:
                ret = ListNode(remaining.val)
                head = ret
            else:
                ret.next = ListNode(remaining.val)
                ret = ret.next
            remaining = remaining.next

        return head
