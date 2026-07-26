class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # same row and column need differ number
        # have 9 block, every block need differ number
        # list to set

        for i in range(len(board)):
            # every row board
            temp_row = set()
            for j in range(len(board)):
                # every row element board[i][j]
                if board[i][j] == '.':
                    continue
                if board[i][j] in temp_row:
                    return False
                temp_row.add(board[i][j])

        for i in range(len(board)):
            # every column board
            temp_column = set()
            for j in range(len(board)):
                # every column element board[j][i]
                if board[j][i] == '.':
                    continue
                if board[j][i] in temp_column:
                    return False
                temp_column.add(board[j][i])
        
        for row in range(0,9,3):
            for column in range(0,9,3):
                block = set()
                for i in range(row,row + 3):
                    for j in range(column, column + 3):
                        if board[i][j] == '.':
                            continue
                        if board[i][j] in block:
                            return False
                        block.add(board[i][j])
                
        return True

                