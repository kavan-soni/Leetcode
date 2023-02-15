class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])

        ans = []
        def countSoldiers(i):
            l, r = 0, n
            while l < r:
                m = l + (r-l)//2
                if mat[i][m]==0: r = m
                else: l = m + 1
            ans.append([l,i])


        for i in range(m):
            countSoldiers(i)
        
        ans = [x[1] for x in sorted(ans)]
        return ans[:k]
        
            