class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = [[] for _ in range(numCourses)]

        for p in prerequisites:
            edges[p[0]].append(p[1])
        
        def dfs(visited, curr):
            if curr in visited:
                return False
            visited.add(curr)
            for v in edges[curr]:
                if not dfs(visited, v):
                    return False
            visited.remove(curr)
            return True

        for c in range(numCourses):
            if not dfs(set(), c):
                return False
        
        return True

