class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n-1 : return -1
        parent = [i for i in range(n)]
        rank = [0 for _ in range(n)]

        def find(x):
            return x if parent[x] == x else find(parent[x])

        def union(x,y, rootX, rootY):
            if rank[rootX] > rank [rootY] : parent[rootY] = rootX
            elif rank[rootX] < rank[rootY] : parent[rootX] = rootY
            else: parent[rootY] = rootX; rank[rootX] +=1;

    
        connections = sorted(connections, key = lambda x: x[2] )
        total_cost = 0
        total_edges = 0

        for u,v,cost in connections:
            rootX, rootY = find(u-1), find(v-1)
            if rootX == rootY: continue
            union(u-1,v-1, rootX, rootY)
            total_cost += cost
            total_edges +=1

        
        return total_cost if total_edges == n-1 else -1
            
