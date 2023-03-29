class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
        
        directions = [(1, 0), (0, 1)]
        valid = lambda r, c : 0<=r<n and 0<=c<m
        
        dp = defaultdict(int)
        dp[(n-1, m-1)] = grid[n-1][m-1]

        def helper(r, c):
            if (r,c) in dp : return dp[(r,c)]

            temp = sys.maxsize
            for x, y in directions :
                if valid(r+x, c+y) : temp = min(temp, grid[r][c] + helper(r+x, c+y))
            
            dp[(r,c)] = temp
            return temp

        
        return helper(0, 0)
