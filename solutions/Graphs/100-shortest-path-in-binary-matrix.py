class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return - 1

        
        ROWS = len(grid)
        COLS = len(grid[0])
        target = (ROWS-1,COLS-1)

        directions = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
        
        queue = deque()
        visited = set()

        queue.append((0,0))
        visited.add((0,0))

        distance = 1
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                r,c = queue.popleft()
                if (r,c) == target:
                    return distance

                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visited and grid[nr][nc] == 0:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
                
            distance += 1
        return - 1
