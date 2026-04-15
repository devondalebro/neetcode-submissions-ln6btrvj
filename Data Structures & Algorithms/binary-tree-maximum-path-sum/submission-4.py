# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        temp = -1000000
        def doMax(root):
            nonlocal temp
            if root is None:
                return 0
            maxLeft = doMax(root.left)
            maxRight = doMax(root.right)
            temp = max([maxLeft + root.val, maxRight + root.val, maxLeft + maxRight + root.val, root.val, temp])
            return max([maxLeft + root.val, maxRight + root.val, root.val])

        doMax(root)
        return temp