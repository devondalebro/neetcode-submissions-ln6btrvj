class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid

        maxA = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.grid[r][c] == 1:
                    print('d')
                    maxA = max(maxA, self.dfs(r, c))
        
        return maxA

    def dfs(self, r, c):
        self.grid[r][c] = 5
        d = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        a = 1

        for dr, dc in d:
            rNew = r + dr
            cNew = c + dc
            if rNew < 0 or rNew >= len(self.grid):
                continue

            if cNew < 0 or cNew >= len(self.grid[0]):
                continue

            if self.grid[rNew][cNew] == 1:
                a += self.dfs(rNew, cNew)

        return a