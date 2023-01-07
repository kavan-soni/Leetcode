class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        def binary_search(x):
            l, r = 0, len(nums)
            while l<r:
                m = l+(r-l)//2
                if nums[m]>x: r = m
                else: l = m+1
            return l


        nums = sorted(nums)

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
    
        return [binary_search(q) for q in queries]


        