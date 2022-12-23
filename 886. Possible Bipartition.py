class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        adjList = collections.defaultdict(list)
        for [x,y] in dislikes:
            adjList[x].append(y)
            adjList[y].append(x)
        
        #union-find
        parent = [i for i in range(n+1)]

        def find(x):
            return x if x == parent[x] else find(parent[x])
        
        def union(x,y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY : return False
            parent[rootX] = rootY
        
        for node in range(1,n+1):
            for neighbor in adjList[node]:
                if find(neighbor) == find(node) : return False
                union(neighbor,adjList[node][0])
        return True

            
        '''
        #bfs
        color = [-1 for i in range(n+1)]
        for i in range(1,n+1):
            if color[i] == -1 :

                q =  collections.deque()
                q.append(i)
                color[i] = 0
                while q:
                    node = q.popleft()
                    for neighbor in adjList[node]:
                        if color[neighbor] == color[node]: return False
                        if color[neighbor] == -1 : 
                            color[neighbor] = 1 - color[node]
                            q.append(neighbor)
        return True
        '''