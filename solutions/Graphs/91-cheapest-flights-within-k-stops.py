class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dist = [float('inf')] * n
        graph = defaultdict(list)

        for u,v,w in flights:
            graph[u].append((v,w))
        
        dist[src] = 0

        queue = deque()
        queue.append((0,src))

        stops = 0

        while queue and stops <= k:
            level_size = len(queue)

            for _ in range(level_size):
                distance,node = queue.popleft()

                for nei,w in graph[node]:
                    new_dist = distance + w

                    if new_dist < dist[nei]:
                        dist[nei] = new_dist
                        queue.append((new_dist,nei))

            stops += 1
        return dist[dst] if dist[dst] != float('inf') else -1