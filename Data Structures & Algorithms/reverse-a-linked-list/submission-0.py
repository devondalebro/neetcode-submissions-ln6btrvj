# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        p, c, n = None, head, head.next
        while c is not None:
            c.next = p
            p = c
            c = n
            if c is None:
                break
            n = c.next
        
        return p