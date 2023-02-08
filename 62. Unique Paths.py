class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        count = 0

        dp = collections.defaultdict(int)

        def helper(x,y):
            if (x,y) in dp : return dp[(x,y)]
            if x > m-1 or y > n-1 : return 0
            
            if x == m-1 or y == n-1 : dp[(x,y)] = 1
            else : dp[(x,y)] = helper(x+1,y) + helper(x, y+1)
                
            
            return dp[(x,y)]

        return helper(0,0)