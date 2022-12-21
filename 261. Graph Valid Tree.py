class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
            Q. What are the conditions for a graph to be a valid tree?
            1. graph is fully connected
            2. there are no cycles
        """

        relation = collections.defaultdict(list)
        for [p,c] in edges:
            relation[p].append(c)
            relation[c].append(p)

        visited = set()

        def dfs(k):
            if k<0 or k>=n or k in visited: return False # checks if there is a cycle
            visited.add(k)
            x = True
            for child in relation[k]:
                relation[child].remove(k) # removes trivial cycles in undirected graph
                x &= dfs(child)
            return x
        
        return len(visited) == n if dfs(0) else False # checks if graph is fully connected
