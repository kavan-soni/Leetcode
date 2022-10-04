class Solution:
    def rob(self, nums: List[int]) -> int:

        @lru_cache(None)
        def helper(indx):
            if indx >= len(nums): return 0
            return max(nums[indx]+helper(indx+2), helper(indx+1))

        return helper(0)