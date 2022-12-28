class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) -1

        while l<r:
            m = l + (r-l)//2
            if target <= nums[m]: r = m
            else: l = m +1
        return l + 1 if target > nums[-1] else l