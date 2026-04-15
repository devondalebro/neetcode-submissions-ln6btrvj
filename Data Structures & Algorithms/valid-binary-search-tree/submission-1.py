# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def doValid(root, lo, hi):
            if root is None:
                return True
            
            if lo is not None and lo >= root.val:
                return False

            if hi is not None and hi <= root.val:
                return False
            
            l = doValid(root.left, lo, root.val)
            r = doValid(root.right, root.val, hi)

            return l and r
        
        return doValid(root, None, None)