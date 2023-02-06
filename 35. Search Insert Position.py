class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) # since target can be greater than max value in array, right boundary is set as len(nums)

        def condition(x):
            return nums[x]>=target

        while l<r:
            m = l + (r-l)//2
            if condition(m): r = m
            else: l = m +1
        return l
