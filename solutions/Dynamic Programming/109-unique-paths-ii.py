class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0
        
        directions = [(1,0),(0,1)]
        ROWS = len(grid)
        COLS = len(grid[0])


        target = (ROWS-1,COLS-1)
        

        @cache
        def helper(r,c):
            if (r,c) == target:
                return 1
            
            total_paths = 0
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == 0:
                    total_paths += helper(nr,nc)
            return total_paths
        return helper(0,0)

            
