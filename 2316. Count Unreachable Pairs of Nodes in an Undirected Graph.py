class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        def find(x):
            return x if x == parent[x] else find(parent[x])
        
        def union(x_root, y_root):
            if x_root == y_root: return
            if rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
                rank[x_root] += rank[y_root]
                rank[y_root] = 0
            else:
                parent[x_root] = y_root
                rank[y_root] += rank[x_root]
                rank[x_root] = 0
        

        rank = [1 for _ in range(n)] # denotes cluster size
        parent = [x for x in range(n)]
        for x, y in edges:
            union(find(x), find(y))

        def suffix_sum(arr):
            ss = [sum(arr) - arr[0]]
            for i in range(1, len(arr)):
                ss.append(ss[i-1] - arr[i])
            return ss

        ans = 0
        clusters_size = list(x for x in rank if x != 0)
        ss = suffix_sum(clusters_size)

        for i in range(len(clusters_size)) :
            ans += clusters_size[i] * ss[i]
        return ans