class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        nums.append(float(inf))
        l, r = 0, len(nums)//2 

        def condition(m):
            return nums[2*m] < nums[2*m + 1] 

        while l<r:
            m = l + (r-l)//2
            if condition(m) : r = m
            else: l = m + 1
        return nums[2*l]