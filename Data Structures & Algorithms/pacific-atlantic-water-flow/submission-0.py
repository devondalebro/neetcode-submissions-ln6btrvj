class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        dr, dc = [0, 0, -1, 1], [1, -1, 0, 0]
        
        def dfs(r, c, visit, prev):
            if (r < 0 or r == len(heights) 
                or c < 0 or c == len(heights[0]) or
                (prev is not None and heights[r][c] < prev)
                or (r, c) in visit
                ):
                return

            visit.add((r, c))
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                dfs(nr, nc, visit, heights[r][c])

        for c in range(len(heights[0])):
            dfs(0, c, pac, None)
            dfs(len(heights) - 1, c, atl, None)
        
        for r in range(len(heights)):
            dfs(r, 0, pac, None)
            dfs(r, len(heights[0]) - 1, atl, None)
        
        ret = []
        for r, c in pac:
            if (r, c) in atl:
                ret.append([r, c])
        
        return ret
