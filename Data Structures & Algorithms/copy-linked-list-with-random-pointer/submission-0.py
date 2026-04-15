"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeDict = {}

        c = head
        while c is not None:
            nodeDict[c] = Node(c.val)
            c = c.next

        new = None
        ret = None
        c = head
        while c is not None:
            if new is None:
                ret = new = nodeDict[c]
            else:
                new.next = nodeDict[c]
                new = new.next
            
            if c.random is None:
                new.random = None
            else:
                new.random = nodeDict[c.random]
            
            c = c.next
        
        return ret