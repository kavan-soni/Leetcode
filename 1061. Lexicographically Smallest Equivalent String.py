class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        parent = [i for i in range(26)]

        ord_a = ord("a")

        def find(x):
            return x if x == parent[x] else find(parent[x])
        
        def union(x,y):
            if x < y : parent[y] = parent[x]
            elif x > y : parent[x] = parent[y]
        
        for i in range(len(s1)):
            x, y = ord(s1[i]) - ord_a, ord(s2[i]) - ord_a
            rootX, rootY = find(x), find(y)
            union(rootX, rootY)

        genAns = lambda c: chr(find(ord(c) - ord_a) + ord_a)
        

        return "".join([genAns(c) for c in baseStr])
        


