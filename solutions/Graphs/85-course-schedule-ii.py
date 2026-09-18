class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        n = numCourses

        graph = defaultdict(list)
        indegree = [0] * n
        heap = []

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        for node in range(n):
            if indegree[node] == 0:
                heapq.heappush(heap,node)
        topo = []
        while heap:
            node = heapq.heappop(heap)
            topo.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    heapq.heappush(heap,nei)
        
        return topo if len(topo) == n else []
        
        

