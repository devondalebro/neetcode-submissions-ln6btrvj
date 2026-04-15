# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []

        def levelFillList(root, height):
            if root is None:
                return
            nonlocal ret

            if len(ret) <= height:
                ret.append([])
            
            ret[height].append(root.val)
            levelFillList(root.left, height + 1)
            levelFillList(root.right, height + 1)
        
        levelFillList(root, 0)
        
        return ret