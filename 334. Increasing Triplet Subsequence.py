class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums)<3: return False

        low = mid = float('inf')

        for i,v in enumerate(nums):
            if v <= low: low = v
            elif v <= mid: mid = v
            else: return True
        
        return False