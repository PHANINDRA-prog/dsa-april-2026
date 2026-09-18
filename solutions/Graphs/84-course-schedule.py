class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        graph = defaultdict(list)
        indegree = [0] * n
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        queue = deque()
        
        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)
        
        processed = 0
        while queue:

            node = queue.popleft()
            processed += 1

            for nei in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
        
        return processed == n
        

        