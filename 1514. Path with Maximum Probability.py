class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        adj = defaultdict(list)
        for i in range(len(edges)):
            x, y = edges[i]
            adj[x].append((succProb[i], y))
            adj[y].append((succProb[i], x))

        pq = [(-1,start)]
        visited = set()

        while pq:
            prob, node = heapq.heappop(pq)
            if node == end: return -prob

            visited.add(node)
            for nei_prob, nei in adj[node]:
                if nei not in visited: heapq.heappush(pq, [prob * nei_prob, nei])
        
        return 0






