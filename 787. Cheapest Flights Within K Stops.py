class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = collections.defaultdict(list)
        cost = collections.defaultdict(lambda : float(inf))

        for x, y, price in flights:
            adj[x].append([y,price])
        
        #print(adj[dst])
        
        #visited = set()
        q = [[src,0,-1]]

        min_price = float(inf)

        while q:
            node, price, stops = q.pop(0)
            if node == dst or stops == k : continue
            #if node in visited or stops > k : continue
            #if node == dst:
            #    if price < min_price : min_price = price
            #    continue
            #visited.add(node)

            for neighbor, nei_price in adj[node]:
                if price + nei_price >= cost[neighbor] : 
                    continue
                cost[neighbor] = price + nei_price
                q.append([neighbor, price + nei_price, stops + 1])
        
        return -1 if cost[dst] == float(inf) else cost[dst]
