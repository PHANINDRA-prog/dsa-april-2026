class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]

        # To check whether it is safe to place queen or not
        def isSafe(row,col):

            r = row
            # Check the column
            while r >= 0:
                if board[r][col] == "Q":
                    return False
                
                r -= 1
            
            # Check the left diagnol

            r = row
            c = col

            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1
            
            # Check the right diagnol

            r = row
            c = col

            while r >=0 and c < n:
                if board[r][c] == "Q":
                    return False
                
                r -= 1
                c += 1
            
            return True # If no one return executed above then i am going to return True as we can place the queen at that particular grid block
        

        def solveNQueens(row):

            if row == n:
                solution = []
                for r in board:
                    solution.append("".join(r))
                return [solution]
            

            answers = []
            for col in range(n):
                if not isSafe(row,col):
                    continue
                
                # Choose
                board[row][col] = "Q"
                child = solveNQueens(row+1)

                answers.extend(child)

                # Now Undo
                board[row][col] = "."
            return answers
        return solveNQueens(0)
                
