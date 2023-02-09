class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        n = numRows

        ans = [[0]*i for i in range(1,n+1)]
        ans[0][0] = 1

        for i in range(n-1):
            for j in range(i+1):
                ans[i+1][j] += ans[i][j]
                ans[i+1][j+1] += ans[i][j]
        
        return ans

            




        