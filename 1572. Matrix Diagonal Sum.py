class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(0,len(mat),1):
            ans += mat[i][i]
            ans += mat[i][-1-i]
        return ans if not len(mat)%2 else ans-mat[len(mat)//2][len(mat)//2]
            
  