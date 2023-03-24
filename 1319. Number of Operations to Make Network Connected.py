class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n-1 : return -1

        parent = [x for x in range(n)]
        rank = [0 for _ in range(n)]

        def find(x):
            return x if x == parent[x] else find(parent[x])
        
        def union(rootX, rootY):
            if rootX == rootY : return
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
                rootX += 1
            else: 
                parent[rootX] = rootY
                rootY += 1
        
        for x, y in connections:
            union(find(x), find(y))
        
        return sum([1 for i, v in enumerate(parent) if i == v ]) - 1