class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals: return [newInterval]
        if newInterval[0] >= intervals[-1][0]: intervals.append(newInterval)
        else:
            for i in range(len(intervals)):
                if intervals[i][0] < newInterval[0]: continue
                else: intervals.insert(i,newInterval)
        
        ans = [intervals.pop(0)]

        while intervals:
            if ans[-1][1] >= intervals[0][0]:
                ans[-1][0] = min(ans[-1][0], intervals[0][0])
                ans[-1][1] = max(ans[-1][1], intervals[0][1])
                del(intervals[0])
            else:
                ans.append(intervals.pop(0))
        return ans

            
            
