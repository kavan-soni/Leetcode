class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        ans, n = [], len(nums)

        def helper(arr = [], visited = []):
            if len(visited) == n : ans.append(arr); return

            for i in range(n):
                if i in visited: continue
                if i > 0 and nums[i] == nums[i-1]: continue
                helper(arr + [nums[i]], visited + [i])
        
        nums = sorted(nums)
        helper()
        return ans

        
