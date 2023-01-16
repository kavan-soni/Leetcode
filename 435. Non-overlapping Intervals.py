class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals, key = lambda x: (x[1]))
        count = 0
        prev_e = intervals[0][1]
        
        for i in range(1, len(intervals)):
            s, e = intervals[i][0], intervals[i][1]
            if s < prev_e : count+=1
            else: prev_e = e
        
        return count