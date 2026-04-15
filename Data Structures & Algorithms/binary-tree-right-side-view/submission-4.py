# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        view = []

        def rhs(r, h):
            if r is None:
                return

            if h == len(view):
                view.append(r.val)
            

            rhs(r.right, h + 1)
            rhs(r.left, h + 1)
        
        rhs(root, 0)
        return view