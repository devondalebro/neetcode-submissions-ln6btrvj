# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -10000
        def doMaxSum(root):
            nonlocal maxSum
            if root is None:
                return 0
            leftSum = doMaxSum(root.left)
            rightSum = doMaxSum(root.right)
            possibleSums = [root.val, max(leftSum, rightSum) + root.val]
            maxSum = max(maxSum, max(possibleSums))
            maxSum = max(maxSum, leftSum + rightSum + root.val)
            return max(possibleSums)
        
        doMaxSum(root)
        return maxSum