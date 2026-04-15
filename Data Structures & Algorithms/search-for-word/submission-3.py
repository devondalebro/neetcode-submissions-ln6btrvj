class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        used = set()
        rs = [1, 0, -1, 0]
        cs = [0, 1, 0, -1]
        def dfs(i, r, c):
            if i == len(word) - 1:
                nonlocal res
                res = True
                return

            for j in range(len(rs)):
                rNew, cNew = r + rs[j], c + cs[j]
                if rNew >= len(board) or rNew < 0:
                    continue
                if cNew >= len(board[0]) or cNew < 0:
                    continue
                if board[rNew][cNew] == word[i + 1] and tuple([rNew, cNew]) not in used:
                    used.add(tuple([rNew, cNew]))
                    dfs(i + 1, rNew, cNew)
                    used.remove(tuple([rNew, cNew]))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    used.add(tuple([r, c]))
                    dfs(0, r, c)
                    used.remove(tuple([r, c]))
        return res