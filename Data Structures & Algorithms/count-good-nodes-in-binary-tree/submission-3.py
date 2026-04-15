# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def countGood(root, stack):
            if root is None:
                return
            
            print(f'val is {root.val} and stack {stack}')

            nonlocal count
            if len(stack) == 0 or root.val >= stack[-1]:
                stack.append(root.val)
                count += 1
            
            countGood(root.left, stack[:])
            countGood(root.right, stack[:])
        countGood(root, [])
        return count
            

            
            

