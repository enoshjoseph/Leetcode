class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])
        
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        for r in range(rows):
            for c in range(cols):
                count = 0
                curr = [(r+1, c), (r-1, c),(r, c+1), (r, c-1), (r+1, c+1), (r-1, c-1), (r-1, c+1), (r+1, c-1)]

                for i,j in curr:
                    if i >= 0 and j >= 0 and i<rows and j < cols and copy_board[i][j] == 1:
                        count += 1

                if copy_board[r][c] == 1:
                    if count < 2 or count > 3:
                        board[r][c] = 0
                
                else:
                    if count == 3:
                        board[r][c] = 1
