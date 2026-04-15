class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqrs = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                sqr = int((row // 3) * 3) + int(col // 3)

                if val == '.':
                    continue
                if val in rows[row]:
                    return False
                if val in cols[col]:
                    return False
                if val in sqrs[sqr]:
                    return False
                
                rows[row].add(val)
                cols[col].add(val)
                sqrs[sqr].add(val)
        
        return True
