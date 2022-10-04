class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @lru_cache(None)
        def helper(i, curr):
            if i> len(nums): return 0
            if i == len(nums) and curr == target : return 1
            if i == len(nums) : return 0
            return helper(i+1, curr+nums[i]) + helper(i+1, curr-nums[i])
        return helper(0, 0)
