class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        directions = [(0,1),(1,0)]
        target = (m - 1,n - 1)

        @cache
        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0

            if (r,c) == target:
                return 1
            
            total_paths = 0
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    total_paths += dfs(nr,nc)
            return total_paths
        return dfs(0,0)
            
