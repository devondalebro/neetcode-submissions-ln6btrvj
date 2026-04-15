# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        l = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+l], inorder[:l])
        root.right = self.buildTree(preorder[1+l:], inorder[1+l:])
        return root