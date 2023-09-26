class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_start = 0 
        row_end = len(matrix) - 1
        while row_start <= row_end:
            mid_row = (row_start + row_end) // 2
            col_start = 0
            col_end = len(matrix[mid_row]) - 1
            if target in range(matrix[mid_row][col_start], matrix[mid_row][col_end]+1):
                while col_start <= col_end:
                    mid_col = (col_start + col_end)//2
                    if matrix[mid_row][mid_col] == target:
                        return True
                    elif matrix[mid_row][mid_col] > target:
                        col_end = mid_col - 1
                    else:
                        col_start = mid_col + 1

            if target < matrix[mid_row][col_start]:
                row_end = mid_row - 1
            else:
                row_start = mid_row + 1
        return False