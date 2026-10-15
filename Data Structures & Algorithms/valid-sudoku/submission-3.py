class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for i in range(9):
            remaining = set("123456789")
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] not in remaining:
                    return False
                remaining.remove(board[i][j])

        #coloumns
        for i in range(9):
            remaining = set("123456789")
            for j in range(9):
                if board[j][i] == '.':
                    continue
                elif board[j][i] not in remaining:
                    return False
                remaining.remove(board[j][i])
        
        #3x3
        for x in range(3):
            for y in range(3):
                remaining = set("123456789")
                for i in range(x * 3, x * 3 + 3):
                    for j in range(y * 3, y * 3 + 3):
                        if board[i][j] == ".":
                            continue
                        elif board[i][j] not in remaining:
                            return False
                        remaining.remove(board[i][j])
        return True
