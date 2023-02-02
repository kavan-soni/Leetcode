class Graph_Theory:
    '''
    Kruskal's Algorithm is used to find MST of a graph. It uses union-find.

    Pseudocode:
        1. Create a list of node edges with weights
        2. Sort the list based on weight
        3. Loop over each edge
        4. Verify the edge doesnt form a cycle -> use find()
        5. add edge to MST -> use union()
    '''
    def kruskalsAlgo(edges):

        n = len(edges)
        edges = sorted(edges, key = lambda x: x[0])

        parent = [x for x in range(n)]
        rank = [0 for _ in range(n)]

        def find(x):
            return x if x == parent[x] else find(parent[x])
        
        def union(x,y):
            rootX, rootY = find(x), find(y)
            
            if rootX != rootY :  # include edge in MST only if it does not form a cycle
                cost += w
                if rank[rootX] >= rank[rootY] :
                    parent[rootY] = parent[rootX]
                    MST.append(x); MST.append(y)
                    
                else : 
                    parent[rootX] = parent[rootY]
                    MST.append(y); MST.append(x)
                
                 
        MST, cost = list(), 0
        for (wt, x, y) in edges:
            union(x, y) 
            
        return [cost, MST]

        
        
        