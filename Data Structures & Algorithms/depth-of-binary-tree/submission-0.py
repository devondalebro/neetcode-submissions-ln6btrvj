# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getMaxDepth(root, 0)
    
    def getMaxDepth(self, root, currDepth):
        if root is None:
            return currDepth
        
        return max(self.getMaxDepth(root.left, currDepth + 1), 
                self.getMaxDepth(root.right, currDepth + 1))