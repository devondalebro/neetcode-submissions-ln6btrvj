class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                print(f"Row: {row} Col: {col} Val: {val}")
                square = int((row // 3) * 3 + col // 3)
                
                if val == '.':
                    continue
                elif val in rows[row]:
                    print(rows[row])
                    return False
                elif val in cols[col]:
                    print(cols[col])
                    return False
                elif val in squares[square]:
                    print(squares[square])
                    return False

                rows[row].add(val)
                cols[col].add(val)
                squares[square].add(val)
        
        return True