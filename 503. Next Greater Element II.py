class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        stack, d, n = [], {}, len(nums)

        for i in range(n*2):
            while stack and nums[i%n] > nums[stack[-1]%n]:
                d[stack.pop()] = i%n
            stack.append(i)
        
        ans = []
        for i in range(n):
            idx = d.get(i, -1)
            if idx == -1: ans.append(-1)
            else: ans.append(nums[idx])
        return ans