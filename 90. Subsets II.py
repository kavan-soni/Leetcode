class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans, n = [], len(nums)

        def helper(arr, index):

            ans.append(arr)

            for i in range(index, n):
                if i > index and nums[i] == nums[i-1] : continue
                helper(arr + [nums[i]], i+1)
            
        
        nums = sorted(nums)
        
        helper([],0)
        return ans