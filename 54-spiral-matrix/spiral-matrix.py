class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        min_row,max_row = 0, len(matrix)
        min_col, max_col = 0, len(matrix[0])
        row = 0
        output = []
        while min_row<max_row and min_col < max_col:
            for col in range(min_col, max_col):
                output.append(matrix[row][col])
            min_row += 1

            for row in range(min_row, max_row):
                output.append(matrix[row][col])
            max_col -= 1

            if min_row<max_row and min_col < max_col:
                for col in range(max_col - 1, min_col - 1, -1):
                    output.append(matrix[row][col])

                max_row -= 1

                for row in range(max_row - 1, min_row - 1, -1):
                    output.append(matrix[row][col])
                
                min_col += 1
        return output
            