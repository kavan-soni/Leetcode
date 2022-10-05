class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        prefixsum = [nums[0]]
        for i in range(1, len(nums)):
            prefixsum.append(nums[i] + prefixsum[i-1])

        if prefixsum[-1]-prefixsum[0] == 0 : return 0
        #if prefixsum[-2] == 0: return len(nums)-1
        
        for i in range(1, len(nums)):
            if prefixsum[i-1] == prefixsum[-1] - prefixsum[i]: return i
        return -1
        