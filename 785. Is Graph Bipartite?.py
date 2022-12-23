class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        '''
        #union-find
        parent = [i for i in range(len(graph))]

        def find(x):
            return x if x == parent[x] else find(parent[x])
        
        def union(x,y):
            rX, rY = find(x), find(y)
            parent[rX] = rY
        
        for u in range(len(graph)):
            for v in graph[u]:
                if find(u) == find(v) : return False
                union(graph[u][0],v)
        return True
        '''

        #bfs
        color = [-1 for _ in range(len(graph))]

        for u in range(len(graph)):
            if color[u] == -1:
                q = collections.deque()
                q.append(u)
                color[u] = 0
                while q:
                    node = q.popleft()
                    for neighbor in graph[node]:
                        if color[neighbor] == color[node] : return False
                        if color[neighbor] == -1 :
                            color[neighbor] = 1 - color[node]
                            q.append(neighbor)
        return True
