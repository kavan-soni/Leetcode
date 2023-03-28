class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        adjList = defaultdict(list)
        dirList = defaultdict(list)

        for a,b in connections:
            adjList[a].append(b); adjList[b].append(a)
            dirList[a].append(b)

        count = 0
        visited = set()
        q = [(0,-1)]
        while q :
            node, parent = q.pop(0)
            visited.add(node)
            
            if node != 0 and parent not in dirList[node] : count += 1

            for child in adjList[node] :
                if child not in visited: q.append((child, node))
        
        return count