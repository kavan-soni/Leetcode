class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1

        def condition(idx):
            return nums[idx] >= target

        while l<r:
            m = l + (r-l) // 2
            if condition(m): r = m
            else: l = m + 1

        return l if nums[l] == target else -1