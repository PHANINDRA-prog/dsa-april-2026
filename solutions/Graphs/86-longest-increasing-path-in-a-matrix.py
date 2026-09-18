class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        directions =  [(0,1),(0,-1),(1,0),(-1,0)]

        # In normal problems we use size to calculate how long are we able to go and then here it's a path and path cannot split so max and then we say from mine i don't know max size so let me child calculate and he comesback and says this is what i found and then we add 1 to say i am putting my choice to it

        @cache
        def dfs(r,c):
            max_size = 0

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if 0<=nr<ROWS and 0<=nc<COLS and matrix[r][c] < matrix[nr][nc]:
                    max_size = max(max_size ,dfs(nr,nc))
            
            return  1 + max_size
        
        max_size = 0
        for r in range(ROWS):
            for c in range(COLS):
                current_size = dfs(r,c)
                max_size = max(max_size,current_size)
        return max_size
                
