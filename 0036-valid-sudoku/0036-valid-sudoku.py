class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grid_set = set()
        for row in range(0,len(board),3):
            for col in range(len(board[row])):
                if col == 0 or col == 3 or col == 6:
                    print(grid_set)
                    grid_set = set()
                if board[row][col] != ".": 
                    if board[row][col] not in grid_set:
                        grid_set.add(board[row][col])
                    else:
                        return False
                if board[row+1][col] != ".":
                    if board[row+1][col] not in grid_set:
                        grid_set.add(board[row+1][col])
                    else:
                        return False
                if board[row+2][col] != ".":
                    if board[row+2][col] not in grid_set:
                        grid_set.add(board[row+2][col])
                    else:
                        return False
        for row in range(len(board)):
            
            row_set = set()
            for col in range(len(board[row])):
                if board[row][col] in row_set:
                    return False
                if board[row][col] != ".":
                    row_set.add(board[row][col])
        for col in range(len(board[0])):
            
            col_set = set()
            for row in range(len(board)):
                if board[row][col] in col_set:
                    return False
                if board[row][col] != ".":
                    col_set.add(board[row][col])
        return True
        
                                       
            