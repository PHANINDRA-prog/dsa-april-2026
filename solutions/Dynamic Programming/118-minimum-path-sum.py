class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        
        directions = [(0,1),(1,0)]

        ROWS = len(grid)
        COLS = len(grid[0])

        target = (ROWS-1,COLS-1)

        @cache
        def helper(r,c):

            if (r,c) == target:
                return grid[r][c]
            
            min_cost = float('inf')
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if 0<=nr<ROWS and 0<=nc<COLS:
                    min_cost = min(min_cost,helper(nr,nc))
                
            return grid[r][c] + min_cost
        return helper(0,0)