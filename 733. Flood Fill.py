class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        start_color = image[sr][sc] 
        visited = set()

        def helper(r, c):
            if r<0 or c<0 or r > m-1 or c > n-1 : return
            if (r,c) in visited or image[r][c] != start_color: return
            image[r][c] = color
            visited.add((r,c))
            for (x,y) in [(-1,0), (1,0), (0,-1), (0,1)]:
                helper(r+x, c+y)
        
        helper(sr, sc)
        return image