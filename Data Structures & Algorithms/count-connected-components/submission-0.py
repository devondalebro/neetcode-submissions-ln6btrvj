class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        e = [[] for _ in range(n)]
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for i in e[node]:
                dfs(i)
        
        for i, j in edges:
            e[i].append(j)
            e[j].append(i)
        
        ret = 0
        for i in range(n):
            if i not in visited:
                ret += 1
            dfs(i)
        
        return ret