class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points = sorted(points, key = lambda x: x[0])
        #print(points)

        count = 1

        max_start, min_end = points.pop(0)

        while points:

            curr = points.pop(0)
            #print(count, max_start, min_end, curr)

            if min_end >= curr[0]: # if curr overlaps with previous
                max_start = max(curr[0], max_start)
                min_end = min(curr[1], min_end)

            else:
                max_start, min_end = curr[0], curr[1]
                count += 1

        return count

