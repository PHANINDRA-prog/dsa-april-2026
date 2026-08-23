class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        visited = [[False] * COLS for _ in range(ROWS)]

        queue = deque()

        # Due to multiple rotten oranges might be there we record all the starting points in the queue and then also record the fresh oranges in the process

        fresh_oranges = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        time = 0
        
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (0<=nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        queue.append((nr,nc))

                        fresh_oranges -= 1
            if queue:
                time += 1
        
        return time if fresh_oranges == 0 else -1
