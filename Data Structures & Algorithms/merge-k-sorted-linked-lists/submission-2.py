# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ret = None
        head = None
        nums = [10000] * len(lists)

        minN, minI = 10000, -1
        while True:
            if ret is None:
                for i in range(len(lists)):
                    nums[i] = lists[i].val
            elif minI != -1:
                minList = lists[minI]
                lists[minI] = lists[minI].next
                if lists[minI] is None:
                    nums[minI] = 10000
                else:
                    nums[minI] = lists[minI].val
            else:
                print("bru")

            minN, minI = 10000, -1
            for i in range(len(lists)):
                if lists[i] is not None and lists[i].val < minN:
                    minN, minI = lists[i].val, i
            
            if minI == -1:
                break
            
            if ret is None:
                head = ret = ListNode(minN)
            else:
                ret.next = ListNode(minN)
                ret = ret.next
        return head
