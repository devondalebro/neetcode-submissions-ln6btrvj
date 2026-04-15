# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def doKth(root):
            nonlocal k
            nonlocal ans
            if root is None:
                return 0
            
            doKth(root.left)
            k -= 1
            print(f'current val is {root.val} and k {k}')
            if k == 0:
                ans = root.val
            
            doKth(root.right)
        
        doKth(root)
        return ans
        