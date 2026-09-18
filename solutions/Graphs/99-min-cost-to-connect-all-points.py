class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # Prim Algorithmn

        x,y = points[0]
        visited = set()
        n = len(points)

        heap = [(0,x,y)]

        total = 0
        components_connected = 0

        while heap:
            distance , x, y = heapq.heappop(heap)

            if (x,y) in visited:
                continue

            total += distance
            components_connected += 1
            visited.add((x,y))

            for point in points:
                x2,y2 = point
                if (x2,y2) not in visited:
                    cost = abs(x-x2) + abs(y-y2)
                    heapq.heappush(heap,(cost,x2,y2))
        
        return total
