class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1

        def convert_1d_to_2d(index):
            row = index // cols
            col = index % cols

            return row,col
        
        while left <= right:
            mid = (left + right)//2

            row,col = convert_1d_to_2d(mid)

            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] < target:
                left = mid + 1
            
            else:
                right = mid - 1
        return False
