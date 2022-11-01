class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        s = {}
        for i in range(0,len(nums)):
            if target - nums[i] not in s.keys(): s[nums[i]] = i
            else: return [i, s[target-nums[i]]]