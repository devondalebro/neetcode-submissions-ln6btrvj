class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            prereqs[crs].append(pre)

        output = []
        visited, path = set(), set()

        # do dfs
        def dfs(crs):
            if crs in path:
                return False
            if crs in visited:
                return True
                
            visited.add(crs)
            path.add(crs)

            for p in prereqs[crs]:
                if dfs(p) is False:
                    return False

            path.remove(crs)
            output.append(crs)


        for c in range(numCourses):
            if dfs(c) is False:
                return []
        
        return output