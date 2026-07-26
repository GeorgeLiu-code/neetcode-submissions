class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        square = {}
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                s = (r//3) * 3 + (c//3)
                if num == '.':
                    continue 
                    
                if num in rows.get(r,set()):
                    return False
                if num in cols.get(c,set()):
                    return False
                if num in square.get(s,set()):
                    return False
                rows.setdefault(r,set()).add(num)
                cols.setdefault(c,set()).add(num)
                square.setdefault(s,set()).add(num)
        return True
        