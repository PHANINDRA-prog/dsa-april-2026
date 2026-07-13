class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    digit = board[r][c]
                    box = (r//3)*3 + c//3
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box].add(digit)
                else:
                    empties.append((r,c))
        

        def isValid(row,col,digit):
            box = (row//3)*3 + col//3

            if digit in rows[row]:
                return False
            
            if digit in cols[col]:
                return False
            
            if digit in boxes[box]:
                return False
            
            return True
        

        def helper(index):
            if index == len(empties):
                return True
            

            row,col = empties[index]
            box = (row//3)*3 + col//3

            for digit in "123456789":

                if not isValid(row,col,digit):
                    continue
                
                # Choose
                board[row][col] = digit
                rows[row].add(digit)
                cols[col].add(digit)
                boxes[box].add(digit)

                if helper(index+1):
                    return True
                
                # Undo

                board[row][col] = "."
                rows[row].remove(digit)
                cols[col].remove(digit)
                boxes[box].remove(digit)
            return False
        helper(0)