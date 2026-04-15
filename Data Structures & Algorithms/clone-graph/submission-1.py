"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # dfs og graph
        nodes = dict()
        visited = set()
        def dfs(node):
            if node is None:
                return

            if node.val in visited:
                return
            else:
                visited.add(node.val)

            if node.val in nodes:
                newNode = nodes[node.val]
            else:
                newNode = Node(node.val)
                nodes[node.val] = newNode
            
            for nb in node.neighbors:
                if nb.val in nodes:
                    newNb = nodes[nb.val]
                else:
                    newNb = Node(nb.val)
                    nodes[nb.val] = newNb

                newNode.neighbors.append(newNb)
                dfs(nb)
        
        dfs(node)
        
        if node is None:
            return None
        return nodes[node.val]
