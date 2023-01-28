class SummaryRanges:

    def __init__(self):
        self.intervals = list()

    def addNum(self, value: int) -> None:
        self.intervals.append([value,value])


    def getIntervals(self) -> List[List[int]]:

        ranges = sorted(self.intervals, key = lambda x: x[0]) 
        ans = []
        
        while ranges:
            interval = ranges.pop(0)
            if not ans: ans.append(interval); continue

            if ans[-1][1] + 1 >= interval[0]:
                ans[-1][0] = min(ans[-1][0], interval[0])
                ans[-1][1] = max(ans[-1][1], interval[1])
            else: ans.append(interval)
        
        self.intervals = ans
        return ans

        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()