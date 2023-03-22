class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        parent = [x for x in range(n+1)]
        rank = [0 for _ in range(n+1)]
        
        def find(x):
            return x if x == parent[x] else find(parent[x])

        def union(rootX, rootY):
            if rootX == rootY : return
            if rank[rootX] > rank[rootY] : 
                rank[rootX] +=1
                parent[rootY] = rootX
            else : 
                rank[rootY] +=1
                parent[rootX] = rootY
        
        for x, y, dist in roads:
            union(find(x), find(y)) 
        
        ans = 10001
        for x, y, dist in roads:
            # continue if edge is not part of connected path between 1 and n
            if find(x) != find(1) : continue 
            ans = min(ans, dist)

        return ans











        

