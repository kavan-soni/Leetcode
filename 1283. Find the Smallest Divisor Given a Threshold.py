class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:


        l, r = 1, max(nums)

        def condition(divisor):
            return threshold >= sum([math.ceil(num/divisor) for num in nums])

        while l<r:

            mid = l + (r-l)//2
            if condition(mid): r = mid
            else: l = mid+1
        return l

