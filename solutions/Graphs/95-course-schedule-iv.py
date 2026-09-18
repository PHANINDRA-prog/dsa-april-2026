class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        answer = []

        graph = defaultdict(list)

        indegree = [0] * n

        prereqs_of = [set() for _ in range(n)]

        queue = deque()

        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            

            for nei in graph[node]:
                indegree[nei] -= 1
                prereqs_of[nei].add(node)
                prereqs_of[nei].update(prereqs_of[node])
                if indegree[nei] == 0:
                    queue.append(nei)

        for u,v in queries:
            
            answer.append(u in prereqs_of[v])
        
        return answer
            