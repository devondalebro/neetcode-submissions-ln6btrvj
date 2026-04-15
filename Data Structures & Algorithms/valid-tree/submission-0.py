class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        e = [[] for _ in range(n)]

        for i, j in edges:
            e[i].append(j)
            e[j].append(i)
        
        visited = set()

        def dfs(pre, cur):
            if cur in visited:
                return False
            
            visited.add(cur)
            for x in e[cur]:
                if x == pre:
                    continue
                if not dfs(cur, x):
                    return False
            
            return True
            

        
        return dfs(-1, 0) and len(visited) == n

        