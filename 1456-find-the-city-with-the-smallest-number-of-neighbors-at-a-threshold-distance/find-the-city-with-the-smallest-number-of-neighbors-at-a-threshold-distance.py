class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = float("inf")
        dist = [[INF]*n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for v,u,w in edges:
            dist[v][u] = w
            dist[u][v] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        count = [-1]*(n)
        for i in range(n):
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    count[i] += 1
        minimum = float("inf")
        res = INF
        for i in range(len(count)):
            if count[i] <= minimum:
                minimum = count[i]
                res = i

        return res
            
