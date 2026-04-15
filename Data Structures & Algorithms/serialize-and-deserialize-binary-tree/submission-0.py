# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ret = ""

        def doSerialise(root):
            nonlocal ret
            if root is None:
                ret += "n,"
            else:
                ret += f'{root.val},'
                doSerialise(root.left)
                doSerialise(root.right)
        doSerialise(root)
        return ret
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def doDeserialise():
            nonlocal data
            if len(data) == 0:
                return None
            
            valStr = data[:data.index(',')]
            data = data[data.index(',') + 1:]
            if valStr == 'n':
                return None
            val = int(valStr)
            root = TreeNode(val)
            root.left = doDeserialise()
            root.right = doDeserialise()
            return root
        
        return doDeserialise()
