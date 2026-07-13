class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["."] * n for _ in range(n)]
        
        def isSafe(row,col):

            # First check the col
            r = row
            while r >=0:
                if board[r][col] == "Q":
                    return False
                r -= 1
            
            # Now check the left diagonal

            r = row
            c = col

            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                
                r -= 1
                c -= 1
            
            # Now check the right diagonal

            r = row 
            c = col

            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                
                r -= 1
                c += 1
            
            return True
        

        def solveNQueens(row):

            if row == n:
                return 1
            
            total_valid_paths = 0
            for col in range(n):
                if not isSafe(row,col):
                    continue
                
                # Choose Case
                board[row][col] = "Q"
                child = solveNQueens(row+1)
                total_valid_paths += child

                #Undo
                board[row][col] = "."
            return total_valid_paths
        return solveNQueens(0)

