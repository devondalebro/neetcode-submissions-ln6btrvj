# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        isSub = self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        if root.val == subRoot.val:
            return self.checkSubtree(root, subRoot) or isSub
        
        return isSub
        
    def checkSubtree(self, root, sub):
        if root is None and sub is None:
            return True
        
        if not(root is not None and sub is not None):
            return False
        
        if root.val != sub.val:
            return False
        
        return self.checkSubtree(root.left, sub.left) and self.checkSubtree(root.right, sub.right)