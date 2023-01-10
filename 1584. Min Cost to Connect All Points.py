class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        
        n = len(p)
        edges = list([i,j,abs(p[j][0] - p[i][0]) + abs(p[j][1] - p[i][1])] for i in range(n) for j in range(i+1 ,n)) 
        edges = sorted(edges, key = lambda x : x[2])

        parent = [i for i in range(n)]
        rank = [0 for _ in range(n)]

        def find(x):
            return x if parent[x] == x else find(parent[x])

        def union(x, y):
            if rank[x] > rank[y]: parent[y] = x
            elif rank[y] > rank[x]: parent[x] = y
            else: parent[y] = x; rank[x] += 1;

        
        cost = 0
        for a, b, dist in edges:
            rootA, rootB = find(a), find(b)
            if rootA == rootB: continue
            union(rootA, rootB)
            cost += dist
            
        return cost 
