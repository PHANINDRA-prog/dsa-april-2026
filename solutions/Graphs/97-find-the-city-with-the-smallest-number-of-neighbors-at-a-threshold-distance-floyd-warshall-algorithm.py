class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Floyds Algo 

        dist = [[float('inf')]* n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0
        
        for u,v,w in edges:
            dist[u][v] = w
            dist[v][u] = w
            
        
        
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] == float('inf'):
                        continue
                    
                    if dist[k][j] == float('inf'):
                        continue
                    
                    dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
        
        # print(dist)
        
        best_score = float('inf')
        best_node = None
        for i in range(n):
            score = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    score += 1
            if score <= best_score:
                best_node = i
                best_score = score
        return best_node
        
