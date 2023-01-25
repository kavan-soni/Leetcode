class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans, n = [], len(nums)

        def helper(arr, index):
            ans.append(arr)

            for i in range(index, n):
                helper(arr + [nums[i]], i+1)


        
        helper([], 0)
        return ans