class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

        m, n = len(grid), len(grid[0])
        answer = []

        for col in range(n):
            depth, stuck = 0, 0 

            while not (stuck or depth == m) :
                if (col == n-1 and grid[depth][col] == 1) or (col == 0 and grid[depth][col] == -1): stuck = 1
                elif grid[depth][col] == 1 and grid[depth][col+1] == -1 : stuck = 1
                elif grid[depth][col] == -1 and grid[depth][col-1] == 1 : stuck = 1
                if grid[depth][col] == 1: col +=1
                else: col -=1
                depth += 1

            if stuck : answer.append(-1)
            else : answer.append(col)

        return answer