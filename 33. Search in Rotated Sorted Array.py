class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l < r: 
            m = l + (r-l)//2
            if nums[m] < nums[0]: r = m
            else: l = m + 1
        pivot = l
        
        if nums[pivot] <= target <= nums[-1] : l, r = pivot, len(nums)
        else: l, r = 0, pivot

        while l < r:
            m = l + (r-l)//2
            if nums[m] >= target: r = m
            else: l = m + 1
        return l if nums[l] == target else -1