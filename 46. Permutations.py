class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans, n = [], len(nums)

        def helper(arr, visited):
            if len(visited) == n : ans.append(arr); return

            for i in range(n):
                if i in visited : continue
                helper(arr + [nums[i]], visited + [i])


        helper([], [])
        return ans

