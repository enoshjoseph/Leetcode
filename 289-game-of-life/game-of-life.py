class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                count = 0

                curr = [(r+1, c), (r-1, c),(r, c+1), (r, c-1), (r+1, c+1), (r - 1, c+1), (r - 1, c - 1), (r+1, c-1) ]

                for i, j in curr:
                    if i >=0 and j>=0 and i<rows and j < cols and (board[i][j] == 1 or board[i][j] == 2):
                        count += 1
                
                if board[r][c] == 1 and (count <2 or count > 3):
                    board[r][c] = 2
                
                elif board[r][c] == 0 and count == 3:
                    board[r][c] = -1

        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 2:
                    board[row][col] = 0
                elif board[row][col] == -1:
                    board[row][col] = 1
    
