# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def doDiameter(root, height):
            nonlocal diameter
            if root is None:
                return height - 1

            lHeight = doDiameter(root.left, height + 1) - height
            rHeight = doDiameter(root.right, height + 1) - height

            print(f'at node {root.val} height is {height} lheight is {lHeight} rheight is {rHeight}')

            diameter = max(diameter, lHeight + rHeight)

            return max(lHeight + height, rHeight + height)

        doDiameter(root, 0)
        return diameter
        
