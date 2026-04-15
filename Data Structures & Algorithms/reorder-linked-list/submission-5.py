# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        listLen = 0
        c = head
        while c is not None:
            listLen += 1
            c = c.next
        
        print(listLen)
        
        if listLen <= 2:
            return 

        i, j = 0, 0
        cI, cJ = head, head

        # go until j = n - (n - 1) // 2
        cJprev, cJnext = None, None
        while j < (listLen + 1) // 2:
            cJprev = cJ
            cJ = cJ.next
            j += 1
        
        if cJprev is not None:
            cJprev.next = None

        cJprev = None
        if cJ is not None:
            cJnext = cJ.next
        while cJ is not None:
            cJ.next = cJprev
            cJprev = cJ
            cJ = cJnext
            if cJ is not None:
                cJnext = cJ.next
        
        cJ = cJprev
        cJnext = cJ.next
        while cJ is not None:
            cJ.next = cI.next
            cI.next = cJ
            cJ = cJnext
            if cJ is not None:
                cJnext = cJ.next
            cI = cI.next.next
