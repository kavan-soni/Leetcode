class Solution:
    def rob(self, nums: List[int]) -> int:

        @lru_cache(None)
        def helper(indx, flag):
            if flag == 0 and indx>= len(nums)-1 or flag == 1 and indx>=len(nums): return 0
            return max(nums[indx] + helper(indx+2, flag), helper(indx+1, flag))
        
        return max(helper(0,0), helper(1,1))if len(nums)>1 else nums[0]