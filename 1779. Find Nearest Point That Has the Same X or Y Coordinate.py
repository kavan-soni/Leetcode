class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        min_dist = float(inf)
        idx = -1

        def valid(point):
            return point[0] == x or point[1] == y
        
        def dist(point):
            return abs(x-point[0]) + abs(y-point[1])

        for i, point in enumerate(points):
            if valid(point) and (d:=dist(point)) < min_dist : min_dist = d; idx = i
        return idx