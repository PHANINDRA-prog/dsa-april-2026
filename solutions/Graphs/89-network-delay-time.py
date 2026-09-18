class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        dist = [[float('inf')] * n for _ in range(n)]

        source = k -1

        # Intial filling of the dist array

        for i in range(n):
            dist[i][i] = 0
        
        for u,v,w in times:
            dist[u-1][v-1] = w

        graph = defaultdict(list)
        edges = []

        # First build the graph
        # for u,v,w in times:
        #     graph[u-1].append((v-1,w))
        
        # Now the same we can do with bellman if there are negative cycles involved
        for u,v,w in times:
            edges.append((u-1,v-1,w))
        
        
        # heap = [(0,k-1)]

        # while heap:
        #     distance,node = heapq.heappop(heap)

        #     if distance > dist[node]:
        #         continue

        #     for nei,w in graph[node]:
        #         new_dist = distance + w

        #         if new_dist < dist[nei]:
        #             dist[nei] = new_dist
        #             heapq.heappush(heap,(new_dist,nei))
        
        # min_time = max(dist)
        # return min_time if min_time != float('inf') else -1 

        # for _ in range(n-1):
        #     changed = False
        #     for u,v,w in edges:
        #         if dist[u] == float("inf"):
        #             continue
        #         new_dist = dist[u] + w

        #         if new_dist < dist[v]:
        #             dist[v] = new_dist
        #             changed = True
        #     if not changed:
        #         break
        
        # for u,v,w in edges:
        #     if dist[u] == float('inf'):
        #         continue
            
        #     if dist[u] + w < dist[v]:
        #         return None
        # print(dist)
        # min_time = max(dist)
        # return min_time if min_time != float('inf') else -1

        # Now Floyd Warshall time
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] == float('inf'):
                        continue
                    elif dist[k][j] == float('inf'):
                        continue
                    dist[i][j] = min(dist[i][j] , dist[i][k] + dist[k][j])

        for i in range(n):
            if dist[i][i] < 0:
                return None
        
        source_row = dist[source]

        max_time = max(source_row)

        return max_time if max_time != float('inf') else -1
            