class Solution(object):
    def searchMatrix(self, mat, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        l, r = 0, len(mat)
        while l < r: # search column 0
            m = l + (r-l)//2
            if mat[m][0] > target : r = m
            else: l = m + 1
        row = l - 1

        l, r = 0, len(mat[0])
        while l < r: # search row that may contain target
            m = l + (r-l)//2
            if mat[row][m] >= target: r = m
            else: l = m + 1 
        
        return mat[row][l] == target if l < len(mat[0]) else False