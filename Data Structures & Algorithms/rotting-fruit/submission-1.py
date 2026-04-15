class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dr = [0, 0, -1, 1]
        dc = [1, -1, 0, 0]
        ret = 0
        while True:
            rottingSet = set()
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] != 1:
                        continue
                    
                    hasAdjacentFreshFruit = False
                    for i in range(4):
                        nr, nc = r + dr[i], c + dc[i]
                        if nc < 0 or nr < 0 or nc >= len(grid[0]) or nr >= len(grid):
                            continue
                        if grid[nr][nc] == 0:
                            continue
                        elif grid[nr][nc] == 2:
                            rottingSet.add((r, c))
                            hasAdjacentFreshFruit = True
                            break
                        elif grid[nr][nc] == 1:
                            hasAdjacentFreshFruit = True
                    
                    if not hasAdjacentFreshFruit:
                        return -1
            
            if len(rottingSet) == 0:
                break
            
            for r, c in rottingSet:
                grid[r][c] = 2

            ret += 1
        
        return ret
                    