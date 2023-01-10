class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:

        # Prim's Algorithm

        n = len(p)
        adj = collections.defaultdict(list)

        for i in range(n):
            for j in range(i+1, n):
                dist = abs(p[i][1]-p[j][1]) + abs(p[i][0]-p[j][0])
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        q = [[0,0]] #[dist, start_idx]
        visited = set()

        total_cost = 0

        while q and len(visited) < n:
            dist_to_node, node_idx = heapq.heappop(q)
            if node_idx in visited: continue
            
            total_cost += dist_to_node
            visited.add(node_idx)
            for dist_to_neighbor, neighbor_idx in adj[node_idx]:
                if neighbor_idx in visited: continue
                heapq.heappush(q, [dist_to_neighbor, neighbor_idx])

        return total_cost
            

        '''
        # Kruskal's Algorithm
        n = len(p)

        def edge(i,j):
            return [i,j,abs(p[j][0] - p[i][0]) + abs(p[j][1] - p[i][1])]
            
        edges = list(edge(i,j) for i in range(n) for j in range(i+1 ,n)) 
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
        '''












