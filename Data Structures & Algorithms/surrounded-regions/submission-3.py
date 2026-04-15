class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # whist traversing an 'O' region
        # if we encounter one on the boundary
        # then it is not surrounded
        dr = [0, 0, -1, 1]
        dc = [1, -1, 0, 0]
        def dfs(r, c, curr):
            curr.add((r, c))
            for i in range(4):
                rNew, cNew = r + dr[i], c + dc[i]
                if rNew < 0 or rNew >= len(board) or cNew < 0 or cNew >= len(board[0]):
                    print((r, c))
                    return False
                if (rNew, cNew) in curr:
                    continue
                if board[rNew][cNew] == 'X':
                    continue
                if not dfs(rNew, cNew, curr):
                    return False
                
            return True

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X':
                    continue
                oRegion = set()
                if dfs(r, c, oRegion):
                    for row, col in oRegion:
                        board[row][col] = 'X'
        
        # o x x o x
        # x o o x o
        # x o x o x
        # o x o o o
        # x x o x o
