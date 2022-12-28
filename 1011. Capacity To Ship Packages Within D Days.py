class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def feasible(capacity):
            d = 1
            curr = 0
            for w in weights:
                if curr + w > capacity:
                    curr = 0
                    d += 1
                    if d > days: return False
                curr += w
            return True
        
        l, r = max(weights), sum(weights)
        while l < r:
            mid = l + (r-l)//2
            if feasible(mid): r = mid 
            else: l = mid + 1

        return l