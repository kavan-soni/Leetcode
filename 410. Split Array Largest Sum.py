class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:  

        def feasible(largest_sum):
            curr_sum, curr_k = 0, 1

            for num in nums:
                if curr_sum + num > largest_sum:
                    curr_sum = 0
                    curr_k += 1
                    if curr_k > k : return False
                curr_sum += num
            return True

        l = max(nums) # least value of [largest sum of any subarray], when k = len(nums)
        r = sum(nums) # greatest value of [largest sum of any subarray], when k = 1

        while l < r:

            m = l + (r-l)//2
            if feasible(m): 
                r = m
            else: 
                l = m + 1

        return l
