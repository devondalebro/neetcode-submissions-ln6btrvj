class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        inCol = [0] * n
        inLeftDiag = [0] * (2 * n - 1)
        inRightDiag = [0] * (2 * n - 1)

        def doNQueens(cur, i):
            if i == n:
                ret.append(cur[:])
                return

            for c in range(n):
                r = i
                ld = r + n - c - 1
                rd = r + c

                if inCol[c] or inLeftDiag[ld] or inRightDiag[rd]:
                    continue

                inCol[c], inLeftDiag[ld], inRightDiag[rd] = 1, 1, 1
                cur[r] = cur[r][:c] + 'Q' + cur[r][c + 1:]
                doNQueens(cur, i + 1)
                cur[r] = cur[r][:c] + '.' + cur[r][c + 1:]
                inCol[c], inLeftDiag[ld], inRightDiag[rd] = 0, 0, 0
        
        cur = ['.' * n for _ in range(n)]
        for c in cur:
            print(c)
        doNQueens(cur, 0)
        return ret