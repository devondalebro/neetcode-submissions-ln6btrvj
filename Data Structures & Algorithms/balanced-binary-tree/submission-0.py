# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def checkBalanced(root, height):
            nonlocal balanced
            if root is None:
                return height
            
            lHeight = checkBalanced(root.left, height + 1)
            rHeight = checkBalanced(root.right, height + 1)

            print(f'node {root.val} has lh {lHeight} and rh {rHeight}')

            if abs(lHeight - rHeight) > 1:
                balanced = False
            
            return max(lHeight, rHeight)
            
        checkBalanced(root, 0)
        
        return balanced
    
