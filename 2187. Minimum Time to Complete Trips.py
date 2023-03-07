class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        d = defaultdict(int)
        for num in time:
            d[num] += 1
        
        def enough(t):
            trips = 0
            for x in d :
                trips += d[x] * (t//x)
            return trips >= totalTrips

        l, r = 1, totalTrips * max(time) 
        while l < r :
            m = l + (r-l)//2
            if enough(m) : r = m
            else: l = m + 1
        return l

            