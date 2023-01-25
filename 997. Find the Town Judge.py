class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1 and trust ==[] : return 1


        adj = collections.defaultdict(set)
        for x,y in trust:
            adj[y].add(x) # y is trusted by x

        def trusts(x): # check if x trusts anybody
            for i in adj:
                if x in adj[i]: return True
            return False

        print(adj)
        for i in range(1,n+1):
            if i in adj and len(adj[i]) == n-1 and not trusts(i): return i
        
        return -1


