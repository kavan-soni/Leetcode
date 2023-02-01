import heapq
import collections

class Graph_Theory:

    '''
    Dijkstra's Algorithm is a single source shortest path algorithm that 
    works for non negative edge weights.
    It finds shortest distance form source node to all other nodes.
    '''
    def dijkstrasAlgo(arr, src):

        adj = collections.defaultdict(list)
        for (u, v, w) in arr:
            adj[u].append(v,w)
        
        pq = [(0,src)]
        shortest_path_from_src = {}

        while pq:
            dist_from_src, node = heapq.heappop(pq)
            if node not in shortest_path_from_src:
                shortest_path_from_src[node] = dist_from_src
                for (dist_to_nei, neighbor) in adj[node]:
                    heapq.heappush(pq, (dist_from_src + dist_to_nei, neighbor))
        
        return shortest_path_from_src
        

        
