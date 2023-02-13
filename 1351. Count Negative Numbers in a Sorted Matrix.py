class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n =len(grid[0])
        count = 0

        for row in grid:
            l, r = 0, n
            while l<r:
                m = l+(r-l)//2
                if row[m] < 0: r = m
                else: l = m+1
            count += n-l
        return count
            