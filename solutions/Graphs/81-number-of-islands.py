class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 
            
            if grid[r][c] == "0":
                return
            

            grid[r][c] = "0"

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                    dfs(nr,nc)
        island = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    island += 1
                    dfs(r,c)
        
        return island