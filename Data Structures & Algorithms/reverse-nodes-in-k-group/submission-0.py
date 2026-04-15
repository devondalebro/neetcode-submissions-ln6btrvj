# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        ret = None
        
        nextGroup = head
        currGroup = head
        prevGroup = None

        while True:

            i = 0
            beforeNextGroup = None
            while nextGroup is not None and i < k:
                beforeNextGroup = nextGroup
                nextGroup = nextGroup.next
                i += 1
            
            if nextGroup:
                print(f'nextGroup {nextGroup.val}')
            else:
                print(f'nextGroup None')
            
            print(f'value of i is {i}')

            if i < k:
                print("do not reverse")
                prevGroup.next = currGroup
                break

            if prevGroup is not None:
                prevGroup.next = beforeNextGroup
            
            pre, cur, nex = None, currGroup, currGroup.next

            print("About to reverse")
            while nex is not nextGroup:
                cur.next = pre
                pre = cur
                cur = nex
                nex = cur.next
            
            cur.next = pre

            if ret is None:
                ret = cur

            temp = cur
            while temp.next is not None:
                temp = temp.next

            prevGroup = temp
            currGroup = nextGroup
            if prevGroup:
                print(f'prevGroup {prevGroup.val}')
            else:
                print(f'prevGroup NONE')

            if currGroup:
                print(f'currGroup {currGroup.val}')
            else:
                print(f'currGroup NONE')
            
        return ret
