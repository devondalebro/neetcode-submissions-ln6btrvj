class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        landCell = 2147483647

        dr = [0, 0, -1, 1]
        dc = [1, -1, 0, 0]

        def bfs(r, c):
            head = 0
            q = []
            visited = set()
            dist = dict()

            q.append((r, c))
            visited.add((r, c))
            dist[(r, c)] = 0

            while head != len(q):
                row, col = q[head]
                head += 1
                visited.add((row, col))
                if grid[row][col] == -1:
                    continue
                if grid[row][col] == 0:
                    return dist[(row, col)]


                for i in range(4):
                    newR, newC = row + dr[i], col + dc[i]
                    if (newR, newC) in visited:
                        continue
                    if newR < 0 or newR >= len(grid):
                        continue
                    if newC < 0 or newC >= len(grid[0]):
                        continue
                    q.append((newR, newC))
                    dist[(newR, newC)] = dist[(row, col)] + 1
                    
            return landCell
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == landCell:
                    grid[r][c] = bfs(r, c)
            