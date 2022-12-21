class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        components = n
        parent = [i for i in range(n)]
        
        def find(A):
            return A if parent[A] == A else find(parent[A])
    
        def union(edge):
            rootA, rootB = map(find, edge)
            if rootA != rootB : parent[rootA] = rootB
            return 1 if rootA != rootB else 0

        for edge in edges:
            components -= union(edge)
        
        return components