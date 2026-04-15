# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []

        def rightFillList(root, height):
            if root is None:
                return
            nonlocal ret
            if len(ret) <= height:
                ret.append(root.val)

            rightFillList(root.right, height + 1)            
            rightFillList(root.left, height + 1)            

        rightFillList(root, 0)
        return ret
        