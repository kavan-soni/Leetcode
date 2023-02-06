class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])

        def helper(x,y):
            if x < 0 or y < 0 or x > m-1 or y > n-1 : return
            if grid[x][y] != "1": return
    
            grid[x][y] = "*"
            for (a,b) in [(-1,0),(1,0),(0,-1),(0,1)]:
                helper(x+a, y+b)


        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1": 
                    count +=1
                    helper(i,j)
                    
        
        return count
            