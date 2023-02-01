class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)
        for x,y,w in times:
            adj[x].append([y,w])

        d = {}
        pq = [(0,k)]
        while pq:
            time_from_src, node = heappop(pq)
            if node not in d:
                d[node] = time_from_src
                for nei, time_to_nei in adj[node]:
                    heappush(pq,[time_from_src+time_to_nei, nei])
                    
        if len(d) != n: return -1
        d = sorted(d.items(), key = lambda x: x[1])
        return d[-1][1]


         

        