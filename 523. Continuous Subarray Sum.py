class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        total, n = sum(nums), len(nums)
        i, j = 0, n-1

        while i<j:
            if total % k == 0 : return True
            if n>2 and ((total - nums[i]) % k == 0 or (total - nums[j]) % k == 0): return True
            total -= (nums[i]+nums[j])
            i+=1; j-=1; n-=2

        return False
