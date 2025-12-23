class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        t = (row * col) - 1
        low = 0

        while low <= t:
            mid = low + (t - low) //2
            r = mid // col
            c = mid % col

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                low = mid + 1
            else:
                t = mid - 1
        return False
            
            
        