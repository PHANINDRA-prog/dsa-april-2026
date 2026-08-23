class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(r,c,original_color):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            
            if image[r][c] != original_color:
                return
            
            image[r][c] = color

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == original_color:
                    dfs(nr,nc,original_color)
        
        if image[sr][sc] == color:
            return image
        dfs(sr,sc,image[sr][sc])
        return image
