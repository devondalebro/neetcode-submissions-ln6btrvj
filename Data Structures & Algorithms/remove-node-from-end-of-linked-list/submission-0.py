# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listLen = 0
        temp = head
        while temp is not None:
            temp = temp.next 
            listLen += 1
        
        pre, cur, nex = None, head, head.next
        i = 0


        while i != listLen - n:
            pre = cur
            cur = nex
            nex = cur.next
            i += 1
        
        if pre is None:
            return nex
        
        pre.next = nex
        return head
