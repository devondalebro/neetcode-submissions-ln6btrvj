class Solution:
    def dfs(self, r, c):
        self.grid[r][c] = '.'
        d = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        for dr, dc in d:
            rNew = r + dr
            cNew = c + dc
            if rNew < 0 or rNew >= len(self.grid):
                continue

            if cNew < 0 or cNew >= len(self.grid[0]):
                continue

            if self.grid[rNew][cNew] == '1':
                self.dfs(rNew, cNew)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        ret = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.grid[r][c] == '1':
                    ret += 1
                    self.dfs(r, c)
        
        return ret
        